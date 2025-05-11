import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description="K-Means Clustering")
parser.add_argument("--image", required=True, help="Path to the input image")
args = parser.parse_args()

# 1. Load and resize image
img = cv2.imread(args.image)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (256, 256))

# 2. Reshape the image to a 2D array of pixels
pixel_values = img.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

# 3. Apply K-Means clustering
k = 4  # number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(pixel_values)

# 4. Replace each pixel with its cluster center
centers = np.uint8(kmeans.cluster_centers_)
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(img.shape)

# 5. Display results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.title(f"K-Means Segmentation (k={k})")
plt.imshow(segmented_image)
plt.show()