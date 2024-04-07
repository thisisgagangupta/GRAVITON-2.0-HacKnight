# Add the path to the YOLOv7 repository to the PYTHONPATH
import sys
sys.path.insert(0, 'C:/Users/Harshita Kamani/Desktop/yolov7')


import os
import torch
from PIL import Image
from models.experimental import attempt_load  # Import the function to load the model

# Load the model
model = attempt_load(r'C:\Users\HARSHITA KAMANI\Desktop\yolov7.pt')  # Use the function from the models.experimental module

# Make sure to call model.eval() method before inferencing
model.eval()

# Define the input and output directories
input_dir = 'final_frames_4'
output_dir = 'diagrams'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Initialize a counter for the diagrams
diagram_counter = 0

# Iterate over the images in the input directory
for filename in os.listdir(input_dir):
    # Only process .jpg files
    if filename.endswith('.jpg'):
        # Load the image
        img = Image.open(os.path.join(input_dir, filename))

        # Perform inference
        results = model(img)

        # Filter the results to only include human bodies
        human_bodies = results.xyxy[0][results.xyxy[0][:, -1] == 'person']

        # If there are any human bodies
        if len(human_bodies) > 0:
            # Iterate over the human bodies
            for human_body in human_bodies:
                # Get the bounding box coordinates
                x1, y1, x2, y2 = human_body[:4]

                # Crop the human body from the image
                cropped_img = img.crop((x1, y1, x2, y2))

                # Save the cropped human body in the output directory
                cropped_img.save(os.path.join(output_dir, f'human_body_{diagram_counter}.jpg'))

                # Increment the counter
                diagram_counter += 1

# Print a success message
print(f"Human bodies from the images in {input_dir} have been successfully detected, cropped, and saved in {output_dir}.")
