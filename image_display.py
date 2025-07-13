import os
from PIL import Image, ImageTk
import cv2

def show_meal_image(meal_name):
    try:
        filename = meal_name.replace(" ", "_") + ".jpg"
        image_path = os.path.join("meal_images", filename)

        if not os.path.exists(image_path):
            print(f"⚠️ Image file not found: {image_path}")
            return

        img = cv2.imread(image_path)
        if img is not None:
            cv2.imshow(f"🍽️ Your Meal: {meal_name}", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("⚠️ Unable to load the image.")
    except Exception as e:
        print("⚠️ Error showing image:", e)
def load_image_for_gui(meal_name):
    try:
        filename = meal_name.replace(" ", "_") + ".jpg"
        image_path = os.path.join("meal_images", filename)

        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((300, 200))
            return ImageTk.PhotoImage(img)
        else:
            return None
    except Exception as e:
        print("Error loading image:", e)
        return None
