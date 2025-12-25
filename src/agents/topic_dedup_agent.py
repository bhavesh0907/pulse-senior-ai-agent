import json
import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

MODEL = SentenceTransformer("all-MiniLM-L6-v2")
REGISTRY_PATH = "data/processed/topic_registry.json"
SIM_THRESHOLD = 0.85


def load_registry():
    if not os.path.exists(REGISTRY_PATH):
        return {}
    with open(REGISTRY_PATH, "r") as f:
        return json.load(f)


def save_registry(registry):
    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2)


def canonicalize_topics(daily_topic_counts: dict):
    """
    Input:
    {
        "delivery issue": 12,
        "late delivery": 3
    }

    Output:
    {
        "delivery issue": 15
    }
    """
    registry = load_registry()
    canonical_topics = list(registry.keys())
    canonical_embeddings = MODEL.encode(canonical_topics) if canonical_topics else []

    canonical_counts = {}

    for topic, count in daily_topic_counts.items():

        # First topic ever
        if not canonical_topics:
            registry[topic] = [topic]
            canonical_counts[topic] = count
            canonical_topics.append(topic)
            canonical_embeddings = MODEL.encode(canonical_topics)
            continue

        topic_embedding = MODEL.encode([topic])
        similarities = cosine_similarity(topic_embedding, canonical_embeddings)[0]

        best_idx = similarities.argmax()
        best_score = similarities[best_idx]

        if best_score >= SIM_THRESHOLD:
            canonical = canonical_topics[best_idx]
            registry[canonical].append(topic)
            canonical_counts[canonical] = canonical_counts.get(canonical, 0) + count
        else:
            registry[topic] = [topic]
            canonical_counts[topic] = count
            canonical_topics.append(topic)
            canonical_embeddings = MODEL.encode(canonical_topics)

    save_registry(registry)
    return canonical_counts
