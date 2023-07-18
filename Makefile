BACKEND_DIR = ../Backend
PROTO_DIR = proto
PROTO_OUTPUT_DIR = proto/js
DOCKER_COMPOSE_FILE = docker-compose-dev.yml

.PHONY: grpc backend-grpc run check-setup build stop logs

check-setup:
	@echo "🚀 Checking setup..."
	@bash scripts/check-setup.sh $(BACKEND_DIR)
	@echo "✅ Setup is okay!"

grpc: backend-grpc

backend-grpc:
	@echo "🚀 Generating Backend Protobuf files ..."
	@bash scripts/make_backend_protos.sh $(PROTO_DIR) $(PROTO_OUTPUT_DIR) $(BACKEND_DIR)
	@echo "✅ Backend Protobuf files generated successfully!"

run:
	@echo "🚀 Starting Docker services in detached mode..."
	docker compose -f $(DOCKER_COMPOSE_FILE) up -d
	@echo "✅ Docker services started successfully!"

build: check-setup grpc
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
