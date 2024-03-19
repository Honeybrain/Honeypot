import os
from jinja2 import Environment, FileSystemLoader
import json
import shutil
import subprocess
import time
from firebase import create_account


def wait_for_container_health(container_name, timeout=3600):
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            output = subprocess.check_output(["docker", "ps", "--format", "{{json .}}"])
            containers = [line for line in output.decode().split("\n") if line.strip()]

            for container in containers:
                container_info = json.loads(container)
                if container_info["Names"] == container_name:
                    status = container_info["Status"]
                    if "healthy" in status:
                        return

            time.sleep(1)

        except subprocess.CalledProcessError:
            pass

    raise TimeoutError(
        f"Timeout while waiting for container '{container_name}' to become healthy."
    )


def generate(config_file_path, username, password):
    try:
        print("[INFO] Parsing config...")
        # Open the config file
        with open(config_file_path, "r") as f:
            config = json.load(f)

        # Parameters
        num_dummy_pc = (
            config["dummy_pc"]["num_services"] if "dummy_pc" in config else None
        )
        ip_addresses_dummy_pc = (
            config["dummy_pc"]["ip_addresses"] if "dummy_pc" in config else None
        )
        ftp_port = config["ftp"]["port"] if "ftp" in config else None
        ftp_ip_address = config["ftp"]["ip_address"] if "ftp" in config else None
        subnet = config["subnet"]
        dockerfile = config["dockerfile"]

        # Load the template file
        file_loader = FileSystemLoader("templates")
        env = Environment(loader=file_loader)
        print("[ OK ] Config parsed.")
    except Exception as e:
        print("[ERROR] Could not parse config: " + e.__cause__)
        return

    try:
        print("[INFO] Generating docker compose...")
        # Load the main template
        template = env.get_template("docker-compose-template.yml")

        # Render the main template with the number of services and the IP addresses
        output = template.render(
            num_dummy_pc=num_dummy_pc,
            ip_addresses_dummy_pc=ip_addresses_dummy_pc,
            ftp_port=ftp_port,
            ftp_ip_address=ftp_ip_address,
            subnet=subnet,
            dockerfile=dockerfile,
        )

        template_ips = env.get_template("docker-compose-ips-template.yml")

        output_ips = template_ips.render()

        print("[ OK ] Docker compose generated.")
    except Exception as e:
        print("[ERROR] Could not generate docker compose: " + e.__cause__)
        return

    try:
        print("[INFO] Checking Honeypot...")
        honeypot_path = "../../Honeypot"

        if not os.path.exists(honeypot_path):
            print("[WARN] Honeypot folder does not exist!")
            print("[INFO] Cloning Honeypot...")
            subprocess.run(["git", "clone", "https://github.com/Honeybrain/Honeypot", honeypot_path])
            print("[ OK ] Honeypot cloned.")
        print("[ OK ] Honeypot exists.")

        print("[INFO] Copying files...")
        shutil.copytree(
            "../../Honeypot/config", "../build/honeypot/config", dirs_exist_ok=True
        )
        shutil.copytree(
            "../../Honeypot/logs", "../build/honeypot/logs", dirs_exist_ok=True
        )
        shutil.copy(
            "../../Honeypot/scripts/start_honeybrain.sh", "../build/start_honeybrain.sh",
        )
        shutil.copy(
            "../../Honeypot/config/fail2ban/fail2ban.env",
            "../build/honeypot/fail2ban.env",
        )

        # Write the output to a file
        with open("../build/docker-compose.yml", "w") as f:
            f.write(output)

        # Write the output to a file
        with open("../build/docker-compose-ips.yml", "w") as f:
            f.write(output_ips)

        print("[ OK ] Files copied.")
    except Exception as e:
        print("[ERROR] Could not copy honeybrain files: " + e.__cause__)
        return

    try:
        print("[INFO] Starting honeypot services...")
        subprocess.run(["chmod", "+x", "../build/start_honeybrain.sh"])
        subprocess.run(
            ["../build/start_honeybrain.sh", "../build/docker-compose.yml", "../build/docker-compose-ips.yml"],
            cwd=".",
        )
    except Exception as e:
        print("[ERROR] Could not start honeypot services: " + e.__cause__)
        return

    try:
        wait_for_container_health("backend")
        print("[ OK ] Docker services started.")
    except TimeoutError:
        print("[ERROR] Could not start backend.")
        return

    try:
        print("[INFO] Creating account...")
        create_account(username, password)
        print("[ OK ] Account created.")
    except Exception as e:
        print("[ERROR] Could not create user: " + e.__cause__)
        return

    try:
        wait_for_container_health("frontend")
    except TimeoutError:
        print("[ERROR] Could not start frontend.")
        return

    print(
        "All services are now started! You can access the dashboard using http://localhost:3000."
    )

    print('(Tip: You can see your services using "docker ps" in a terminal)')
    print("")
    print("")
    print("")
    print("")
