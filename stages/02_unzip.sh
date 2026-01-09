#!/usr/bin/env bash

# Script to extract T3DB zip files

set -euo pipefail

localpath=$(pwd)
downloadpath="$localpath/download"
rawpath="$localpath/raw"

mkdir -p "$rawpath"

echo "Extracting T3DB files..."

# Extract all zip files
for zipfile in "$downloadpath"/*.zip; do
    if [[ -f "$zipfile" ]]; then
        echo "Extracting $(basename "$zipfile")..."
        unzip -o -q "$zipfile" -d "$rawpath"
    fi
done

echo "Extraction complete."
find "$rawpath" -type f | head -20
