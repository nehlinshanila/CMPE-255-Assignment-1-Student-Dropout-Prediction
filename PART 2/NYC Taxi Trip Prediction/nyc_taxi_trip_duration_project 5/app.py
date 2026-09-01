from __future__ import annotations
from datetime import datetime, date, time
from pathlib import Path
import sys
import joblib
import numpy as np
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from src.features import build_features, haversine_distance_km
from src.modeling import seconds_to_human

MODEL_PATH = ROOT / "models" / "taxi_duration_model.joblib"

st.set_page_config(page_title="NYC Taxi ETA", page_icon="🚕", layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 2rem; padding-bottom: 3rem;}
[data-testid="stMetricValue"] {font-size: 2.2rem;}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_bundle():
    if not MODEL_PATH.exists():
        return None
    return joblib.load(MODEL_PATH)

bundle = load_bundle()

st.title("🚕 NYC Taxi ETA")
st.caption("End-to-end ML demo for the Kaggle NYC Taxi Trip Duration challenge")

if bundle is None:
    st.error("Model artifact not found. Run the notebook first.")
    st.stop()

meta = bundle.get("metadata", {})
if "synthetic" in meta.get("trained_on", "").lower():
    st.warning(
        "The included artifact is a demo model trained on synthetic schema-compatible data. "
        "Run the notebook with Kaggle train.csv to replace it with your competition-trained model."
    )

tab_predict, tab_model, tab_project = st.tabs(["Predict", "Model", "Project"])

with tab_predict:
    left, right = st.columns([1.15, .85], gap="large")

    with left:
        st.subheader("Trip details")
        preset = st.selectbox("Route preset", [
            "Custom",
            "Midtown Manhattan → JFK Airport",
            "Midtown Manhattan → LaGuardia Airport",
            "Lower Manhattan → Times Square",
        ])
        presets = {
            "Midtown Manhattan → JFK Airport": (40.7580,-73.9855,40.6413,-73.7781),
            "Midtown Manhattan → LaGuardia Airport": (40.7580,-73.9855,40.7769,-73.8740),
            "Lower Manhattan → Times Square": (40.7075,-74.0113,40.7580,-73.9855),
        }
        defaults = (40.7580,-73.9855,40.7306,-73.9352) if preset == "Custom" else presets[preset]

        c1, c2 = st.columns(2)
        with c1:
            pickup_lat = st.number_input("Pickup latitude", value=float(defaults[0]), format="%.6f")
            pickup_lon = st.number_input("Pickup longitude", value=float(defaults[1]), format="%.6f")
            passenger_count = st.slider("Passengers", 1, 6, 1)
            vendor_id = st.selectbox("Vendor ID", [1,2])
        with c2:
            dropoff_lat = st.number_input("Dropoff latitude", value=float(defaults[2]), format="%.6f")
            dropoff_lon = st.number_input("Dropoff longitude", value=float(defaults[3]), format="%.6f")
            pickup_date = st.date_input("Pickup date", value=date(2016,6,15))
            pickup_time = st.time_input("Pickup time", value=time(8,30))

        store_flag = st.selectbox("Store-and-forward flag", ["N","Y"])
        clicked = st.button("Predict trip duration", type="primary", use_container_width=True)

    with right:
        st.subheader("Route")
        st.map(pd.DataFrame({"lat":[pickup_lat,dropoff_lat],"lon":[pickup_lon,dropoff_lon]}),
               zoom=10, use_container_width=True)
        straight_km = float(haversine_distance_km(
            [pickup_lat],[pickup_lon],[dropoff_lat],[dropoff_lon]
        )[0])
        st.metric("Straight-line distance", f"{straight_km:.2f} km")
        st.caption("The model also computes Manhattan-style distance, bearing, route-center and time features.")

    if clicked:
        pickup_dt = datetime.combine(pickup_date, pickup_time)
        raw = pd.DataFrame([{
            "vendor_id": vendor_id,
            "pickup_datetime": pickup_dt.strftime("%Y-%m-%d %H:%M:%S"),
            "passenger_count": passenger_count,
            "pickup_longitude": pickup_lon,
            "pickup_latitude": pickup_lat,
            "dropoff_longitude": dropoff_lon,
            "dropoff_latitude": dropoff_lat,
            "store_and_fwd_flag": store_flag,
        }])
        X = build_features(raw)
        pred_seconds = max(float(np.expm1(bundle["model"].predict(X)[0])), 1.0)

        st.divider()
        a,b,c = st.columns(3)
        a.metric("Estimated duration", seconds_to_human(pred_seconds))
        b.metric("Estimated seconds", f"{pred_seconds:,.0f}")
        c.metric("Engineered features", X.shape[1])
        st.info("Historical ML estimate only — not live traffic guidance.")

with tab_model:
    st.subheader("Model artifact")
    st.write({
        "Model": meta.get("model_name","Unknown"),
        "Validation RMSLE": meta.get("validation_rmsle"),
        "Training source": meta.get("trained_on","Unknown"),
        "Target transform": meta.get("target_transform","log1p")
    })
    st.markdown("""
**Why log-transform the target?**  
Kaggle uses RMSLE, so the training notebook models `log1p(trip_duration)`.

**Leakage protection:** `dropoff_datetime` is never used for inference.
""")

with tab_project:
    st.subheader("CRISP-DM implementation")
    st.markdown("""
1. **Business Understanding** — define ETA prediction objective and success metric.
2. **Data Understanding** — inspect quality, skew, coordinate and time distributions.
3. **Data Preparation** — clean training data and engineer inference-safe features.
4. **Modeling** — compare baseline, Random Forest, HistGradientBoosting and XGBoost.
5. **Evaluation** — RMSLE, cross-validation, tuning, residuals and importance.
6. **Deployment** — Joblib artifact + this Streamlit UI.
""")
