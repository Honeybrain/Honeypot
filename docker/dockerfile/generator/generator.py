import os
import json
import subprocess
from jinja2 import Environment, FileSystemLoader

def main():
    try:
        print("[INFO] Parsing config...")
        # Open the config file
        with open("/config/config.json", "r") as f:
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
        file_loader = FileSystemLoader("/config")
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

        # Write the output to a file
        with open("/config/docker-compose.yml", "w") as f:
            f.write(output)

        # Write the output to a file
        with open("/config/docker-compose-ips.yml", "w") as f:
            f.write(output_ips)

        print("[ OK ] Files copied.")
    except Exception as e:
        print("[ERROR] Could not copy honeybrain files: " + e.__cause__)
        return

    print(
        "All services are now started! You can access the dashboard using http://localhost:3000."
    )

    print('(Tip: You can see your services using "docker ps" in a terminal)')
    print("")
    print("")
    print("")
    print("")

if __name__ == "__main__":
    main()
