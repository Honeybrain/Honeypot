#!/bin/bash
set -e

BACKEND_DIR=$2
PROTO_DIR=./Honeypot/protos
PROTO_OUTPUT_DIR=$BACKEND_DIR/src/protos

cd $BACKEND_DIR

mkdir -p $PROTO_OUTPUT_DIR

yarn install

yarn grpc_tools_node_protoc --proto_path=$PROTO_DIR \
    --js_out=import_style=commonjs,binary:$PROTO_OUTPUT_DIR \
    --grpc_out=grpc_js:$PROTO_OUTPUT_DIR \
    $PROTO_DIR/*.proto
