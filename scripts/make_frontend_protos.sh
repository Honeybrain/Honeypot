#!/bin/bash
set -e

FRONTEND_DIR=$3
PROTO_DIR=../Honeypot/$1
PROTO_OUTPUT_DIR=$FRONTEND_DIR/src/$2

cd $FRONTEND_DIR

mkdir -p $PROTO_OUTPUT_DIR

yarn grpc_tools_node_protoc --proto_path=$PROTO_DIR --js_out=import_style=commonjs,binary:$PROTO_OUTPUT_DIR --grpc_out=grpc_js:$PROTO_OUTPUT_DIR $PROTO_DIR/*.proto
