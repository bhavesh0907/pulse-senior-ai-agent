import os
import pandas as pd
from src.utils.io_utils import load_json
from src.utils.date_utils import date_range

PROCESSED_DIR = "data/processed"


def generate_trend_table(target_date: str, days: int = 30):
    dates = date_range(target_date, days)
    trend_data = {}

    for date in dates:
        file_path = f"{PROCESSED_DIR}/{date}_topics.json"
        if not os.path.exists(file_path):
            continue

        topic_counts = load_json(file_path)

        for topic, count in topic_counts.items():
            if topic not in trend_data:
                trend_data[topic] = {d: 0 for d in dates}
            trend_data[topic][date] += count

    df = pd.DataFrame.from_dict(trend_data, orient="index")
    df = df.fillna(0).astype(int)
    return df
