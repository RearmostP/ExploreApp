from datetime import date

def current_year() -> str:
    return str(date.today().year)

def current_month_day() -> str:
    today = date.today()
    return str(f"{today.month:02d}-{today.day:02d}")
