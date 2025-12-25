from datetime import datetime, timedelta

def date_range(end_date: str, days: int = 30):
    """
    Returns list of dates from (end_date - days) to end_date
    """
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return [
        (end - timedelta(days=i)).strftime("%Y-%m-%d")
        for i in reversed(range(days + 1))
    ]
