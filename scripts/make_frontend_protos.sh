#!/bin/bash
set -e

FRONTEND_DIR=$2
PROTO_DIR=../Honeypot/$1
PROTO_OUTPUT_DIR=$FRONTEND_DIR/src/protos

cd $FRONTEND_DIR

mkdir -p $PROTO_OUTPUT_DIR

yarn grpc_tools_node_protoc \
    -I=$PROTO_DIR \
    --ts_out=service=grpc-node,mode=grpc-js:$PROTO_OUTPUT_DIR \
    $PROTO_DIR/*.proto