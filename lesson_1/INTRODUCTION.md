## OpenCV - 1. Overview and installation of OpenCV

In this post, we'll learn about OpenCV, the leading computer vision library. Before we get there, let's review image processing and computer vision.


### Image Processing and Computer Vision
Image processing is the application of multiple operations to an image in order to achieve the desired result. Most image processing is done to improve the quality of a video. Improving image quality, restoring images, and splitting images are all examples of image processing.


Computer vision is a broad concept that includes image processing. While image processing technology transforms the original image into the desired new image, computer vision technology extracts meaningful information from the image. Object detection, tracking, and recognition are some examples. Object detection is the task of determining where the object in the image that you are looking for is located, object tracking is the task of determining where the object in the image is moving, and object recognition is the task of determining what the object in the image is.


Object tracking is roughly understandable, but object detection and object recognition can be confusing. Consider object recognition as the task of showing a picture of a dog and determining whether it is a private cat or a cat. On the other hand, think of object detection as showing a picture of multiple dogs and cats and determining where the dog is located. Object recognition is a private cat, but object detection is a more difficult task because you must locate the dog within the image.

In general, image processing is often performed before computer vision because computer vision is the process of replacing the original image with the desired new image through image processing and then using computer vision to obtain the desired information. Above, I briefly discussed image processing and computer vision. Let's take a look at OpenCV, a leading image processing and computer vision library.

### What is OpenCV?
The OpenCV acronym stands for the Open Source Computer Vision Library, which is the most well-known library in the fields of image processing and computer vision. If you think of OpenCV as a library that allows you to implement Photoshop features that process photos or videos in a programming language, you'd be correct. The OpenCV source code repository is divided into two sections:

Main repository: https://github.com/opencv/opencv

Extra Repository: https://github.com/opencv/opencv_contrib

The main repository is the official repository for the distribution of OpenCV. Extra storage, on the other hand, is a repository containing code that is still in its infancy compared to the algorithm. As maturity grows, code in the Extra repository will be moved to the main repository.

### Installing OpenCV
Now let's install OpenCV

I'll start by creating a virtual environment. Because I have Anaconda installed on my PC, I used conda to create a virtual environment.

Let's use this code to create a virtual environment.
First, it makes a virtual environment that has Python version 3.9. Just type the following into the Anaconda Prompt.

```
# Create a virtual environment in Anaconda
conda create -n opencv python=3.9
```

A virtual environment called opencv has been created, with Python 3.9 installed. As shown below, run the virtual environment you created in this manner.

```
# Run a virtual environment
conda activate opencv
```

Install the desired version of the module inside the virtual environment.

```
# Install numpy, opencv and matplotlib 
pip3 install numpy
pip3 install opencv-contrib
pip3 install matplotlib
```

Now, type python in the command prompt window as shown below to view the version of each module.

```
>>> import numpy
>>> numpy.__version__

>>> import cv2
>>> cv2.__version__

>>> import matplotlib
>>> matplotlib.__version__
```


We have seen an overview of OpenCV as well as how to install it.