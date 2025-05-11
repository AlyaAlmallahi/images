import cv2
import matplotlib.pyplot as plt
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description="Resizing & Normalization")
parser.add_argument("--image", required=True, help="Path to the input image")
args = parser.parse_args()

# Load image
image = cv2.imread(args.image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Resize the image to 256x256 pixels
resized = cv2.resize(image, (256, 256))

# (Normalization)
normalized = resized / 255.0

# Display original and resized & normalized images side by side
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')

# Resized & Normalized image
plt.subplot(1, 2, 2)
plt.imshow(normalized)
plt.title("Resized & Normalized")
plt.axis('off')

plt.show()
