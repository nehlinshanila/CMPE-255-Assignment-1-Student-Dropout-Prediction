# Prompt Used

This is a reproducible **project-generation prompt**, not hidden reasoning or system instructions.

## Main prompt

> Act as a senior data scientist, ML engineer, and product-minded front-end developer. Build an end-to-end GitHub-ready project for Kaggle's **New York City Taxi Trip Duration** challenge using the CRISP-DM framework.
>
> Requirements:
>
> 1. **Business Understanding**
>    - Define the prediction objective and business value.
>    - Use Kaggle's official metric, RMSLE.
>    - State assumptions, risks, and deployment constraints.
>
> 2. **Data Understanding**
>    - Load `train.csv` and `test.csv`.
>    - Inspect shape, schema, descriptive statistics, duplicates, missing values, target skew, temporal patterns, coordinate ranges, and suspicious records.
>    - Identify potential data leakage.
>
> 3. **Data Preparation**
>    - Parse timestamps.
>    - Clean invalid training records appropriately.
>    - Engineer inference-safe temporal and geospatial features: month, weekday, hour, rush-hour, Haversine distance, Manhattan-style distance, bearing, route center, vendor/passenger fields, and store-forward encoding.
>    - Do not use `dropoff_datetime` as a predictor.
>
> 4. **Modeling**
>    - Train on `log1p(trip_duration)`.
>    - Compare a dummy baseline, Random Forest, HistGradientBoosting, and XGBoost.
>    - Evaluate with RMSLE.
>    - Cross-validate the strongest candidate and perform light hyperparameter tuning.
>    - Refit the selected model and save it with Joblib.
>
> 5. **Evaluation**
>    - Present a model comparison table.
>    - Compare cross-validation stability and tuned vs. untuned performance.
>    - Inspect residuals and feature importance.
>    - Generate Kaggle-format `submission.csv` with `id` and `trip_duration`.
>
> 6. **Deployment**
>    - Build a polished Streamlit UI using the exact same feature engineering code.
>    - Let users enter pickup/dropoff coordinates, pickup time, passenger count, vendor ID, and store-forward flag.
>    - Show route points and a human-readable trip-duration estimate.
>    - State clearly that this is historical ML, not live traffic routing.
>
> 7. **Repository**
>    - Create a polished README, requirements, reusable `src/` code, Dockerfile, images, CRISP-DM report, sample schema-compatible data, and a prompt log.
>    - Never commit the large Kaggle CSV files.
>    - Clearly label synthetic sample data and never present its score as Kaggle performance.

## Follow-up prompt after official-data execution

> Review the executed notebook as a skeptical senior data scientist. Compare holdout RMSLE, CV mean/std, tuned vs. untuned XGBoost, residual behavior, and feature importance. Update the README Results section using only measured results from the official Kaggle training data. Do not overclaim leaderboard performance.
