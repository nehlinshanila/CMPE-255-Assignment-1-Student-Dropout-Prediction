# Data

The repository intentionally does **not** commit Kaggle's full competition CSV files.

## Official data

Place these files here:

- `train.csv`
- `test.csv`
- `sample_submission.csv`

After accepting the competition rules and configuring Kaggle API credentials:

```bash
kaggle competitions download -c nyc-taxi-trip-duration -p data
unzip data/nyc-taxi-trip-duration.zip -d data
```

The notebook automatically prefers the official files. If they are absent, it falls back to the included synthetic sample files.

## Included samples

`sample_train.csv` and `sample_test.csv` are **synthetic schema-compatible smoke-test data**. They exist only so the notebook and Streamlit UI can run immediately.

Do not report sample-model scores as Kaggle results.

## Real executed sample

`real_kaggle_schema_sample.csv` contains the real rows used for the executed smoke test in this repository.

Source:
`https://raw.githubusercontent.com/guebin/DV2023/main/posts/NYCTaxi.csv`

The included file is deliberately small enough for GitHub. It is not the complete Kaggle competition file.
