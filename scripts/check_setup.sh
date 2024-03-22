#!/bin/bash

BACKEND_DIR=$1
FRONTEND_DIR=$2
INSTALLER_DIR=$3

# Check if the Backend directory exists
if [ ! -d "$BACKEND_DIR" ]; then
  echo "❌ Error: Directory $BACKEND_DIR does not exist."
  exit 1
fi
echo "✅ Backend directory exists."

# Check if the Frontend directory exists
if [ ! -d "$FRONTEND_DIR" ]; then
  echo "❌ Error: Directory $FRONTEND_DIR does not exist."
  exit 1
fi
echo "✅ Frontend directory exists."

# Check if the Installer directory exists
if [ ! -d "$INSTALLER_DIR" ]; then
  echo "❌ Error: Directory $INSTALLER_DIR does not exist."
  exit 1
fi
echo "✅ Installer directory exists."

# Check if yarn is installed
if ! command -v yarn &> /dev/null; then
  echo "❌ Error: yarn is not installed."
  exit 1
fi
echo "✅ yarn is installed."

# Check if python or python3 is installed
if ! command -v python3 &> /dev/null; then
  echo "❌ Error: python3 is not installed."
  exit 1
fi
echo "✅ python is installed."

# Check if tkinter is installed for python3
if ! python3 -c "import tkinter" &> /dev/null; then
    echo "❌ Error: tkinter is not installed for python3. Please install package using 'apt-get install python3-tk'."
    exit 1
fi
echo "✅ tkinter is installed."

## Check if grpcio is installed
#if ! python3 -c "import grpc" &> /dev/null; then
#    echo "❌ Error: grpc is not installed for python3. Please install 'grpcio-tools' and 'grpcio' pip3 packages."
#    exit 1
#fi
#echo "✅ grpc is installed."

# Check for protoc-gen-mypy plugin
#if ! command -v protoc-gen-mypy &> /dev/null; then
#    echo "❌ Error: protoc-gen-mypy is not installed or not in PATH. Please install 'mypy-protobuf' pip3 package and add the executable to PATH."
#    exit 1
#fi
#echo "✅ protoc-gen-mypy plugin is available."

# Check if netifaces is installed
if ! python3 -c "import netifaces" &> /dev/null; then
    echo "❌ Error: netifaces is not installed for python3. Please install 'netifaces' pip3 package."
    exit 1
fi
echo "✅ netifaces is installed."

# Check if jinja2 is installed
if ! python3 -c "import jinja2" &> /dev/null; then
    echo "❌ Error: jinja2 is not installed for python3. Please install 'jinja2' pip3 package."
    exit 1
fi
echo "✅ jinja2 is installed."
