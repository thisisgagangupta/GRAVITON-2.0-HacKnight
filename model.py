import cv2

# Replace with the actual path to your EAST model file
model_path = r'C:\Users\HARSHITA KAMANI\Desktop\yt\frozen_east_text_detection.pb'
#config_path = 'path/to/east_model.pbtxt'

# Load the EAST model
net = cv2.dnn.readNet(model_path)

# Check if the model loaded successfully
if net.empty():
    print("Error: Model could not be loaded.")
else:
    print("Model loaded successfully.")
