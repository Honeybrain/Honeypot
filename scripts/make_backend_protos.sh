#!/bin/bash
set -e

BACKEND_DIR=$3
PROTO_DIR=$BACKEND_DIR/$1
PROTO_OUTPUT_DIR=$BACKEND_DIR/$2

cd $BACKEND_DIR

mkdir -p $PROTO_OUTPUT_DIR

yarn grpc_tools_node_protoc --proto_path=$PROTO_DIR --js_out=import_style=commonjs,binary:$PROTO_OUTPUT_DIR --grpc_out=grpc_js:$PROTO_OUTPUT_DIR $PROTO_DIR/logs.proto
