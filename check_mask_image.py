#%%
#%%
import json
import random
import os
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Path to the JSON file
json_file_path = "/fs/scratch/PAS2099/DataSet_Butterfly/train_test_separate/(malleti x plesseni) x malleti/test_data.json"

# Load the JSON data
with open(json_file_path, "r") as file:
    data = json.load(file)

# Base directory for relative paths
base_dir = "/fs/scratch/PAS2099/"

# Randomly select 10 elements from the data
random_elements = random.sample(data, 10)

# Define at least 18 distinct colors with transparency
color_map = [
    (255, 0, 0, 128),     # Red
    (255, 127, 0, 128),   # Orange
    (255, 255, 0, 128),   # Yellow
    (127, 255, 0, 128),   # Light Green
    (0, 255, 0, 128),     # Green
    (0, 255, 127, 128),   # Spring Green
    (0, 255, 255, 128),   # Cyan
    (0, 127, 255, 128),   # Light Blue
    (0, 0, 255, 128),     # Blue
    (127, 0, 255, 128),   # Purple
    (255, 0, 255, 128),   # Magenta
    (255, 0, 127, 128),   # Rose
    (127, 127, 127, 128), # Gray
    (255, 165, 0, 128),   # Amber
    (255, 69, 0, 128),    # Red-Orange
    (144, 238, 144, 128), # Pale Green
    (173, 216, 230, 128), # Light Blue (Soft)
    (221, 160, 221, 128)  # Plum
]

# Display final overlay images
for element in random_elements:
    x_value = element[0]
    image_url = element[1]
    mask_relative_path = element[2]
    mask_full_path = os.path.join(base_dir, mask_relative_path)  # Convert to full path

    try:
        # Step 1: Load the image from the URL
        print(f"Loading image from URL: {image_url}")
        with urllib.request.urlopen(image_url) as response:
            img = Image.open(response).convert("RGBA")
            img = img.resize((1024, 1024))  # Resize to ensure matching size

        # Step 2: Load the grayscale mask
        print(f"Loading mask from path: {mask_full_path}")
        if not os.path.exists(mask_full_path):
            raise FileNotFoundError(f"Mask file not found: {mask_full_path}")
        mask = Image.open(mask_full_path).convert("L")
        mask = mask.resize((1024, 1024))  # Resize to ensure matching size

        # Step 3: Normalize the mask to enhance visibility
        mask_np = np.array(mask)  # Convert mask to a NumPy array
        min_val, max_val = mask_np.min(), mask_np.max()
        if max_val > min_val:  # Avoid division by zero
            mask_normalized = ((mask_np - min_val) / (max_val - min_val) * 255).astype(np.uint8)
        else:
            mask_normalized = mask_np  # Keep it unchanged if all values are the same

        # Step 4: Convert normalized mask to RGBA with distinct colors
        rgba_mask = Image.new("RGBA", mask.size)
        for y in range(mask.size[1]):
            for x in range(mask.size[0]):
                gray_value = mask_normalized[y, x]
                if gray_value == 0:  # Background
                    rgba_mask.putpixel((x, y), (0, 0, 0, 0))  # Transparent
                else:
                    # Assign colors cyclically based on the mask value
                    color_index = (gray_value % len(color_map))
                    rgba_mask.putpixel((x, y), color_map[color_index])

        # Step 5: Ensure image and mask have the same size
        if img.size != rgba_mask.size:
            print("Resizing mismatch detected, aligning dimensions.")
            rgba_mask = rgba_mask.resize(img.size)

        # Step: Overlay the mask on the image
        overlay = Image.alpha_composite(img, rgba_mask)

        # Step 7: Show the final overlay image
        plt.figure(figsize=(8, 8))
        plt.imshow(overlay)
        plt.title(f"Overlayed Image (X Value: {x_value})")
        plt.axis("off")
        plt.show()

    except Exception as e:
        print(f"Error processing {image_url} or {mask_full_path}: {e}")
