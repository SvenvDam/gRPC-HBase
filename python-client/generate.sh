#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
GENERATED_DIR=$SCRIPT_DIR/src
pyenv activate gRPC-hbase

python -m grpc_tools.protoc \
  -I"$SCRIPT_DIR"/../proto \
  --python_out="$GENERATED_DIR" \
  --grpc_python_out="$GENERATED_DIR" \
  "$SCRIPT_DIR"/../proto/hbase.proto
