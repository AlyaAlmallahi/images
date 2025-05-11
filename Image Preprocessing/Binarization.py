import cv2
import matplotlib.pyplot as plt
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description="Binarization")
parser.add_argument("--image", required=True, help="Path to the input image")
args = parser.parse_args()

# Upload the image and convert it to grayscale.
image = cv2.imread(args.image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#binarization application
_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# Display original and binarized images side by side
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')

# Binarized image
plt.subplot(1, 2, 2)
plt.imshow(binary, cmap='gray')
plt.title("Binarized Image")
plt.axis('off')

plt.show()
