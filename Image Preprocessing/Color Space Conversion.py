import cv2
import matplotlib.pyplot as plt
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description="Color Space Conversion")
parser.add_argument("--image", required=True, help="Path to the input image")
args = parser.parse_args()

img = cv2.imread(args.image)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (256, 256))

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# Display channels
h, s, v = cv2.split(hsv)

# Display original and HSV channels side by side
plt.figure(figsize=(12, 6))

# Original image
plt.subplot(1, 4, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')

# Hue channel
plt.subplot(1, 4, 2)
plt.imshow(h, cmap='gray')
plt.title("Hue")
plt.axis('off')

# Saturation channel
plt.subplot(1, 4, 3)
plt.imshow(s, cmap='gray')
plt.title("Saturation")
plt.axis('off')

# Value channel
plt.subplot(1, 4, 4)
plt.imshow(v, cmap='gray')
plt.title("Value")
plt.axis('off')

plt.show()
