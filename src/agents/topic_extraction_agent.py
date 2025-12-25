from collections import Counter
from src.utils.io_utils import load_json

# Mock topics for deterministic demo
MOCK_TOPIC_MAP = [
    "delivery issue",
    "late delivery",
    "food quality issue",
    "delivery partner rude",
    "refund delayed",
    "app crashing",
    "maps not working",
    "instamart availability"
]

def extract_topics_from_reviews(review_file: str):
    """
    Returns:
    {
        "delivery issue": 12,
        "late delivery": 3,
        ...
    }
    """
    reviews = load_json(review_file)
    extracted_topics = []

    for review in reviews:
        text = review["text"].lower()
        for topic in MOCK_TOPIC_MAP:
            if any(word in text for word in topic.split()):
                extracted_topics.append(topic)

    return dict(Counter(extracted_topics))
