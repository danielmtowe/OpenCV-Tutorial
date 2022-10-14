# OpenCV-LS6_Image color representation (BGR, HSV, YUV)

We'll look at how OpenCV can represent colors in this post.


#### BGR, BGRA

BGRA, BGR
Colors can be represented in RGB (Red, Green, Blue) format. It's a method of combining three different colors of light: red, green, and blue to achieve the desired color. Each color is represented by a number between 0 and 255, and the higher the number, the brighter the light in that color gets. When RGB = (255, 255, 255), the color is white; when RGB = (0, 0, 0), the color is black. OpenCV, on the other hand, expresses the contrary order in BGR. For example, the RGB value of red is (255, 0, 0), but the BGR value is (0, 0, 255).

RGBA is a color notation that combines RGB and A (alpha, alpha). The letter A represents the background's transparency. A can potentially have values ranging from 0 to 255, but only 0 and 255 are commonly used to represent the background's transparency. A number of 255 represents white, while a value of 0 represents black.

Let's take a look at the example code below. As the second parameter to cv2, use the cv2.imread() function. If you include an IMREAD COLOR, the image will be read in BGR format. cv2. If it is IMREAD UNCHANGED, the picture is read in the BGRA format if it has an alpha channel.

```
# BGR, BGRA, Ahlpha channels (rgba.py)

import cv2
import numpy as np

# default option
img = cv2.imread('../img/opencv_logo.png')
# IMREAD_COLOR option
bgr = cv2.imread('../img/opencv_logo.png', cv2.IMREAD_COLOR)
# IMREAD_UNCHANGED option
bgra = cv2.imread('../img/opencv_logo.png', cv2.IMREAD_UNCHANGED)
# Image shape according to each option
print("default", img.shape, "color", bgr.shape, "unchanged", bgra.shape)

cv2.imshow('bgr', bgr)
cv2.imshow('bgra', bgra)
cv2.imshow('alpha', bgra[:,:,3]) # show only alpha channel
cv2.waitKey(0)
cv2.destroyAllWindows()
```

cv2 is a parameter. There is no distinction between an image that includes IMREAD_COLOR and an image that does not include any parameters. Because the background is black, I can't see the black letters of OpenCV. Furthermore, both the first and second photographs contain forms (240, 195, 3). In contrast, the third image features one more alpha channel, with form (240, 195, 4). The alpha value in the foreground in the third image is 255, whereas the alpha value in the background is 0. This is due to the fact that an alpha value of 255 is white and a value of 0 is black. Unlike the first and second photos, the third image simply shows an alpha channel, allowing you to readily distinguish between foreground and background. As a result, the alpha channel is also known as the mask channel.


#### To Convert BGR Color Image to Grayscale Image

Converting a color image to a grayscale image is critical for increasing performance by lowering the amount of image computation. cv2.imread(img, cv2. IMREAD GRAYSCALE) is the function that reads in grayscale from the start. cv2.imread() as the function cv2's second parameter Simply enter IMREAD GRAYSCALE. However, there are situations when you must read it as a BGR color image first and then convert it to grayscale. This is possible with the cv2.cvtcolor() function. It stands for color conversion.

The code below demonstrates two methods for converting a color image to a grayscale image. The first method is to implement it yourself using the average value, and the second method is to use OpenCV's cv2.cvtcolor() function.

```
# Convert BGR color image to grayscale image (bgr2gray.py)

import cv2
import numpy as np

img = cv2.imread('../img/yeosu.jpg')

img2 = img.astype(np.uint16) # change dtype
b,g,r = cv2.split(img2) # Split by channel
#b,g,r = img2[:,:,0], img2[:,:,1], img2[:,:,2]
gray1 = ((b + g + r)/3).astype(np.uint8) # change dtype after calculating average value

gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # change BGR to grayscale
cv2.imshow('original', img)
cv2.imshow('gray1', gray1)
cv2.imshow('gray2', gray2)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

The gray1 image is a direct implementation of an algorithm that represents it as a grayscale image by using average values. Before I got the average, I adjusted the dtype to unit16. This is because the sum of the three channel values can be more than 255. Change it back to unit8 once you've calculated the average.

The cv2.split(img2) function splits images based on their BGR channel and returns them as a tuple. This is equivalent to numpy slicing. As a result, the two codes below are the same.


```
b, g, r = cv2.split(img2)
b, g, r = img2[:, :, 0], img2[:, :, 1], img2[:, :, 2]
```

However, rather than merely calculating an average, a function can be used to convert a BGR color image to a grayscale image. This can be accomplished by utilizing the cv2.cvtcolor(img, flag) function, which is available in cv2 for the flag parameter. Simply add a COLOR BRG2GRAY.

There are 274 flag parameters in all, however the most commonly used ones are as follows:


- cv2. COLOR_BGR2GRAY: Convert
- BGR color image to grayscale imagecv2. COLOR_GRAY2BGR: Convert
- grayscale images to BGR color imagescv2. COLOR_BGR2RGB: Convert
- BGR color images to RGB color imagescv2. COLOR_BGR2HSV: Convert
- BGR color image to HSV color imagecv2. COLOR_HSV2BGR: Convert
- HSV color images to BGR color imagescv2. COLOR_BGR2YUV: Convert
- BGR color image to YUV color imagecv2. COLOR_YUV2BGR: Convert YUB color images to BGR color images

Later, we'll examine into HSV and YUV. FYI COLOR GRAY2BGR is a parameter that converts a grayscale image to a BGR color image, but it does not replace the grayscale image with a colored one. This means that a 2-D array image is converted to a 3-D array with the identical values in all three channels. If the dimensions of the photos are different, the operation is impossible, so this is the labor required to fit the dimensions.

#### The HSV technique

The HSV technique, like RGB, is a three-channel representation of a color image. H (Hue, Hue), S (Saturation, Saturation), and V are the three channels (Value, Brightness)

It will be easier to grasp if you look at H, S, and V in the image above. The H value indicates the image's color. S represents how pure the colors in the image are. V indicates how light or dark the color is. Color() takes cv2.cvtc2 as the second parameter. If you include a COLOR BGR2HSV, the BGR method will be converted to HSV. When you add a COLOR HSV2BGR, the HSV method is converted to the BGR method. An example code for converting the BGR method to the HSV method is provided below.


```
import cv2
import numpy as np

#---① Create primary color pixels in BGR color space
red_bgr = np.array([[[0,0,255]]], dtype=np.uint8) # Pixels with only red values
green_bgr = np.array([[[0,255,0]]], dtype=np.uint8) # Pixels with only green values
blue_bgr = np.array([[[255,0,0]]], dtype=np.uint8) # Pixels with only blue values
yellow_bgr = np.array([[[0,255,255]]], dtype=np.uint8) # Pixels with only yellow values

#---② Convert BGR color space to HSV color space
red_hsv = cv2.cvtColor(red_bgr, cv2.COLOR_BGR2HSV);
green_hsv = cv2.cvtColor(green_bgr, cv2.COLOR_BGR2HSV);
blue_hsv = cv2.cvtColor(blue_bgr, cv2.COLOR_BGR2HSV);
yellow_hsv = cv2.cvtColor(yellow_bgr, cv2.COLOR_BGR2HSV);

#---③ Output pixels converted to HSV
print("red:",red_hsv)
print("green:", green_hsv)
print("blue", blue_hsv)
print("yellow", yellow_hsv)
```


If a color with BGR is (0, 0, 255) expressed in HSV, it is (0, 255, 255). To figure out the color, the RGB method needs to know the values of all three channels, but the HSV method is more convenient and effective because it only needs to know the H value.


#### YUV and YCbCr methods

The YUV method, commonly known as the YCbCr method, is composed of Y for brightness (Luma), U for brightness and blue color difference (Chroma Blue, Cb), and V for brightness and red color difference (Chroma Red, Cr). It compresses data by allocating a large number of bits to Y (brightness) and a small number of bits to U(Cb) and V. (Cr). The areas of the YUV color picture according to V and U at Y=0.5 are shown below.

An example code for converting BGR values to YUV data is provided below.


```
# Convert BGR value to YUV (bgr2yuv.py)

import cv2
import numpy as np

#---① Create 3 brightness pixels in BGR color space
dark = np.array([[[0,0,0]]], dtype=np.uint8) # Darkest pixel with all 3 channels 0
middle = np.array([[[127,127,127]]], dtype=np.uint8) # Medium brightness pixels with all 3 channels 127
bright = np.array([[[255,255,255]]], dtype=np.uint8) # Brightest pixel for all 3 channels of 255

#---② Convert BGR color space to YUV color space
dark_yuv = cv2.cvtColor(dark, cv2.COLOR_BGR2YUV)
middle_yuv = cv2.cvtColor(middle, cv2.COLOR_BGR2YUV)
bright_yuv = cv2.cvtColor(bright, cv2.COLOR_BGR2YUV)

#---③ Output pixels converted to YUV
print("dark:",dark_yuv)
print("middle:", middle_yuv)
print("bright", bright_yuv)
```


BGR values are (0, 0, 0), (127, 127, 127), (255, 255, 255), which are the darkest pixels, medium brightness pixels, and brightest pixels. If you convert it to the YUV way, you get (0, 128, 128), (127, 128, 128), (255, 128, 128), respectively. The very first value, Y, means brightness. The second and third values are the same, but only the Y values are replaced with 0, 127, and 255. In other words, you can see the conversion from a dark value to a light one. If you need to pay more attention to brightness, it might be wiser to use the YUV method than the BGR method, right?


In summary, there are four methods for expressing colors in OpenCV: BGR, BGRA, HSV, and YUV. The BGR approach is similar to the RGB method, except that the order is reversed. The BGRA method is the addition of an A (alpha) value to the BGR method to show transparency. The HSV approach expresses color by using hue, saturation, and brightness, thus if you only know H, you can grasp the hue to a certain amount. So, if you want to know the hue quickly, utilize the HSV approach. If you need to pay close attention to brightness, the YUV technique is ideal.