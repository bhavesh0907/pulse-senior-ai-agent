import random
from datetime import datetime
from src.utils.io_utils import save_json

MOCK_TOPICS = [
    "delivery issue",
    "food stale",
    "delivery partner rude",
    "app crashing",
    "late delivery",
    "refund delayed",
    "maps not working",
    "instamart closed early"
]

def generate_mock_reviews(date: str, n: int = 50):
    reviews = []
    for i in range(n):
        topic = random.choice(MOCK_TOPICS)
        reviews.append({
            "review_id": f"{date}_{i}",
            "date": date,
            "rating": random.randint(1, 5),
            "text": f"I faced a {topic} today.",
            "source": "google_play"
        })
    return reviews

def ingest_daily_reviews(date: str, output_dir="data/raw_reviews"):
    reviews = generate_mock_reviews(date)
    path = f"{output_dir}/{date}.json"
    save_json(reviews, path)
    return path
