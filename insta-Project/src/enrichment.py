from pathlib import Path
import pandas as pd
import json, gzip, re

# --------------------------------------------------
# Internal helpers
# --------------------------------------------------

def _load_json_any(p: Path):
    """Safely load JSON or gzipped JSON."""
    if p.suffix == ".gz":
        with gzip.open(p, "rb") as f:
            raw = f.read().decode("utf-8", "ignore")
    else:
        raw = p.read_text(encoding="utf-8", errors="ignore")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        raw_fixed = re.sub(r",\s*([}\]])", r"\1", raw)
        return json.loads(raw_fixed)

def _coerce_list(raw):
    """Force the raw object into a list of entries."""
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        # single entry?
        if ("string_map_data" in raw) or ("media_map_data" in raw):
            return [raw]
        # dict containing a list somewhere
        list_keys = [k for k, v in raw.items() if isinstance(v, list)]
        if list_keys:
            key = max(list_keys, key=lambda k: len(raw[k]))
            return raw[key]
    return []

def _first_media_dict(media_map_data):
    """Extract the first dict from media_map_data regardless of its key."""
    if not isinstance(media_map_data, dict):
        return {}
    for _k, v in media_map_data.items():
        if isinstance(v, dict):
            return v
    return {}

def _parse_intish(x):
    """Convert comma/str numbers to int."""
    if x is None:
        return 0
    if isinstance(x, (int, float)):
        return int(x)
    if isinstance(x, str):
        x = x.replace(",", "").strip()
        try:
            return int(float(x))
        except ValueError:
            return 0
    return 0

# --------------------------------------------------
# Main function
# --------------------------------------------------

def load_insights_posts(target: Path) -> pd.DataFrame:
    """
    Load post-level insights (likes, comments, reach, etc.) from Instagram's posts.json.
    Works when you pass either the ROOT folder of the export or the file itself.

    Returns tidy columns:
    ['uri','creation_timestamp','title','likes','comments','reach','impressions',
     'saves','shares','profile_visits','follows']
    """
    p = None
    if target.is_dir():
        cands = list(target.rglob("logged_information/past_instagram_insights/posts.json"))
        if not cands:
            cands = list(target.rglob("**/posts.json"))
        p = cands[0] if cands else None
    else:
        p = target

    if not p or not p.exists():
        print("posts.json not found under the provided target.")
        return pd.DataFrame()

    raw = _load_json_any(p)
    entries = _coerce_list(raw)

    if not entries:
        print("Could not coerce posts.json into a list. Top-level keys:",
              list(raw.keys()) if isinstance(raw, dict) else type(raw).__name__)
        return pd.DataFrame()

    rows = []
    for entry in entries:
        row = {}

        media = _first_media_dict(entry.get("media_map_data", {}))
        row["uri"] = media.get("uri")
        row["creation_timestamp"] = media.get("creation_timestamp")
        row["title"] = media.get("title")

        sdata = entry.get("string_map_data", {})
        if isinstance(sdata, dict):
            for k, v in sdata.items():
                if not isinstance(v, dict):
                    continue
                val = _parse_intish(v.get("value"))
                row[k] = val

        rows.append(row)

    df = pd.DataFrame(rows)

    rename_map = {
        "Likes": "likes",
        "Comments": "comments",
        "Saves": "saves",
        "Shares": "shares",
        "Accounts reached": "reach",
        "Impressions": "impressions",
        "Profile visits": "profile_visits",
        "Follows": "follows",
    }
    df = df.rename(columns=rename_map)

    for col in ["likes","comments","reach","impressions","saves","shares","profile_visits","follows"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
        else:
            df[col] = 0

    keep = ["uri","creation_timestamp","title","likes","comments","reach",
            "impressions","saves","shares","profile_visits","follows"]
    return df[keep]

def load_reels_insights(target: Path) -> pd.DataFrame:
    """
    Load reel-level insights (likes, comments, reach, etc.) from Instagram's reels.json.
    Works when you pass either the ROOT folder of the export or the file itself.

    Returns tidy columns:
    ['uri', 'creation_timestamp', 'title', 'likes', 'comments', 'reach', 'impressions', 'saves', 'shares']
    """
    p = None
    if target.is_dir():
        cands = list(target.rglob("your_instagram_activity/media/reels.json"))
        p = cands[0] if cands else None
    else:
        p = target

    if not p or not p.exists():
        print("reels.json not found under the provided target.")
        return pd.DataFrame()

    raw = _load_json_any(p)
    entries = _coerce_list(raw)

    if not entries:
        print("Could not coerce reels.json into a list. Top-level keys:",
              list(raw.keys()) if isinstance(raw, dict) else type(raw).__name__)
        return pd.DataFrame()

    rows = []
    for entry in entries:
        row = {}

        media = _first_media_dict(entry.get("media", {}))
        row["uri"] = media.get("uri")
        row["creation_timestamp"] = media.get("creation_timestamp")
        row["title"] = media.get("title")

        sdata = entry.get("string_map_data", {})
        if isinstance(sdata, dict):
            for k, v in sdata.items():
                if not isinstance(v, dict):
                    continue
                val = _parse_intish(v.get("value"))
                row[k] = val

        rows.append(row)

    df = pd.DataFrame(rows)

    rename_map = {
        "Likes": "likes",
        "Comments": "comments",
        "Saves": "saves",
        "Shares": "shares",
        "Accounts reached": "reach",
        "Impressions": "impressions",
        "Profile visits": "profile_visits",
        "Follows": "follows",
    }
    df = df.rename(columns=rename_map)

    for col in ["likes", "comments", "reach", "impressions", "saves", "shares", "profile_visits", "follows"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
        else:
            df[col] = 0

    keep = ["uri", "creation_timestamp", "title", "likes", "comments", "reach",
            "impressions", "saves", "shares", "profile_visits", "follows"]
    return df[keep]

# --------------------------------------------------
# Merge helper
# --------------------------------------------------

def merge_posts_with_insights(posts_df: pd.DataFrame, insights_df: pd.DataFrame) -> pd.DataFrame:
    """
    Left-join insights metrics onto flattened posts.
    Matches on (uri, creation_timestamp, title) when possible,
    or fills zeros if insights_df is empty.
    """
    if insights_df.empty:
        out = posts_df.copy()
        for c in ["likes","comments","reach","impressions","saves","shares"]:
            out[c] = 0
        return out

    out = posts_df.copy()

    merge_keys = [k for k in ["uri","creation_timestamp","title"] if k in posts_df.columns and k in insights_df.columns]
    if merge_keys:
        out = out.merge(insights_df, how="left", on=merge_keys, suffixes=("", "_insights"))
    else:
        if "creation_timestamp" in posts_df.columns and "creation_timestamp" in insights_df.columns:
            out = pd.merge_asof(
                posts_df.sort_values("creation_timestamp"),
                insights_df.sort_values("creation_timestamp"),
                on="creation_timestamp",
                direction="nearest",
                tolerance=pd.Timedelta("1D"),
            )
        else:
            for c in ["likes","comments","reach","impressions","saves","shares"]:
                out[c] = 0

    # fill blanks
    for c in ["likes","comments","reach","impressions","saves","shares"]:
        if c not in out.columns:
            out[c] = 0
        out[c] = pd.to_numeric(out[c], errors="coerce").fillna(0)

    return out
