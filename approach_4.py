import os
import cv2
import numpy as np
import shutil
import pytesseract
from Levenshtein import distance
from skimage.metrics import structural_similarity as ssim
from skimage.transform import resize

def preprocess_image(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (500, 500))  # Resize to standard size
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # Apply thresholding
    return img

def extract_text(img_path):
    img = preprocess_image(img_path)
    text = pytesseract.image_to_string(img)
    return text

def calculate_image_similarity(img1_path, img2_path):
    img1 = preprocess_image(img1_path)
    img2 = preprocess_image(img2_path)
    return ssim(img1, img2)

def calculate_text_difference(text1, text2):
    return distance(text1, text2)

def process_images(input_folder, output_folder, image_similarity_threshold=0.7, text_difference_threshold=60):
    images = sorted(os.listdir(input_folder))
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    
    texts = {}

    i = 0
    while i < len(images) - 1:
        img1_path = os.path.join(input_folder, images[i])
        img2_path = os.path.join(input_folder, images[i+1])

        image_similarity = calculate_image_similarity(img1_path, img2_path)
        text1 = extract_text(img1_path)
        text2 = extract_text(img2_path)
        text_difference = calculate_text_difference(text1, text2)
        
        if image_similarity < image_similarity_threshold and text_difference > text_difference_threshold:
            shutil.copy(img1_path, os.path.join(output_folder, images[i]))
            
            texts[images[i]] = text1
        i += 1 

    
    shutil.copy(os.path.join(input_folder, images[-1]), os.path.join(output_folder, images[-1]))
    
    texts[images[-1]] = extract_text(os.path.join(input_folder, images[-1]))

    with open('output_sequential.txt', 'w') as f:
        for frame in sorted(texts.keys(), key=lambda x: int(x[6:-4])):
            f.write(f"Frame {frame}:\n{texts[frame]}\n\n")


input_directory = r"C:\Users\HARSHITA KAMANI\Desktop\yt\output_frames"
output_directory = r"C:\Users\HARSHITA KAMANI\Desktop\yt\final_frames_4"
process_images(input_directory, output_directory)
