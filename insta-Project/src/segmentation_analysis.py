import matplotlib.pyplot as plt
import pandas as pd

def analyze_content_performance_by_type(df: pd.DataFrame):
    """
    Analyzes content performance by content type (e.g., portrait vs landscape, with/without people).
    """
    # Group by 'aspect_ratio' and calculate the mean engagement
    performance = df.groupby('aspect_ratio')[['likes', 'comments', 'engagement']].mean()

    # Plot content performance by aspect ratio (portrait vs landscape)
    performance.plot(kind='bar', figsize=(12, 6), title="Content Performance by Aspect Ratio")
    plt.ylabel("Average Engagement")
    plt.xlabel("Aspect Ratio (Portrait vs Landscape)")
    plt.show()

    # Group by 'contains_people' and analyze
    people_performance = df.groupby('contains_people')[['likes', 'comments', 'engagement']].mean()
    people_performance.plot(kind='bar', figsize=(12, 6), title="Content Performance With/Without People")
    plt.ylabel("Average Engagement")
    plt.xlabel("Contains People (1 = Yes, 0 = No)")
    plt.show()

def segment_by_engagement(df: pd.DataFrame):
    """
    Segments the posts into high, medium, and low engagement groups and compares performance by content type.
    """
    def engagement_label(rate):
        if rate >= df["engagement_rate"].quantile(0.75):
            return "High"
        elif rate >= df["engagement_rate"].quantile(0.25):
            return "Medium"
        else:
            return "Low"

    df['engagement_segment'] = df['engagement_rate'].apply(engagement_label)

    # Analyze engagement by content type in different segments
    segment_performance = df.groupby(['engagement_segment', 'aspect_ratio'])[['likes', 'comments', 'engagement']].mean()
    segment_performance.unstack(level=0).plot(kind='bar', figsize=(12, 6))
    plt.title("Performance by Content Type and Engagement Segment")
    plt.ylabel("Average Engagement")
    plt.show()

