from src.core.pipeline import run_ingestion
from src.core.trend_generator import generate_trend_table
from src.core.report_writer import save_report

TARGET_DATE = "2024-06-30"

if __name__ == "__main__":
    run_ingestion(
        app_name="Swiggy",
        target_date=TARGET_DATE
    )

    df = generate_trend_table(TARGET_DATE)
    report_path = save_report(df, TARGET_DATE)

    print(f"Trend report saved at {report_path}")
