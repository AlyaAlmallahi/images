import cv2
import matplotlib.pyplot as plt
import numpy as np
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description="Contrast Adjustment")
parser.add_argument("--image", required=True, help="Path to the input image")
args = parser.parse_args()

# Upload image and resize
image = cv2.imread(args.image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (256, 256))

# Convert to float to apply modifications
image_float = np.float32(image)

# Contrast adjustment: alpha > 1 increases contrast, beta = 0 changes brightness
alpha = 1.5  # contrast
beta = 0     #brightness
adjusted = cv2.convertScaleAbs(image_float, alpha=alpha, beta=beta)

# Display original and adjusted images side by side
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')

# Contrast adjusted image
plt.subplot(1, 2, 2)
plt.imshow(adjusted)
plt.title("Contrast Adjusted")
plt.axis('off')

plt.show()
