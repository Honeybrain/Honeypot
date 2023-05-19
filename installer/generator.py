from jinja2 import Environment, FileSystemLoader
import json
import shutil
import glob
import os
import subprocess

def generate(config_file_path):
    print('Parsing config...')

    # Open the config file
    with open(config_file_path, 'r') as f:
        config = json.load(f)

    # Parameters
    num_dummy_pc = config['dummy_pc']['num_services']
    ip_addresses_dummy_pc = config['dummy_pc']['ip_addresses']
    ftp_port = config['ftp']['port']
    ftp_ip_address = config['ftp']['ip_address']
    subnet = config['subnet']

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
        subnet=subnet
    )

    print('Copying honeypot modules...')

    # Copy docker files
    shutil.copytree('./modules', './build/modules', dirs_exist_ok=True)

    print('Copying honeypot core services...')

    # Copy docker files
    source_path = '../*'
    destination_path = './build/honeypot'
    for file_or_dir in glob.glob(source_path):
        if os.path.isdir(file_or_dir) and os.path.basename(file_or_dir) == 'installer':
            continue  # Exclure le dossier "installer"
        if os.path.isfile(file_or_dir):
            shutil.copy2(file_or_dir, destination_path)
        elif os.path.isdir(file_or_dir):
            shutil.copytree(file_or_dir, os.path.join(destination_path, os.path.basename(file_or_dir)), dirs_exist_ok=True)

    # Write the output to a file
    with open('build/docker-compose.yml', 'w') as f:
        f.write(output)

    print("[OK] Docker Compose file has been created.")

    print("Starting honeypot services...")

    subprocess.run(['docker', 'compose', 'up', '-d'], cwd='build')
    
    print("[OK] Docker services started.")

    # exit()