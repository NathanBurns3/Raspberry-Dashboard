import os
import random

def fetch_photo():
    slideshow_dir = os.path.join(os.path.dirname(__file__), "../../../assets/images/slideshow")
    images = [os.path.join(slideshow_dir, file) for file in os.listdir(slideshow_dir) if file.lower().endswith((".png", ".jpg", ".jpeg"))]
    if not images:
        return None
    return random.choice(images)