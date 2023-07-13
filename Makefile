PROTO_DIR = ../Backend/protos
PROTO_OUTPUT_DIR = ../Backend/protos/js
PROTOC_GEN_GRPC_PATH = protoc
PROTOC_GEN_JS_PATH = `which grpc_tools_node_protoc_plugin`
DOCKER_COMPOSE_FILE = docker-compose-dev.yml

.PHONY: proto
proto:
	@echo "🔧 Generating Protobuf files..."
	mkdir -p $(PROTO_OUTPUT_DIR)
	$(PROTOC_GEN_GRPC_PATH) \
		--js_out=import_style=commonjs,binary:$(PROTO_OUTPUT_DIR) \
		--grpc_out=grpc_js:$(PROTO_OUTPUT_DIR) \
		--plugin=protoc-gen-grpc=$(PROTOC_GEN_JS_PATH) \
		--proto_path=$(PROTO_DIR) \
		$(PROTO_DIR)/*.proto
	@echo "✅ Protobuf files generated successfully!"

.PHONY: run
run:
	@echo "🚀 Starting Docker services in detached mode..."
	docker compose -f $(DOCKER_COMPOSE_FILE) up -d
	@echo "🎉 Docker services started successfully!"

.PHONY: run-build
run-build:
	@echo "🚀 Starting Docker services with build..."
	docker compose -f $(DOCKER_COMPOSE_FILE) up --build
	@echo "🎉 Docker services started successfully!"

.PHONY: stop
stop:
	@echo "⏹️ Stopping Docker services..."
	docker compose -f $(DOCKER_COMPOSE_FILE) down
	@echo "🛑 Docker services stopped successfully!"

.PHONY: logs
logs:
	@echo "📜 Following Docker service logs..."
	docker compose -f $(DOCKER_COMPOSE_FILE) logs -f
