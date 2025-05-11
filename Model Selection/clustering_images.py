import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

image_folder = 'dataset-min/'
output_folder = 'output/'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(image_folder):
    if filename.endswith(('.jpg', '.png', '.jpeg')):
        path = os.path.join(image_folder, filename)

        # Load image
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (256, 256))

        # Preprocessing (Blur)
        blurred = cv2.GaussianBlur(img, (5, 5), 0)

        # Reshape image to 2D pixels
        pixel_values = blurred.reshape((-1, 3))
        pixel_values = np.float32(pixel_values)

        # KMeans
        k = 4
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(pixel_values)
        centers = np.uint8(kmeans.cluster_centers_)
        segmented_image = centers[labels.flatten()].reshape(img.shape)

        # Save output
        out_path = os.path.join(output_folder, f'segmented_{filename}')
        segmented_bgr = cv2.cvtColor(segmented_image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(out_path, segmented_bgr)

        print(f"Processed: {filename}")
