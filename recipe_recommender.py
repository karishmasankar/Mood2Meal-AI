import pandas as pd
import random

def recommend_meal(emotion):
    try:
        df = pd.read_csv("recipes.csv")
        row = df[df['mood'].str.lower() == emotion.lower()]
        if not row.empty:
            options = row['meal'].tolist()
            return random.choice(options)
        else:
            return "No meal found for that mood!"
    except Exception as e:
        return f"Error: {e}"
