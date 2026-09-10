# Image Processing Lab

## Introduction

This lab is about some basic image processing operations using Python.
I used Jupyter Notebook to read images, convert them into arrays, and apply different operations to see how the images change.

The images I used are:

* `lena_gray_256.tif`
* `cameraman.tif`

The main libraries I used are:

* NumPy
* Matplotlib
* Pillow
* OpenCV

## Installation

If the libraries are not installed, I used the following command in Jupyter Notebook:

```python
%pip install numpy matplotlib pillow opencv-python
```

## Task 1 - Sampling and Quantization

In the first task, I worked with sampling and quantization.

### Sampling

I changed the sampling factor to see how it affects the image resolution.

For example:

```python
sampling_factor = 14
```

When the sampling factor is increased, the image has less spatial information and the image becomes lower in resolution.

### Quantization

I also changed the number of quantization levels.

For example:

```python
quantization_levels = 9
```

Quantization changes the number of gray levels in the image. When the number of levels is reduced, the image has fewer shades of gray and the difference becomes more noticeable.

I displayed the original image, sampled image, and quantized image next to each other to compare the results.

## Task 2 - Image Operations

For Task 2, I read two grayscale images and converted them into NumPy arrays.

```python
im1arr = np.asarray(img1)
im2arr = np.asarray(img2)
```

I resized both images to:

```python
resize = (400, 400)
```

Then I performed the required operations.

### 1. Subtraction

I subtracted the two images and displayed the result.

```python
subtraction = np.abs(
    im1arr.astype(np.int16) -
    im2arr.astype(np.int16)
)
```

This shows the differences between the two images.

### 2. Adding a Constant Value

I added a constant value of `175` to one of the images.

```python
addition_175 = np.clip(
    im1arr.astype(np.int16) + 175,
    0,
    255
)
```

This makes the image brighter because the pixel values are increased.

### 3. Set Difference

I applied a difference operation between the two grayscale images.

```python
set_difference = np.abs(
    im1arr.astype(np.int16) -
    im2arr.astype(np.int16)
)
```

The result shows the difference between the pixel values of the two images.

### 4. Symmetric Difference

I used the XOR operation for the symmetric difference.

```python
symmetric_difference = np.bitwise_xor(
    im1arr,
    im2arr
)
```

This compares the binary representation of the pixel values of the two images.

### 5. Intersection

I used the AND operation for the intersection.

```python
intersection = np.bitwise_and(
    im1arr,
    im2arr
)
```

This performs a bitwise AND between the two image arrays.

## Result

After completing the tasks, I was able to see how changing sampling and quantization affects an image. I also practiced different arithmetic and logical operations between two images.

This lab helped me understand how images can be represented as arrays and how NumPy can be used to perform operations directly on image pixels.

## Files Used

```text
lena_gray_256.tif
cameraman.tif
```

## Tools

```text
Python
Jupyter Notebook
NumPy
Matplotlib
Pillow
OpenCV
```
