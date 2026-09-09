"""ARTI 403 Image Processing Lab 1 exercises."""

from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import Image

project_dir = Path(__file__).resolve().parent
image_dir = project_dir / "images"
cameraman_path = image_dir / "cameraman.tif"
lena_path = image_dir / "lena_gray_256.tif"
fallback_path = project_dir / "content.tiff"

if not cameraman_path.exists():
    cameraman_path = fallback_path
    print(f"cameraman.tif was not found; using {fallback_path.name} instead.")

if not lena_path.exists():
    lena_path = fallback_path
    print(f"lena_gray_256.tif was not found; using {fallback_path.name} instead.")

# Task #2a: Load and visualize an image with OpenCV.
img = cv2.imread(str(cameraman_path))

if img is None:
    raise FileNotFoundError(f"Could not load image: {cameraman_path}")
else:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.title("Cameraman (loaded with OpenCV)")
    plt.show()

# Task #2b: Load and visualize an image with PIL.
img2 = Image.open(lena_path)

plt.imshow(img2, cmap=cm.Greys_r)
plt.title("Lena (loaded with PIL)")
plt.show()

# Task #3: Save an image with OpenCV.
cv2.imwrite(str(project_dir / "new_image.jpg"), img)
img2.save(project_dir / "new_image2.jpg")

# Task #4: Display image data as NumPy arrays.
print("---- OpenCV image (NumPy array) ----")
print("Shape:", img.shape)
print(img)

print("\n---- PIL image converted to NumPy array ----")
img_array = np.array(img2)
print("Shape:", img_array.shape)
print(img_array)