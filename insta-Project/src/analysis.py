import pandas as pd
import matplotlib.pyplot as plt

def analyze_engagement_by_time(posts_df: pd.DataFrame):
    """
    Analyzes how engagement varies by the time of day.
    - Extracts the hour from the timestamp
    - Plots average engagement by hour
    """
    posts_df['hour'] = posts_df['timestamp'].dt.hour

    hourly_engagement = posts_df.groupby('hour')['engagement'].mean().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(hourly_engagement['hour'], hourly_engagement['engagement'], marker='o')
    plt.title('Average Engagement by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Average Engagement')
    plt.grid(True)
    plt.show()

def analyze_engagement_by_content_type(posts_df: pd.DataFrame):
    """
    Analyzes engagement based on content type (e.g., post, story, reel).
    """
    if 'content_type' not in posts_df.columns:
        raise ValueError("Missing 'content_type' column in data")

    content_engagement = posts_df.groupby('content_type')[['engagement', 'likes', 'comments']].mean().reset_index()

    content_engagement.set_index('content_type')[['engagement', 'likes', 'comments']].plot(kind='bar', figsize=(12, 6))
    plt.title('Engagement by Content Type')
    plt.ylabel('Average Engagement')
    plt.xlabel('Content Type')
    plt.show()

