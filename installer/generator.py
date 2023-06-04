from jinja2 import Environment, FileSystemLoader
import json
import shutil
import glob
import os
import subprocess
import time
from firebase import create_account

def wait_for_container_health(container_name, timeout=3600):
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            output = subprocess.check_output(['docker', 'ps', '--format', '{{json .}}'])
            containers = [line for line in output.decode().split('\n') if line.strip()]
            
            for container in containers:
                container_info = json.loads(container)
                if container_info['Names'] == container_name:
                    status = container_info['Status']
                    if 'healthy' in status:
                        return

            time.sleep(1)

        except subprocess.CalledProcessError:
            pass

    raise TimeoutError(f"Timeout while waiting for container '{container_name}' to become healthy.")

def generate(config_file_path, username, password):
    print('Parsing config...')

    # Open the config file
    with open(config_file_path, 'r') as f:
        config = json.load(f)

    # Parameters
    num_dummy_pc = config['dummy_pc']['num_services'] if 'dummy_pc' in config else None
    ip_addresses_dummy_pc = config['dummy_pc']['ip_addresses'] if 'dummy_pc' in config else None
    ftp_port = config['ftp']['port'] if 'ftp' in config else None
    ftp_ip_address = config['ftp']['ip_address'] if 'ftp' in config else None
    interface = config['interface']
    subnet = config['subnet']
    dockerfile = config['dockerfile']

    # Load the template file
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    print('Generating docker compose...')

    # Load the main template
    template = env.get_template('docker-compose-template.yml')

    # Render the main template with the number of services and the IP addresses
    output = template.render(
        num_dummy_pc=num_dummy_pc,
        ip_addresses_dummy_pc=ip_addresses_dummy_pc,
        ftp_port=ftp_port,
        ftp_ip_address=ftp_ip_address,
        interface=interface,
        subnet=subnet,
        dockerfile=dockerfile
    )

    print('Copying honeypot modules...')

    # Copy docker files
    shutil.copytree('./modules', './build/modules', dirs_exist_ok=True)

    print('Copying honeypot core services...')

    shutil.copytree('../fail2ban', './build/honeypot/fail2ban', dirs_exist_ok=True)
    shutil.copytree('../logs', './build/honeypot/logs', dirs_exist_ok=True)
    shutil.copytree('../nginx', './build/honeypot/nginx', dirs_exist_ok=True)
    shutil.copytree('../shop', './build/honeypot/shop', dirs_exist_ok=True)
    shutil.copytree('../suricata', './build/honeypot/suricata', dirs_exist_ok=True)
    shutil.copy('../fail2ban.env', './build/honeypot/fail2ban.env')

    # Write the output to a file
    with open('build/docker-compose.yml', 'w') as f:
        f.write(output)

    print("[OK] Docker Compose file has been created.")

    print("Starting honeypot services...")

    subprocess.run(['docker', 'compose', '-f', './build/docker-compose.yml', 'up', '-d'], cwd='.')
    
    print("[OK] Docker services started.")

    wait_for_container_health('backend')
    
    print("Creating account...")

    create_account(username, password)

    print("[OK] Account created.")

    wait_for_container_health('frontend')

    print("All services are now started! You can access the dashboard using http://localhost:3000.")

    print("(Tip: You can see your services using \"docker ps\" in a terminal)")
    print("")
    print("")
    print("")
    print("")