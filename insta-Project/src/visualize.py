import matplotlib.pyplot as plt
import pandas as pd

def plot_monthly_engagement(monthly_engagement: pd.DataFrame):
    """
    Plots the total engagement per month.
    """
    monthly_engagement['engagement'].plot(kind='line', figsize=(10, 6))
    plt.title('Monthly Engagement')
    plt.xlabel('Month')
    plt.ylabel('Total Engagement')
    plt.grid(True)
    plt.show()

def plot_engagement_rate(monthly_engagement: pd.DataFrame):
    """
    Plots the engagement rate per month.
    """
    monthly_engagement['engagement_rate'].plot(kind='line', figsize=(10, 6))
    plt.title('Monthly Engagement Rate')
    plt.xlabel('Month')
    plt.ylabel('Engagement Rate')
    plt.grid(True)
    plt.show()
