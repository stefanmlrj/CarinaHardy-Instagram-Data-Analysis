import pandas as pd
import matplotlib.pyplot as plt

def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds time-based features to the DataFrame, such as:
    - Hour of the day
    - Day of the week
    - Month of the year
    """
    df = df.copy()

    df['hour'] = df['creation_timestamp'].dt.hour

    df['weekday'] = df['creation_timestamp'].dt.day_name()

    df['month'] = df['creation_timestamp'].dt.month_name()

    return df

def analyze_engagement_by_time(df: pd.DataFrame) -> None:
    """
    Analyzes engagement based on the time of the post: 
    - Hour of the day
    - Day of the week
    - Month of the year
    """
    df = add_time_features(df)

    hourly_engagement = df.groupby('hour')['engagement'].mean().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(hourly_engagement['hour'], hourly_engagement['engagement'], marker='o')
    plt.title("Average Engagement by Hour of Day")
    plt.xlabel("Hour of Day")
    plt.ylabel("Average Engagement")
    plt.grid(True)
    plt.show()

    weekday_engagement = df.groupby('weekday')['engagement'].mean().reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]).reset_index()

    plt.figure(figsize=(10, 6))
    plt.bar(weekday_engagement['weekday'], weekday_engagement['engagement'])
    plt.title("Average Engagement by Day of Week")
    plt.xlabel("Day of Week")
    plt.ylabel("Average Engagement")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    monthly_engagement = df.groupby('month')['engagement'].mean().reindex([
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
        'September', 'October', 'November', 'December'
    ]).reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_engagement['month'], monthly_engagement['engagement'], marker='o')
    plt.title("Average Engagement by Month")
    plt.xlabel("Month")
    plt.ylabel("Average Enga
