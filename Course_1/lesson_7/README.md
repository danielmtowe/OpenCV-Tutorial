## OpenCV_LS7_Thresholding, Otsu's Method

In this article, we will examine a common technique for creating binary images: thresh holding.

#### Thresholding
Thresh holding is the most prevalent method for generating binary pictures. A binary image consists of only black and white pixels. Thresh holding is the process of splitting numerous values into two classes depending on a threshold.




#### Global Thrashholding
Global rescheholding is the process of setting a threshold and then designating it as 255 if the pixel value exceeds the threshold or 0 if it does not exceed the threshold. This can be accomplished using numpy, but it can also be implemented using the cv2.threshold() function in OpenCV. I will demonstrate how to execute a global threshholding operation using numpy and the cv2.threshold() function.


```
# global threshold (threshold.py)

import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE) #Read image in grayscale

# Create binary image with NumPy API
thresh_np = np.zeros_like(img) # A zero-padded image of the same size as the original
thresh_np[img > 127] = 255 # change only values greater than 127 to 255

# Create binary image with OpenCV API
ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
print(ret) # 127.0, return the threshold used for the binary image

# Output the original and output to matplotlib
imgs = {'Original': img, 'NumPy API':thresh_np, 'cv2.threshold': thresh_cv}
for i , (key, value) in enumerate(imgs.items()):
     plt.subplot(1, 3, i+1)
     plt.title(key)
     plt.imshow(value, cmap='gray')
     plt.xticks([]); plt.yticks([])

plt.show()
```
First, read the grayscale gradient image that changes gradually from black to white. Initially, I used numpy to replace the pixel value with 127 if it was larger than 255 and 0 if it was less than or equal to 127. The end product is the Numpy API. This is accomplished by using the cv2.threshold(img, 127, 255, cv2. This is also possible using the THRESH BINARY) function. The cv2.threshold() function is utilized as follows:

```
- ret, out = cv2.threshold(img, threshold, value, type_flag)
- img: image
- to convert: threshold: thrashholding
- thresholdvalue: value to apply to pixels that meet the threshold criteria
- type_flag: how to apply thrashholding
- THRESH_TOZERO: Keep the original value if the pixel value exceeds the threshold, specify 0 if it does not exceed cv2.
- THRESH_TOZERO_INV: cv2. Opposition
- to THRESH_TOZERO
```

The function gives two results: the threshold used for threshholding (ret) and the binary image after threshholding (out). The majority of the time, the initial result, ret, corresponds to the threshold parameter.

Below is an example of multiple type flag usage. Note that 255 is white and 0 is black.

```
# Threshold flag (threshold_flag.py)

import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

_, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, t_bininv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, t_truc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, t_2zrinv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

imgs = {'origin':img, 'BINARY':t_bin, 'BINARY_INV':t_bininv, \
         'TRUNC':t_truc, 'TOZERO':t_2zr, 'TOZERO_INV':t_2zrinv}
for i, (key, value) in enumerate(imgs.items()):
     plt.subplot(2,3, i+1)
     plt.title(key)
     plt.imshow(value, cmap='gray')
     plt.xticks([]); plt.yticks([])
    
plt.show()
```

Depending on the type_flag parameters, you can see that various results have been derived.

#### Oats' Heterogeneous Algorithm

Setting a threshold is the most crucial aspect in creating a binary image. Nobuyuki Otsu discovered in 1979 a method for locating the threshold without repeated efforts. This is Otsu's approach for binaryization. The algorithm of Oats sets a threshold at random, divides the pixels into two groups, and repeats the operation of determining the contrast distribution of the two classes; it selects the threshold value of the two classes of contrast distributions when they are the most uniform among all the numbers. In the example provided below, the image is most distinct when the threshold is between 120 and 140.

The OpenCV function enables the application of the Oats algorithm. The final parameter of the cv2.threshold() method is cv2. You only need to pass the THRESH OTSU. Oats' algorithm determines the optimal threshold, hence the value of the threshold parameter passed to the cv2.threshold() function is irrelevant. Because it is ignored regardless.

Listed below is an example of code that employs Oats' threshold-finding technique.


```
Threshold holding using Otsu's algorithm (threshold_otsu.py)

import cv2
import numpy as np
import matplotlib.pylab as plt

# read the image in grayscale
img = cv2.imread('../img/scaned_paper.jpg', cv2.IMREAD_GRAYSCALE)
# Set the boundary value to 130 ---①
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
# Select OTSU algorithm without specifying boundary value ---②
t, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('otsu threshold:', t) # print threshold value selected by Otsu algorithm

imgs = {'Original': img, 't:130':t_130, 'otsu:%d'%t: t_otsu}
for i , (key, value) in enumerate(imgs.items()):
     plt.subplot(1, 3, i+1)
     plt.title(key)
     plt.imshow(value, cmap='gray')
     plt.xticks([]); plt.yticks([])

plt.show()
```

The original image has unclear text. When I turned it to a binary image, though, the text became slightly more legible. The image on the far left is the original, the second image is the binary image with a threshold of 130, and the third image is the binary image after Oats' technique has been applied. We can see that, according to Oats' method, the ideal threshold is 131. (Otsu:131 is labeled at the top of the third image) The following code implements Otsu's algorithm.

```
t, t_otsu = cv2.threshold(img, -1, 255,  cv2.THRESH_BINARY | cv2.THRESH_OTSU) 
```
The second parameter, -1, is the threshold-passing value. As previously described, Oats' algorithm disregards this value, therefore it makes no difference what you put in it.

While Oats' approach has the advantage of automatically determining the appropriate threshold, it is slow because the number of examples must be examined for each case.

#### Adaptive Thrashholding
The above-described worldwide thrashholding does not always perform well. If the source image contains inconsistent illumination or different backdrop colors, it may be difficult to construct a binary image with a single threshold that is clear. Adaptive thresholding, which is given by the following function, requires dividing the image into numerous sections and using only the pixel values surrounding them to determine the threshold.


- cv2.adaptiveThreshold(img, value, method, type_flag, block_size, C)img: input image
value: value
to be applied to pixels that meet the thresholdmethod: method of determining the threshold type_flag: method
of applying thresiholding (same as cv2.threshod())block_size: size of neighbors to be divided into regions (n x n), odd C
: constant to be subtracted from the calculated threshold result (negative)


The method values consist of the following:

cv2. ADAPTIVE THRESH MEAN C: Indicated

by the mean of surrounding pixelscv2. Determined by the sum of the weights according to the Gaussian distribution.


The code below demonstrates an application of adaptive thrashholding.

```
# Apply adaptive thresholding (threshold_adapted.py)

import cv2
import numpy as np
import matplotlib.pyplot as plt

blk_size = 9 # block size
C = 5 # Subtraction constant
img = cv2.imread('../img/sudoku.png', cv2.IMREAD_GRAYSCALE) # read in grayscale

# ---① Apply a single boundary value to the entire image with Otsu's algorithm
ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# ---② Applied adaptive threshold as mean and Gaussian distribution respectively
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,\
                                      cv2.THRESH_BINARY, blk_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                     cv2.THRESH_BINARY, blk_size, C)

# ---③ Output the result to Matplot
imgs = {'Original': img, 'Global-Otsu:%d'%ret:th1, \
        'Adapted-Mean':th2, 'Adapted-Gaussian':th3}
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2,2,i+1)
    plt.title(k)
    plt.imshow(v,'gray')
    plt.xticks([]),plt.yticks([])

plt.show()
```

The upper right corner is a binary image with Oats' algorithm's global thresholding applied. Lower left became black and upper right became white, making it more difficult to recognize the image. This occurs when the bottom left of the original image is darker and more shaded than the top right. This is a regular issue with global garbage collection. With adaptive thrashholding, however, the two binary images below are extremely distinct. The Adapted-Mean distribution is more precise than the Adapted-Gaussian distribution, which has certain flaws; nevertheless, the Gaussian distribution has slightly less precision but fewer flaws than the mean value.

In the preceding example, the adaptive threshholding algorithm is as follows: First, create a total of nine blocks for the image. You can divide the image into nine equal halves. Next, establish a threshold for each block. At the moment, cv2 If you specify ADAPTIVE THRESH MEAN C as a parameter, the threshold is calculated as the mean of the pixels around each block. cv2. If the ADAPTIVE THRESH GAUSSIAN C option is used, the threshold is set to the sum of the weights based on the Gaussian distribution. Based on a predetermined threshold, we discard hold for each block. In doing so, results are more distinct and uniform than when global threscheHolding is performed.



Most photographs contain shadows or light variations. Therefore, adaptive thrashholding is utilized more frequently than global thrashholding.