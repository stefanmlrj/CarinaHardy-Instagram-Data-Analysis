import matplotlib.pyplot as plt

def analyze_audience_behavior(df: pd.DataFrame):
    """
    Analyzes the relationship between content engagement and audience actions like profile visits, follows, and saves.
    """
    corr_df = df[['engagement', 'profile_visits', 'follows', 'saves']]
    corr_matrix = corr_df.corr()

    import seaborn as sns
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Between Engagement and Audience Behavior")
    plt.show()
