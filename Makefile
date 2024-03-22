BACKEND_DIR = ./Backend
FRONTEND_DIR = ./Frontend
INSTALLER_DIR = ./Installer

PROTO_DIR = protos
DOCKER_COMPOSE_FILE = ./Honeypot/docker/compose/docker-compose.yml
DOCKER_COMPOSE_PROD_FILE = ./Honeypot/docker/compose/docker-compose-prod.yml
DOCKER_COMPOSE_IPS_FILE = ./Honeypot/docker/compose/docker-compose-ips.yml
ROOT = .

.PHONY: grpc \
		frontend-grpc \
		installer-grpc \
		run check-setup \
		build \
		stop \
		logs \
		run-production \
		stop-production \
		build-production

check-setup:
	@echo "🚀 Checking setup..."
	@bash scripts/check_setup.sh $(BACKEND_DIR) $(FRONTEND_DIR) $(INSTALLER_DIR)
	@echo "✅ Setup is okay!"

grpc: check-setup frontend-grpc #installer-grpc

backend-grpc:
	@echo "🚀 Generating backend protobuf files ..."
	@bash scripts/make_backend_protos.sh $(PROTO_DIR) $(BACKEND_DIR)
	@echo "✅ Protobuf backend files generated successfully!"

frontend-grpc:
	@echo "🚀 Generating frontend protobuf files ..."
	@bash scripts/make_frontend_protos.sh $(FRONTEND_DIR)
	@echo "✅ Protobuf frontend files generated successfully!"

installer-grpc:
	@echo "🚀 Generating installer protobuf files ..."
	@bash scripts/make_installer_protos.sh $(PROTO_DIR) $(INSTALLER_DIR)
	@echo "✅ Protobuf installer files generated successfully!"

run:
	@echo "🚀 Starting Docker services in detached mode..."
	@bash scripts/start_honeybrain.sh $(DOCKER_COMPOSE_FILE) $(DOCKER_COMPOSE_IPS_FILE)
	@echo "✅ Docker services started successfully!"

run-production:
	@echo "🚀 Starting Docker services in production mode..."
	@bash scripts/start_honeybrain.sh $(DOCKER_COMPOSE_PROD_FILE) $(DOCKER_COMPOSE_IPS_FILE)
	@echo "✅ Docker services started successfully!"

stop-production:
	@echo "🚀 Stopping Docker services in production mode..."
	@bash scripts/stop_honeybrain.sh $(DOCKER_COMPOSE_PROD_FILE) $(DOCKER_COMPOSE_IPS_FILE)
	@echo "✅ Docker services stopped successfully!"

build-production: grpc
	@echo "🚀 Starting Docker services with build in production mode..."
	@bash scripts/build_honeybrain.sh $(DOCKER_COMPOSE_PROD_FILE) $(DOCKER_COMPOSE_IPS_FILE)
	@echo "✅ Docker images built successfully!"

build: grpc
	@echo "🚀 Starting Docker services with build..."
	@bash scripts/build_honeybrain.sh $(DOCKER_COMPOSE_FILE) $(DOCKER_COMPOSE_IPS_FILE)
	@echo "✅ Docker images built successfully!"

stop:
	@echo "🚀 Stopping Docker services..."
	@bash scripts/stop_honeybrain.sh $(DOCKER_COMPOSE_FILE) $(DOCKER_COMPOSE_IPS_FILE)
	@echo "✅ Docker services stopped successfully!"
