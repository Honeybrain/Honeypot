#!/bin/bash
set -e

PROTO_DIR=$1
PROTO_OUTPUT_DIR=$2

mkdir -p $PROTO_OUTPUT_DIR
protoc \
  --js_out=import_style=commonjs,binary:$PROTO_OUTPUT_DIR \
  --grpc_out=$PROTO_OUTPUT_DIR \
  --plugin=protoc-gen-grpc=`which grpc_tools_node_protoc_plugin` \
  --proto_path=$PROTO_DIR \
  $PROTO_DIR/*.proto
