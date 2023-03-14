import os
import sys
import cv2
import numpy as np

# Get the file name from command line arguments
if len(sys.argv) != 2:
    print("Usage: python script.py <file_name>")
    sys.exit(1)
file_name = sys.argv[1]

# Load the color image
img = cv2.imread(file_name)

# Split the color image into its RGB color channels
b, g, r = cv2.split(img)

# Create a blank array for the false color infrared image
infrared = np.zeros_like(img)

# Assign the R channel to the B channel of the infrared image
infrared[:,:,0] = r

# Assign the G channel to the G channel of the infrared image
infrared[:,:,1] = g

# Assign the B channel to the R channel of the infrared image
infrared[:,:,2] = b

# Create a folder for the infrared images (if it doesn't already exist)
if not os.path.exists('infrared_images'):
    os.mkdir('infrared_images')

# Generate a file name for the infrared image
base_name, ext = os.path.splitext(os.path.basename(file_name))
infrared_name = os.path.join('infrared_images', base_name + '_infrared' + ext)

# Save the false color infrared image to the folder
cv2.imwrite(infrared_name, infrared)

# Display the false color infrared image
cv2.imshow('Infrared Image', infrared)
cv2.waitKey(0)
