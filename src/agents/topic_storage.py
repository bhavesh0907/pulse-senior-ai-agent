from src.utils.io_utils import save_json

def save_daily_topics(date: str, topic_counts: dict, output_dir="data/processed"):
    path = f"{output_dir}/{date}_topics.json"
    save_json(topic_counts, path)
    return path
