import csv
from datetime import datetime

def log_mood_history(mood, meal):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("mood_history.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, mood, meal])
