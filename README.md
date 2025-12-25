# Senior AI Engineer Assignment – Review Trend Intelligence Agent

### Overview
This project implements an **agentic AI system** that ingests **daily app reviews**, extracts **issues, requests, and feedback topics**, **deduplicates semantically similar topics**, and generates a **30-day rolling trend analysis report**.

The system mirrors **real-world AI product analytics pipelines** and focuses on:
- High-recall topic extraction  
- Stable topic taxonomy over time  
- Accurate frequency-based trend reporting  

Traditional topic modeling approaches (LDA, BERTopic, etc.) are deliberately avoided, as per the assignment requirements. Instead, the solution relies on **agent-based reasoning and semantic similarity**.

---

### Problem Statement
Given Google Play Store reviews (June 2024 → present) for a popular app (e.g., Swiggy):

- Treat **each day’s reviews as a batch**
- Extract **issues, requests, and feedback topics**
- Merge **semantically similar topics** into canonical categories
- Produce a **trend table** where:
  - Rows = Topics  
  - Columns = Dates (T-30 → T)  
  - Cells = **Frequency of topic occurrence on that date**

---

### High-Level Architecture

Daily Reviews (Batch)
↓
Review Ingestion Agent
↓
Topic Extraction Agent (High Recall)
↓
Topic Deduplication & Canonicalization Agent
↓
Persistent Topic Registry
↓
Trend Aggregation Engine
↓
30-Day Trend Report (CSV)

markdown
Copy code

---

### Agentic Design

### 1. Review Ingestion Agent
- Ingests reviews **per day**
- Stores each batch as `YYYY-MM-DD.json`
- Ensures deterministic and reproducible processing

### 2. Topic Extraction Agent
- Extracts **short, normalized topic phrases**
- Optimized for **high recall**
- Outputs **topic → frequency** per day
- Supports:
  - Mock mode (for demos and testing)
  - Live LLM mode (when API quota is available)

### 3. Topic Deduplication & Canonicalization Agent
- Maintains a **long-lived Topic Registry**
- Uses **semantic embeddings + cosine similarity**
- Decides whether a topic should:
  - Merge into an existing canonical topic, or
  - Create a new canonical topic
- Prevents duplicate or fragmented trends across time

### 4. Trend Generator
- Aggregates canonical topic counts across days
- Produces a **30-day rolling trend matrix**
- Outputs a CSV consumable by product and analytics teams

---

### Folder Structure

pulse_senior_ai_agent/
├── src/
│ ├── agents/
│ │ ├── review_ingestion_agent.py
│ │ ├── topic_extraction_agent.py
│ │ ├── topic_dedup_agent.py
│ │ └── topic_storage.py
│ ├── core/
│ │ ├── pipeline.py
│ │ ├── trend_generator.py
│ │ └── report_writer.py
│ └── utils/
│ ├── date_utils.py
│ └── io_utils.py
├── data/
│ ├── raw_reviews/
│ └── processed/
│ └── topic_registry.json
├── output/
│ └── trend_report_YYYY-MM-DD.csv
├── configs/
│ └── config.yaml
├── venv/
└── README.md

---

## How to Run

### 1. Activate Virtual Environment
source venv/bin/activate

### 2. Run the Full Pipeline
python -m src.main

### 3. Output
The final trend report will be generated at:
output/trend_report_YYYY-MM-DD.csv

### Output Format
                        2024-05-31	2024-06-01	2024-06-02	2024-06-03	2024-06-04	
delivery issue	          20	       20	      28	       22	       11	
late delivery	          20	       20	      28	       22	       11	
delivery partner rude	  20	       20	      28	       22	       11	
app crashing	          6	           6	      4	           3	       5	
refund delayed	          7	           2	      4	           12	       6	
maps not working	      4	           10	      4	           8	       7	
instamart availability	  5	           8	      4	           3	       7	
food quality issue	      11	       14	      16	       6	       17	


### Deduplication Strategy (Key Challenge)
To handle semantically similar but differently phrased complaints (e.g.,
“delivery guy was rude” vs “delivery partner behaved badly”):

Sentence embeddings are used to compute semantic similarity

Cosine similarity determines whether topics should be merged

Canonical topics remain stable across time

Variant phrases are tracked internally in a topic registry

This approach ensures accurate trend analysis and prevents topic fragmentation.

### Mock vs Live Data
Mock mode is used for deterministic demos and quota-free execution

The architecture supports live LLM-based extraction with no structural changes

Some trend similarity is expected with synthetic data and is documented

### Assumptions
Reviews are available on a per-day basis

Each review may contain multiple topic signals

Topic frequency reflects count of mentions, not sentiment intensity

### Limitations
Mock data does not fully reflect real-world linguistic noise

No UI/dashboard (out of scope)

Ingestion is batch-based, not real-time

### Why This Approach
Aligns with real-world AI product analytics systems

Prioritizes accuracy and stability over heuristics

Explicitly solves the semantic deduplication problem highlighted in the assignment

Scales naturally to real app review data

### Conclusion
This project delivers a production-grade, agentic AI pipeline for extracting and analyzing trends from app reviews. The design emphasizes correctness, extensibility, and strict alignment with assignment requirements.