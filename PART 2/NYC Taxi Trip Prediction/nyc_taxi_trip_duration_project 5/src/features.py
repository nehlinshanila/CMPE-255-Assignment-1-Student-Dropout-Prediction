from __future__ import annotations
import numpy as np
import pandas as pd

EARTH_RADIUS_KM = 6371.0088

FEATURE_COLUMNS = [
    "vendor_id","passenger_count",
    "pickup_longitude","pickup_latitude",
    "dropoff_longitude","dropoff_latitude",
    "pickup_month","pickup_day","pickup_weekday","pickup_hour","pickup_minute",
    "pickup_weekofyear","is_weekend","is_rush_hour",
    "haversine_km","manhattan_km","bearing_deg",
    "center_latitude","center_longitude","store_and_fwd_flag_Y"
]

def haversine_distance_km(lat1, lon1, lat2, lon2):
    lat1 = np.radians(np.asarray(lat1, dtype=float))
    lat2 = np.radians(np.asarray(lat2, dtype=float))
    dlat = lat2 - lat1
    dlon = np.radians(np.asarray(lon2, dtype=float) - np.asarray(lon1, dtype=float))
    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    return 2 * EARTH_RADIUS_KM * np.arcsin(np.sqrt(np.clip(a, 0, 1)))

def manhattan_distance_km(lat1, lon1, lat2, lon2):
    vertical = haversine_distance_km(lat1, lon1, lat2, lon1)
    horizontal = haversine_distance_km(lat1, lon1, lat1, lon2)
    return vertical + horizontal

def bearing_degrees(lat1, lon1, lat2, lon2):
    lat1_r = np.radians(np.asarray(lat1, dtype=float))
    lat2_r = np.radians(np.asarray(lat2, dtype=float))
    dlon_r = np.radians(np.asarray(lon2, dtype=float) - np.asarray(lon1, dtype=float))
    y = np.sin(dlon_r) * np.cos(lat2_r)
    x = np.cos(lat1_r) * np.sin(lat2_r) - np.sin(lat1_r) * np.cos(lat2_r) * np.cos(dlon_r)
    return np.degrees(np.arctan2(y, x))

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    required = {
        "vendor_id","pickup_datetime","passenger_count",
        "pickup_longitude","pickup_latitude",
        "dropoff_longitude","dropoff_latitude","store_and_fwd_flag"
    }
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    out = pd.DataFrame(index=df.index)
    pickup_dt = pd.to_datetime(df["pickup_datetime"], errors="coerce")

    for col in [
        "vendor_id","passenger_count","pickup_longitude","pickup_latitude",
        "dropoff_longitude","dropoff_latitude"
    ]:
        out[col] = pd.to_numeric(df[col], errors="coerce")

    out["pickup_month"] = pickup_dt.dt.month
    out["pickup_day"] = pickup_dt.dt.day
    out["pickup_weekday"] = pickup_dt.dt.weekday
    out["pickup_hour"] = pickup_dt.dt.hour
    out["pickup_minute"] = pickup_dt.dt.minute
    out["pickup_weekofyear"] = pickup_dt.dt.isocalendar().week.astype(float)
    out["is_weekend"] = pickup_dt.dt.weekday.isin([5,6]).astype(int)
    out["is_rush_hour"] = (
        pickup_dt.dt.hour.between(7,9) | pickup_dt.dt.hour.between(16,19)
    ).astype(int)

    out["haversine_km"] = haversine_distance_km(
        out["pickup_latitude"], out["pickup_longitude"],
        out["dropoff_latitude"], out["dropoff_longitude"]
    )
    out["manhattan_km"] = manhattan_distance_km(
        out["pickup_latitude"], out["pickup_longitude"],
        out["dropoff_latitude"], out["dropoff_longitude"]
    )
    out["bearing_deg"] = bearing_degrees(
        out["pickup_latitude"], out["pickup_longitude"],
        out["dropoff_latitude"], out["dropoff_longitude"]
    )
    out["center_latitude"] = (out["pickup_latitude"] + out["dropoff_latitude"]) / 2
    out["center_longitude"] = (out["pickup_longitude"] + out["dropoff_longitude"]) / 2
    out["store_and_fwd_flag_Y"] = (
        df["store_and_fwd_flag"].fillna("N").astype(str).str.upper().eq("Y")
    ).astype(int)

    out = out[FEATURE_COLUMNS].replace([np.inf, -np.inf], np.nan)
    return out.fillna(out.median(numeric_only=True)).fillna(0.0)
