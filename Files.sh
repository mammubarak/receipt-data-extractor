#!/bin/bash

mkdir -p data/original_receipts
mkdir -p data/preprocessed_images
mkdir -p data/processed_images
mkdir -p data/output
mkdir -p src

touch src/preprocessing.py
touch src/processing.py
touch src/ocr_summary.py
touch src/visualization.py
touch src/main.py
touch src/utils.py
touch README.md