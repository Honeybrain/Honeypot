#!/bin/bash
set -e

FRONTEND_DIR=$2
PROTO_DIR=../Honeypot/protos
PROTO_OUTPUT_DIR=$FRONTEND_DIR/src/protos

PROTOC_GEN_GRPC_WEB_PATH=node_modules/.bin/protoc-gen-grpc-web

cd $FRONTEND_DIR

mkdir -p $PROTO_OUTPUT_DIR

yarn grpc_tools_node_protoc --ts_out $PROTO_OUTPUT_DIR -I $PROTO_DIR $PROTO_DIR/*.proto --experimental_allow_proto3_optional
