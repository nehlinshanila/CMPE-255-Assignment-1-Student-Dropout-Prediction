# CRISP-DM Project Report — NYC Taxi Trip Duration

## 1. Business Understanding

**Objective:** predict total NYC taxi trip duration using information available at or near pickup time.

**Business value:** ETA communication, passenger planning, dispatch support, fleet analysis, and service monitoring.

**Success criterion:** Kaggle evaluates with **Root Mean Squared Logarithmic Error (RMSLE)**; lower is better.

**Constraint:** `dropoff_datetime` is future information and is excluded to prevent leakage.

---

## 2. Data Understanding

The project inspects:

- shape and schema
- missing values and duplicates
- target skew
- passenger counts
- temporal coverage
- pickup/dropoff coordinate ranges
- suspicious or extreme duration values

The target is right-skewed, motivating log-space modeling.

---

## 3. Data Preparation

Training-only cleaning removes clearly unusable records such as non-positive/extreme durations, impossible passenger counts, and coordinates far outside a broad NYC region.

### Engineered features

**Temporal**
- month
- day
- weekday
- hour
- minute
- ISO week
- weekend flag
- rush-hour flag

**Geospatial**
- Haversine distance
- Manhattan-style distance
- bearing
- route-center latitude/longitude

**Other**
- vendor ID
- passenger count
- store-and-forward flag

`dropoff_datetime` is never a predictor.

---

## 4. Modeling

Models compared:

1. Dummy median baseline
2. Random Forest
3. HistGradientBoosting
4. XGBoost

The target is trained as `log1p(trip_duration)` and transformed back with `expm1`.

The notebook includes:
- holdout evaluation
- model comparison
- 3-fold cross-validation
- light XGBoost tuning
- final refit
- Joblib serialization

---

## 5. Evaluation

Primary metric: **RMSLE**.

Diagnostics include:
- holdout score table
- CV mean and standard deviation
- tuned vs. original comparison
- residual distribution
- feature importance

A complex model is accepted only when it meaningfully beats the naive baseline and remains stable across validation.

---

## 6. Deployment

The final model is saved with Joblib and served through a Streamlit web app.

The UI accepts:
- pickup/dropoff coordinates
- pickup date/time
- passenger count
- vendor ID
- store-and-forward flag

It returns a human-readable duration prediction and plots route points.

### Limitations

- 2016 historical data is not live traffic.
- Distance features approximate road travel.
- Geographic and temporal drift can reduce accuracy.
- Production use should add monitoring, validation, retraining, and prediction intervals.

### Recommended improvements

- road-network / OSRM route features
- holiday/weather features when rules permit
- geohash or spatial clustering
- time-aware validation
- stronger tuning
- SHAP explanations
- drift monitoring and scheduled retraining
