#!/usr/bin/env bash

# Script to download T3DB (Toxin and Toxin-Target Database) files
# Source: https://www.t3db.ca/downloads
# License: Free for academic use, commercial use requires permission

set -euo pipefail

localpath=$(pwd)
downloadpath="$localpath/download"

mkdir -p "$downloadpath"

echo "Downloading T3DB data files..."

BASE_URL="https://www.t3db.ca/system/downloads/current"

# Download CSV files (main data)
echo "Downloading toxins CSV..."
wget --no-check-certificate -q -nc -O "$downloadpath/toxins.csv.zip" "$BASE_URL/toxins.csv.zip" || true

echo "Downloading targets CSV..."
wget --no-check-certificate -q -nc -O "$downloadpath/targets.csv.zip" "$BASE_URL/targets.csv.zip" || true

echo "Downloading mechanisms of action CSV..."
wget --no-check-certificate -q -nc -O "$downloadpath/moas.csv.zip" "$BASE_URL/moas.csv.zip" || true

# Download SDF structures
echo "Downloading toxin structures (SDF)..."
wget --no-check-certificate -q -nc -O "$downloadpath/structures.zip" "$BASE_URL/structures.zip" || true

# Download FASTA sequences
echo "Downloading protein sequences..."
wget --no-check-certificate -q -nc -O "$downloadpath/target_protein_sequences.fasta.zip" \
    "$BASE_URL/sequences/protein/target_protein_sequences.fasta.zip" || true

echo "Downloading gene sequences..."
wget --no-check-certificate -q -nc -O "$downloadpath/target_gene_sequences.fasta.zip" \
    "$BASE_URL/sequences/gene/target_gene_sequences.fasta.zip" || true

echo "Download complete."
ls -la "$downloadpath"
