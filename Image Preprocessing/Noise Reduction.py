import cv2
import matplotlib.pyplot as plt
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description="Noise Reduction")
parser.add_argument("--image", required=True, help="Path to the input image")
args = parser.parse_args()

img = cv2.imread(args.image)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (256, 256))

# Gaussian Blur
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# Median Blur
median = cv2.medianBlur(img, 5)

# Display original and blurred images side by side
plt.figure(figsize=(12, 6))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')

# Gaussian blurred image
plt.subplot(1, 3, 2)
plt.imshow(gaussian)
plt.title("Gaussian Blur")
plt.axis('off')

# Median blurred image
plt.subplot(1, 3, 3)
plt.imshow(median)
plt.title("Median Blur")
plt.axis('off')

plt.show()
