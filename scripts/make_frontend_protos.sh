#!/bin/bash
set -e

FRONTEND_DIR=$1
PROTO_DIR=../Honeypot/protos
PROTO_OUTPUT_DIR=./src/protos

cd $FRONTEND_DIR

mkdir -p $PROTO_OUTPUT_DIR

yarn install

yarn grpc_tools_node_protoc --ts_out $PROTO_OUTPUT_DIR -I $PROTO_DIR $PROTO_DIR/*.proto --experimental_allow_proto3_optional
