import os

def save_report(df, target_date: str, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    path = f"{output_dir}/trend_report_{target_date}.csv"
    df.to_csv(path)
    return path
