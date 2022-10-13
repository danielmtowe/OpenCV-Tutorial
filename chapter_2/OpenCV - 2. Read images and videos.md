## OpenCV - 2. Read images and videos

The majority of OpenCV work consists of reading an image, performing the appropriate operation, and then outputing or saving the results to a file. In this post, we'll look at OpenCV's first step: image I/O.

Here is the OpenCV code for showing an image on the screen.

Please get the picture file from this page. You can use any of the pictures to learn. It will be more fun if you use your own photos to learn.


```
# Display the image file on the screen (img_show.py)
import cv2

img_file = "images/zebra.jpg"   # Image path to display
img = cv2.imread(img_file)      # Read the image and assign it to the img variable

if img is not None:
   cv2.imshow('image', img)       # Display the read image on the screen
   cv2.waitKey()                # Wait until key is input
   cv2.destroyAllWindows()      # Close all windows
else:
     print('No image file.')

```

When I run the code, a new window will open with the stunning Yeosu Nightsea Photo. (FYI, the photo above was taken by me; use the photo you took to reverse the code.) The image can be read using the cv2.imread() function. The cv2.imshow() function outputs the read picture to the screen. When you press any key on the keyboard, the window disappears. If there is no cv2.waitKey() in the code, the window will appear and then disappear. This is because cv2.wiatKey() does the ability to pop up a photo until a key is entered. After you've entered the key, use cv2.destroyAllWindows to turn off all window windows ().


Let's now print a black-and-white image. cv2 as a parameter of cv2.imread (). When you pass an IMREAD_GRAYSCALE, it is imported as a black and white image. The code below is the same as the code above and cv2. IMREAD_GRAYSCALE is only used as a parameter.

cv2.imread(path, flag)
path: image file pathflag
: Set
how images are read - cv2. IMREAD_COLOR (default): Imports as a color image. Ignores the transparency (alpha value).
- cv2. IMREAD_GRAYSCALE: Loads the image in black and white tones.
- cv2. IMREAD_UNCHANGED: Imports the image as-is, including the transparency (alpha value).


```
# Display image files on screen in gray(img_show_gray.py)

import cv2

img_file = "images/zebra.jpg" 
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)    # read in gray

if img is not None:
  cv2.imshow('IMG', img)
  cv2.waitKey()
  cv2.destroyAllWindows()
else:
    print('No image file.')
```


As shown above, a grayscale photo appears. Next, we'll look at how to save the image.

### Saving an image
The photo file I read is placed in a variable called img when I run the cv2.imread() function in the previous code. You can save a photo file contained in the img variable to your own PC by calling the cv2.imwrite() function. The code that reads the original color file, zebra.jpg, converts it to gray, and saves the gray photo as zebra_gray.jpg is shown below.


```
# Saving the image (image_write.py)

import cv2

img_file = 'images/zebra.jpg'
save_file = 'images/zebra_gray.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img) # Save as file, format depends on extension
cv2.waitKey()
cv2.destroyAllWindows()
```

When I run the above code, I get a gray photo in the images directory called zebra_gray.jpg.

### Reading Video files 

OpenCV can process both photos and videos. The code for reading a video file is provided below. The code below will start a brief animated video.

```
# Read the video file (video_play.py)

import cv2

video_file = "../img/big_buck.avi" # Video file path

cap = cv2.VideoCapture(video_file) # Create a video capture object ---①
if cap.isOpened(): # Check capture object initialization
     while True:
         ret, img = cap.read() # Read next frame --- ②
         if ret: # frame read normal
             cv2.imshow(video_file, img) # Display on screen --- ③
             cv2.waitKey(25) # 25ms delay (assume 40fps) --- ④
         else: # Unable to read next frame,
             break # finished playing
else:
     print("can't open video.") # Failed to initialize capture object
cap.release() # Release capture resource
cv2.destroyAllWindows()
```