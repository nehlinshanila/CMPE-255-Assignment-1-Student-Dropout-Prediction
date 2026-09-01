from __future__ import annotations
import numpy as np
from sklearn.metrics import mean_squared_log_error

def rmsle(y_true, y_pred) -> float:
    y_true = np.clip(np.asarray(y_true, dtype=float), 0, None)
    y_pred = np.clip(np.asarray(y_pred, dtype=float), 0, None)
    return float(np.sqrt(mean_squared_log_error(y_true, y_pred)))

def seconds_to_human(seconds: float) -> str:
    seconds = max(float(seconds), 0)
    minutes = seconds / 60
    if minutes < 60:
        return f"{minutes:.1f} min"
    hours = int(minutes // 60)
    rem = int(round(minutes % 60))
    return f"{hours} h {rem} min"
