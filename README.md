
# 🧠 Mood2Meal AI 🍽️

> **"Let your mood decide your food!"**

**Mood2Meal AI** is a Python-based desktop app that detects your mood using your webcam and recommends a suitable meal. It also shows an image of the recommended dish and logs your mood history for future reference.

---

## 🎯 Features

- 😊 **Real-time emotion detection** using DeepFace
- 🍱 **Mood-based meal recommendations**
- 🖼️ Displays a dish image based on your detected mood
- 🗂️ Logs every mood and meal suggestion in a history file
- 🖥️ Beautiful GUI interface using Tkinter
- 📸 Screenshot-ready for showcasing

---

## 🧠 How It Works

1. Starts your webcam and captures your emotion.
2. Analyzes your face and detects your **dominant mood**.
3. Picks a **random meal** from the `recipes.csv` file based on that mood.
4. Displays a **visual image of the dish**.
5. Logs your mood and meal to `mood_history.csv`.

---

## 🖥️ Screenshots

### 1️⃣ Mood Detection via Webcam
> Captures a frame and detects the user's facial emotion.

![Mood Detection](screenshots/mood_detection.png)

---

### 2️⃣ Meal Recommendation
> Based on the detected emotion, a suitable meal is recommended.

![Meal Recommendation](screenshots/meal_recommendation.png)

---

### 3️⃣ Dish Image Preview
> Shows a relevant dish image from the `meal_images/` folder.

![Meal Image](screenshots/meal_image.png)

---

### 4️⃣ Mood History Logging
> Every emotion and meal is logged in a CSV file for later reference.

![Mood History](screenshots/mood_logging.png)

---

## 🗂️ Project Structure

```

Mood2Meal-AI/
│
├── main.py                  # Main controller
├── emotion\_detector.py      # Webcam + DeepFace emotion detection
├── recipe\_recommender.py    # Meal suggestion logic
├── image\_display.py         # Load & show meal images
├── gui\_app.py               # Tkinter-based GUI
├── mood\_logger.py           # Log mood and meal
├── recipes.csv              # Meals mapped to moods
├── mood\_history.csv         # Logged mood + meal history
├── meal\_images/             # Dish image folder
└── screenshots/             # For README.md visuals

````

---

## ⚙️ Requirements

Install the required Python libraries:

```bash
pip install deepface opencv-python pandas Pillow tk
````

Ensure you are using **Python 3.10** as DeepFace works best with it.

---

## 🚀 Run the Project

```bash
py -3.10 gui_app.py
```

Or, if using CLI version:

```bash
py -3.10 main.py
```

---

## ❤️ Quote

> *"A happy mood deserves something sweet. A sad soul? Soup might help."*
> — Mood2Meal AI

---

## 👩‍💻 Created by

**Karishma S.J**
CSE | AI-ML Enthusiast

```

---
