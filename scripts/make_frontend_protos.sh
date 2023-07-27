#!/bin/bash
set -e

FRONTEND_DIR=$2
PROTO_DIR=../Honeypot/protos
PROTO_OUTPUT_DIR=$FRONTEND_DIR/src/protos

PROTOC_GEN_TS_PATH=node_modules/.bin/protoc-gen-ts
PROTOC_GEN_GRPC_PATH=node_modules/.bin/grpc_tools_node_protoc_plugin

cd $FRONTEND_DIR

mkdir -p $PROTO_OUTPUT_DIR

yarn grpc_tools_node_protoc \
    -I=$PROTO_DIR \
    --plugin=protoc-gen-ts=$PROTOC_GEN_TS_PATH \
    --plugin=protoc-gen-grpc=${PROTOC_GEN_GRPC_PATH} \
    --ts_out=grpc_js:$PROTO_OUTPUT_DIR \
    "$PROTO_DIR"/*.proto
