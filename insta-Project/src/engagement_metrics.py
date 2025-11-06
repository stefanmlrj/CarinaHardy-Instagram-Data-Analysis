import pandas as pd

def prepare_engagement_fields(df: pd.DataFrame, default_followers: int | float = 1000) -> pd.DataFrame:
    """
    Guarantees presence of likes/comments/followers_count with sensible defaults.
    """
    df = df.copy()
    if "likes" not in df.columns: df["likes"] = 0
    if "comments" not in df.columns: df["comments"] = 0
    if "followers_count" not in df.columns:
        df["followers_count"] = default_followers
    df["likes"] = pd.to_numeric(df["likes"], errors="coerce").fillna(0)
    df["comments"] = pd.to_numeric(df["comments"], errors="coerce").fillna(0)
    df["followers_count"] = pd.to_numeric(df["followers_count"], errors="coerce").replace(0, default_followers)
    return df

def calculate_engagement_metrics(posts_df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds:
      - engagement = likes + comments
      - engagement_rate = engagement / followers_count
    """
    df = posts_df.copy()
    df = prepare_engagement_fields(df)
    df["engagement"] = df["likes"] + df["comments"]
    df["engagement_rate"] = (df["engagement"] / df["followers_count"]).replace([float("inf"), -float("inf")], 0).fillna(0)
    return df

def aggregate_engagement_by_month(df: pd.DataFrame, ts_col: str = "creation_timestamp") -> pd.DataFrame:
    """
    Returns monthly sums/means useful for plotting and trend analysis.
    """
    if ts_col not in df.columns:
        return pd.DataFrame()
    grp = df.copy()
    grp["month"] = grp[ts_col].dt.to_period("M")
    out = grp.groupby("month")[["likes","comments","engagement","engagement_rate"]].agg({"likes":"sum","comments":"sum","engagement":"sum","engagement_rate":"mean"})
    return out.reset_index()
