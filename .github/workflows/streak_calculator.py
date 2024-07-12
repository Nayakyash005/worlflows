from datetime import datetime, timedelta

def calculate_streak(dates):
    dates = sorted(dates)
    streak = 0
    current_streak = 0
    previous_date = None

    for date in dates:
        if previous_date and date == previous_date + timedelta(days=1):
            current_streak += 1
        else:
            current_streak = 1
        streak = max(streak, current_streak)
        previous_date = date

    return streak

if __name__ == "__main__":
    # Example usage
    dates = [
        datetime(2024, 7, 1),
        datetime(2024, 7, 2),
        datetime(2024, 7, 3),
        datetime(2024, 7, 5),
        datetime(2024, 7, 6)
    ]
    streak = calculate_streak(dates)
    with open("streak.txt", "w") as file:
        file.write(f"Current streak: {streak} days\n")
