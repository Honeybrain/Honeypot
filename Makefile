BACKEND_DIR = ../Backend
FRONTEND_DIR = ../Frontend
INSTALLER_DIR = ../Installer

PROTO_DIR = protos
DOCKER_COMPOSE_FILE = ./docker/compose/docker-compose.yml
DOCKER_COMPOSE_IPS_FILE = ./docker/compose/docker-compose-ips.yml
ROOT = .

.PHONY: grpc backend-grpc frontend-grpc installer-grpc run check-setup build stop logs

check-setup:
	@echo "🚀 Checking setup..."
	@bash scripts/check-setup.sh $(BACKEND_DIR) $(FRONTEND_DIR) $(INSTALLER_DIR)
	@echo "✅ Setup is okay!"

grpc: check-setup backend-grpc frontend-grpc installer-grpc

backend-grpc:
	@echo "🚀 Generating backend protobuf files ..."
	@bash scripts/make_backend_protos.sh $(PROTO_DIR) $(BACKEND_DIR)
	@echo "✅ Protobuf backend files generated successfully!"

frontend-grpc:
	@echo "🚀 Generating frontend protobuf files ..."
	@bash scripts/make_frontend_protos.sh $(PROTO_DIR) $(FRONTEND_DIR)
	@echo "✅ Protobuf frontend files generated successfully!"

installer-grpc:
	@echo "🚀 Generating installer protobuf files ..."
	@bash scripts/make_installer_protos.sh $(PROTO_DIR) $(INSTALLER_DIR)
	@echo "✅ Protobuf installer files generated successfully!"

run:
	@echo "🚀 Starting Docker services in detached mode..."
	@bash scripts/start_honeybrain.sh $(ROOT) $(DOCKER_COMPOSE_FILE) $(DOCKER_COMPOSE_IPS_FILE)
	@echo "✅ Docker services started successfully!"

build: grpc
	@echo "🚀 Starting Docker services with build..."
	docker compose -f $(DOCKER_COMPOSE_FILE) build
	@echo "✅ Docker images built successfully!"

stop:
	@echo "🚀 Stopping Docker services..."
	docker compose -f $(DOCKER_COMPOSE_FILE) down
	@echo "✅ Docker services stopped successfully!"

logs:
	@echo "📜 Following Docker service logs..."
	docker compose -f $(DOCKER_COMPOSE_FILE) logs -f
