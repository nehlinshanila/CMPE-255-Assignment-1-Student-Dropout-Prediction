#!/usr/bin/env bash
set -e
mkdir -p data
if ! command -v kaggle >/dev/null 2>&1; then
  echo "Install Kaggle CLI first: pip install kaggle"
  exit 1
fi
echo "You must have accepted the competition rules and configured Kaggle credentials."
kaggle competitions download -c nyc-taxi-trip-duration -p data
unzip -o data/nyc-taxi-trip-duration.zip -d data
echo "Data downloaded to data/."
