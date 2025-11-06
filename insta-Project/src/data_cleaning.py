import json
import pandas as pd
from pathlib import Path
import gzip
import re
from datetime import datetime, timezone, timedelta 

def load_json_any(p: Path):
    """
    Loads a JSON or gzipped JSON file safely.
    Returns the raw parsed JSON object.
    """
    raw = None
    if p.suffix == ".gz":
        with gzip.open(p, "rb") as f:
            raw = f.read().decode("utf-8", "ignore")
    else:
        raw = p.read_text(encoding="utf-8", errors="ignore")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        raw_fixed = re.sub(r",\s*([}\]])", r"\1", raw)
        data = json.loads(raw_fixed)
    return data


def flatten_instagram_json(posts_file: Path) -> pd.DataFrame:
    """
    Converts nested Instagram JSON export into a flat tabular DataFrame.
    Does NOT perform any timestamp conversion or cleaning.
    Each media item becomes one row.
    """
    data = load_json_any(posts_file)

    flattened_rows = []
    for item in data:
        top_creation = item.get("creation_timestamp", None)
        top_title = item.get("title", "")
        media_list = item.get("media", [])

        for media in media_list:
            row = {}
            row.update(media)
            row["top_creation_timestamp"] = top_creation
            row["top_title"] = top_title
            flattened_rows.append(row)

    df = pd.DataFrame(flattened_rows)

    if "media_metadata" in df.columns:
        df["media_metadata.camera_metadata.has_camera_metadata"] = df["media_metadata"].apply(
            lambda x: x.get("camera_metadata", {}).get("has_camera_metadata") if isinstance(x, dict) else None
        )
        df = df.drop(columns=["media_metadata"])

    if "cross_post_source" in df.columns:
        df["cross_post_source.source_app"] = df["cross_post_source"].apply(
            lambda x: x.get("source_app") if isinstance(x, dict) else None
        )
        df = df.drop(columns=["cross_post_source"])

    return df

# Timezone: Asia/Jakarta (UTC+7)
TZ_OFFSET_HOURS = 7
LOCAL_TZ = timezone(timedelta(hours=TZ_OFFSET_HOURS))

def to_dt_safe(x):
    """
    Converts a numeric or string timestamp to datetime safely.
    Returns NaT for invalid or missing values.
    """
    if pd.isna(x) or x == "":
        return pd.NaT
    try:
        v = float(x)
        if v > 10_000_000_000:  # milliseconds
            v = v / 1000
        return pd.to_datetime(v, unit="s", utc=True).tz_convert(LOCAL_TZ)
    except Exception:
        return pd.NaT


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the flattened Instagram data:
    - Converts all timestamp columns to datetime
    - Fills missing text/numeric fields
    - Adds derived columns (like date, month, year)
    """
    df = df.copy()

    # Identify timestamp columns (contains 'timestamp')
    ts_cols = [c for c in df.columns if "timestamp" in c.lower()]
    for col in ts_cols:
        df[col] = df[col].apply(to_dt_safe)

    # Fill missing string and numeric values
    df = df.fillna({
        "title": "",
        "top_title": "",
        "uri": ""
    })

    # Optional: add derived columns
    if "creation_timestamp" in df.columns:
        df["creation_date"] = df["creation_timestamp"].dt.date
        df["creation_month"] = df["creation_timestamp"].dt.to_period("M")

    if "top_creation_timestamp" in df.columns:
        df["top_creation_date"] = df["top_creation_timestamp"].dt.date

    return df