from emotion_detector import detect_emotion
from recipe_recommender import recommend_meal
from image_display import show_meal_image
import csv
from datetime import datetime

# Define the logging function before you call it
def log_mood_history(mood, meal):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("mood_history.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, mood, meal])

# Step 1: Detect emotion
emotion = detect_emotion()

# Step 2: Recommend meal
if emotion:
    meal = recommend_meal(emotion)
    print(f"\n🍽️ Based on your mood '{emotion}', we recommend: {meal}")
    show_meal_image(meal)
    log_mood_history(emotion, meal)
else:
    print("Could not detect emotion to suggest a meal.")
