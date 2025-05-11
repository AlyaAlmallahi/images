# Image Preprocessing Project

This project demonstrates various image preprocessing techniques using Python and OpenCV. The techniques include contrast adjustment, edge enhancement, color space conversion, noise reduction, binarization, resizing & normalization, sharpening, and clustering (K-Means).

## Dataset
The project uses sample images stored in the `dataset` folder. Ensure the following images are 

## Files
### Image Preprocessing
- **Contrast Adjustment.py**: Adjusts the contrast of an image.
- **Edge Enhancement.py**: Enhances edges using Canny edge detection.
- **Color Space Conversion.py**: Converts an image to HSV and displays its channels.
- **Noise Reduction.py**: Applies Gaussian and Median blurring.
- **Binarization.py**: Converts an image to binary using thresholding.
- **Resizing & Normalization.py**: Resizes and normalizes an image.
- **Sharpening.py**: Sharpens an image using a kernel.

### Model Selection
- **K-Means.ipynb**: Segments an image using K-Means clustering.
 
### Notebooks
- **K-Means.ipynb**: A well-documented notebook demonstrating K-Means clustering for image segmentation.
 
## Visual Examples
Below are some examples of the preprocessing and clustering results:

### Preprocessing
- **Original Image**:
  ![Original Image](dataset-min/Animals.jpg)
- **Contrast Adjusted**:
  ![Contrast Adjusted](dataset-min/contrast_adjusted.png)
- **Edge Detection**:
  ![Edge Detection](dataset-min/edge_detection.png)

### Clustering
- **K-Means Segmentation**:
  ![K-Means Segmentation](dataset-min/kmeans_segmentation.png)
 

## Steps to Run
1. Clone the repository or download the files.
2. Install the required libraries:
   ```bash
   pip install opencv-python matplotlib numpy scikit-learn scikit-image
   ```
3. Place the required images in the `data` folder.
4. Open the notebooks in Jupyter Notebook, Kaggle, or Google Colab.
5. Run the cells sequentially to reproduce the results.

## Hosted Notebooks
- [K-Means Notebook on Kaggle](#) *(Replace with actual link)*
 
## Additional Features

### GUI Application
A user-friendly GUI application has been developed using Python's `tkinter` library. It allows users to:
- Upload an image.
- Select an image preprocessing or clustering operation.
- Apply the selected operation with ease.

The GUI application is located in the `GUI` folder:
- **File**: `main_gui.py`
