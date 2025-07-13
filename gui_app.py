import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
from emotion_detector import detect_emotion
from recipe_recommender import recommend_meal
from image_display import load_image_for_gui
from mood_logger import log_mood_history
import random

# List of motivational quotes
QUOTES = [
    "Good food is good mood! 🍴",
    "You deserve something delicious today. 😊",
    "Let your taste buds dance! 💃",
    "One bite can change your day. ✨",
    "Feed your mood with flavor! 🍽️",
    "Comfort food for a comfort mood. 🧡"
]

def start_app():
    # Step 1: Detect emotion
    emotion = detect_emotion()
    if not emotion:
        mood_label.config(text="Mood detection failed.")
        return

    # Step 2: Recommend a meal
    meal = recommend_meal(emotion)
    mood_label.config(text=f"Detected Mood: {emotion.capitalize()}", foreground="#4CAF50")
    meal_label.config(text=f"Recommended Meal: {meal}")
    quote_label.config(text=random.choice(QUOTES))

    # Step 3: Show meal image
    meal_image = load_image_for_gui(meal)
    if meal_image:
        image_label.config(image=meal_image)
        image_label.image = meal_image  # Store reference
    else:
        image_label.config(text="No image found", image="")

    # Step 4: Log the history
    log_mood_history(emotion, meal)

# GUI Setup
root = tk.Tk()
root.title("Mood2Meal AI")
root.geometry("500x600")
root.configure(bg="#f5f5f5")

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 12), padding=10, background="#FF9800")

# Mood Label
mood_label = tk.Label(root, text="Press 'Detect Mood' to begin", font=("Helvetica", 14), bg="#f5f5f5", fg="#333")
mood_label.pack(pady=10)

# Meal Label
meal_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f5f5f5", fg="#000")
meal_label.pack(pady=10)

# Image Display
image_label = tk.Label(root, bg="#f5f5f5")
image_label.pack(pady=10)

# Quote Label
quote_label = tk.Label(root, text="", wraplength=400, font=("Georgia", 12, "italic"), bg="#f5f5f5", fg="#607d8b")
quote_label.pack(pady=20)

# Button
detect_button = ttk.Button(root, text="Detect Mood & Suggest Meal", command=start_app)
detect_button.pack(pady=20)

# Start GUI
root.mainloop()
