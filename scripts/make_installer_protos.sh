#!/bin/bash
set -e

INSTALLER_DIR=$2
PROTO_DIR=./Honeypot/protos
PROTO_OUTPUT_DIR=$INSTALLER_DIR/src/protos

cd $INSTALLER_DIR

# Create the protos output directory if it doesn't exist
mkdir -p $PROTO_OUTPUT_DIR

# Generate the Python gRPC code from the .proto files
python3 -m grpc_tools.protoc \
    -I${PROTO_DIR} \
    --python_out=${PROTO_OUTPUT_DIR} \
    --mypy_out=${PROTO_OUTPUT_DIR} \
    --grpc_python_out=${PROTO_OUTPUT_DIR} \
    --mypy_grpc_out=${PROTO_OUTPUT_DIR} \
    ${PROTO_DIR}/*.proto

# Create __init__.py file in the protos directory
echo "import sys" > $PROTO_OUTPUT_DIR/__init__.py
echo "import os" >> $PROTO_OUTPUT_DIR/__init__.py
echo "sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))" >> $PROTO_OUTPUT_DIR/__init__.py
