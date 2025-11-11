# src/performance_analysis.py
def get_performance_posts(posts_model, label):
    return posts_model[posts_model["performance_label_log"] == label]["uri"].tolist()
