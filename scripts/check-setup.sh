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
    echo "❌ Error: tkinter is not installed for python3."
    exit 1
fi
echo "✅ tkinter is installed."