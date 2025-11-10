# src/design_aesthetics.py
from pathlib import Path
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.cluster import KMeans
import colorsys
import os

def extract_palette_features(image_path: Path, k=5, sample_pixels=5000):
    def _to_hex(rgb_tuple):
        r, g, b = [int(max(0, min(255, v))) for v in rgb_tuple]
        return f"#{r:02X}{g:02X}{b:02X}"

    def _rgb_to_hsv01(rgb):
        r, g, b = [v/255.0 for v in rgb]
        return colorsys.rgb_to_hsv(r, g, b)

    def _warm_ratio(hues01):
        hues01 = np.asarray(hues01)
        return np.mean((hues01 >= 11/12) | (hues01 < 1/6))

    try:
        with Image.open(image_path) as im:
            im = im.convert("RGB")
            if max(im.size) > 1080:
                im.thumbnail((1080,1080))
            arr = np.array(im).reshape(-1, 3)
    except Exception:
        return None

    if arr.shape[0] > sample_pixels:
        idx = np.random.default_rng(42).choice(arr.shape[0], size=sample_pixels, replace=False)
        arr_sample = arr[idx]
    else:
        arr_sample = arr

    k = min(k, max(1, arr_sample.shape[0]))
    km = KMeans(n_clusters=k, n_init="auto", random_state=42)
    labels = km.fit_predict(arr_sample)
    centers = km.cluster_centers_
    counts = np.bincount(labels, minlength=k)
    order = np.argsort(counts)[::-1]
    centers, counts = centers[order], counts[order]
    pcts = counts / counts.sum()

    hexes = [_to_hex(c) for c in centers]
    hsv = np.apply_along_axis(lambda x: _rgb_to_hsv01(x), 1, arr_sample)
    h, s, v = hsv[:,0], hsv[:,1], hsv[:,2]
    stats = {
        "avg_hue01": float(np.mean(h)),
        "avg_saturation": float(np.mean(s)),
        "avg_value": float(np.mean(v)),
        "std_value": float(np.std(v)),
        "colorfulness": float(np.std(arr_sample, axis=0).mean()),
        "warm_ratio": float(_warm_ratio(h)),
    }
    top = 3
    hex_pad = (hexes + [None]*top)[:top]
    pct_pad = (pcts.tolist() + [0.0]*top)[:top]
    return {
        "dominant_hex_1": hex_pad[0],
        "dominant_hex_2": hex_pad[1],
        "dominant_hex_3": hex_pad[2],
        "dominant_pct_1": pct_pad[0],
        "dominant_pct_2": pct_pad[1],
        "dominant_pct_3": pct_pad[2],
        **stats
    }

def build_aesthetic_dataset(posts_model, image_folder: Path, output_path: Path):
    records, missing = [], []
    uris = posts_model["uri"].dropna().unique().tolist()

    for uri in uris:
        img_path = image_folder / uri
        if not img_path.exists():
            missing.append(uri)
            continue
        res = extract_palette_features(img_path)
        if res is None:
            missing.append(uri)
            continue
        res["uri"] = uri
        records.append(res)

    aesthetics_df = pd.DataFrame(records)
    merge_cols = ["uri","engagement","engagement_rate","log_engagement_rate","performance_label_log"]
    merge_cols = [c for c in merge_cols if c in posts_model.columns]
    if merge_cols:
        aesthetics_df = aesthetics_df.merge(posts_model[merge_cols], on="uri", how="left")

    aesthetics_df.to_csv(output_path, index=False)
    print(f"✅ Aesthetics data saved to: {output_path}")
    print(f"⚠️ Missing images: {len(missing)}")
    return aesthetics_df
