#!/bin/bash

BACKEND_DIR=$1
FRONTEND_DIR=$2

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

# Check if npx is installed
if ! command -v npx &> /dev/null; then
  echo "❌ Error: npx is not installed."
  exit 1
fi
echo "✅ npx is installed."
