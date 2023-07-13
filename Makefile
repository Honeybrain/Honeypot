PROTO_DIR = ../Backend/protos
PROTO_OUTPUT_DIR = ../Backend/protos/js
DOCKER_COMPOSE_FILE = docker-compose-dev.yml

grpc: backend-grpc

backend-grpc:
	@echo "🔧 Generating Backend Protobuf files ..."
	@bash scripts/make_backend_protos.sh $(PROTO_DIR) $(PROTO_OUTPUT_DIR)
	@echo "✅ Backend Protobuf files generated successfully!"

run:
	@echo "🚀 Starting Docker services in detached mode..."
	@DOCKER_GROUP_ID=$(DOCKER_GROUP_ID) docker compose up -f $(DOCKER_COMPOSE_FILE) -d
	@echo "🎉 Docker services started successfully!"

build: grpc
	@echo "🚀 Starting Docker services with build..."
	docker compose -f $(DOCKER_COMPOSE_FILE) up --build
	@echo "🎉 Docker services started successfully!"

stop:
	@echo "⏹️ Stopping Docker services..."
	docker compose -f $(DOCKER_COMPOSE_FILE) down
	@echo "🛑 Docker services stopped successfully!"

logs:
	@echo "📜 Following Docker service logs..."
	docker compose -f $(DOCKER_COMPOSE_FILE) logs -f