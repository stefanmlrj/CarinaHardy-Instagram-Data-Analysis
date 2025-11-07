import pandas as pd

def categorize_image_content(df: pd.DataFrame) -> pd.DataFrame:
    """
    Categorizes image content based on its attributes like file extension and presence of people.
    """
    df = df.copy()

    # Content type: Image (e.g., .jpg, .png) vs. Video (e.g., .mp4)
    df['content_type'] = df['uri'].apply(lambda x: 'Image' if x.endswith(('.jpg', '.png')) else ('Video' if x.endswith('.mp4') else 'Other'))

    # Presence of people: Simple heuristic if title contains common person names
    df['contains_people'] = df['title'].apply(lambda x: 1 if 'person' in str(x).lower() else 0)
    
    # Presence of Jewelry: Basic heuristic or metadata
    df['contains_jewelry'] = df['title'].apply(lambda x: 1 if 'jewelry' in str(x).lower() else 0)

    return df
