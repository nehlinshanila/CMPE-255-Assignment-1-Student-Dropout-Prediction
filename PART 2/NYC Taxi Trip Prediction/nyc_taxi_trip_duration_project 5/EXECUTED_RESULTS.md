# Executed Real-Data Results

This project was actually executed on a small **real NYC Taxi Trip Duration competition-schema sample** retrieved from a public educational mirror of the Kaggle training data.

## Data used

- Rows: **50**
- Columns: **11**
- Date range: **2016-01-02 01:16:42 → 2016-06-28 13:57:15**
- Target: `trip_duration`
- Leakage field excluded from predictors: `dropoff_datetime`

## Holdout results

| Model                |   Holdout RMSLE |
|:---------------------|----------------:|
| Random Forest        |          0.5519 |
| XGBoost              |          0.7557 |
| HistGradientBoosting |          0.8352 |
| Dummy Median         |          0.8848 |

## Cross-validation of best smoke-test model

- Best model: **Random Forest**
- 5-fold mean log-RMSE: **0.5055**
- 5-fold standard deviation: **0.0287**

## Interpretation

The Random Forest clearly beats the naive median baseline on this real-data slice. However, this is intentionally labeled a **smoke test**, because a 50-row sample is much too small to estimate final Kaggle performance reliably.

The full repository remains designed for the official Kaggle `train.csv` (~1.46M rows). When that file is available locally, the notebook will run the same feature-engineering and model-comparison pipeline on the full competition data.

## Provenance

Public raw CSV source:
`https://raw.githubusercontent.com/guebin/DV2023/main/posts/NYCTaxi.csv`

That source uses the same competition columns and contains real 2016 NYC taxi rows.
