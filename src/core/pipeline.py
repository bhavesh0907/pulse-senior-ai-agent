from src.agents.review_ingestion_agent import ingest_daily_reviews
from src.agents.topic_extraction_agent import extract_topics_from_reviews
from src.agents.topic_dedup_agent import canonicalize_topics
from src.agents.topic_storage import save_daily_topics
from src.utils.date_utils import date_range


def run_ingestion(app_name: str, target_date: str):
    print(f"Starting ingestion for {app_name}")
    dates = date_range(target_date, days=30)

    for date in dates:
        review_path = ingest_daily_reviews(date)

        raw_topic_counts = extract_topics_from_reviews(review_path)
        canonical_topic_counts = canonicalize_topics(raw_topic_counts)

        save_daily_topics(date, canonical_topic_counts)
        print(f"Canonicalized topics for {date}")
