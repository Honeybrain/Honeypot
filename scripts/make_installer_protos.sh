#!/bin/bash
set -e

INSTALLER_DIR=$2
PROTO_DIR=../Honeypot/protos
PROTO_OUTPUT_DIR=$INSTALLER_DIR/src/protos

cd $INSTALLER_DIR

mkdir -p $PROTO_OUTPUT_DIR

python3 -m grpc_tools.protoc \
	-I${PROTO_DIR} \
	--python_out=${PROTO_OUTPUT_DIR} \
	--mypy_out=${PROTO_OUTPUT_DIR} \
	--grpc_python_out=${PROTO_OUTPUT_DIR} \
	--mypy_grpc_out=${PROTO_OUTPUT_DIR} \
	${PROTO_DIR}/*.proto
