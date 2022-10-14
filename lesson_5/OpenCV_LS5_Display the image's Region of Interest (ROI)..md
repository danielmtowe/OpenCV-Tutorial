## OpenCV_lesson5 Display the image's Region of Interest (ROI).

This article will demonstrate how to display the Region of Interest (ROI) in an image.

#### To Display a Region of Interest (ROI)

A region of interest (ROI) is a literal region of interest inside a video. This image depicts the sunset. Let's examine how to display the desired portion of a sunset photograph.
When you run the code below, you'll get an image with a green square around the sun.

```
# Display region of interest (roi.py)

import cv2
import numpy as np

img = cv2.imread('./img/sunset.jpg')

x=320; y=150; w=50; h=50 # roi coordinates
roi = img[y:y+h, x:x+w] # Specify roi ---①

print(roi.shape) # roi shape, (50,50,3)
cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0)) # Draw rectangle over roi ---②
cv2.imshow("img", img)

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()
```
The image is returned as a numpy array when the cv2.imread() function is used. Numpy arrays are being sliced. You can slice the picture numpy array to specify the required area. Img[y:y+h, x:x+w] in the preceding code slices the desired area. In other words, the roi variable includes a numpy array that has been sliced to represent the area of interest, which is the sun.

The function cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0) displays a rectangle in the color (0, 255, 0) from (0, 0) to (h-1, w-1) of a roi image with just the solar component sliced. The top left is (0, 0), whereas the bottom right is (h-1, w-1). It draws a rectangle from the bottom right corner, with the top left of the roi picture as a vertex. Green is represented by the RGB value (0, 255, 0).



If you didn't specify a region of interest, roi, the code would be as follows:


```
cv2.rectangle(roi, (x, y), (x+w, y+h), (0,255,0))
```

The following code replicates the provided region of interest in the original image so that it appears as two, or it just appears in a new window.


```
# Duplicate the region of interest and open it in a new window (roi_copy.py)

import cv2
import numpy as np

img = cv2.imread('../img/sunset.jpg')

x=320; y=150; w=50; h=50
roi = img[y:y+h, x:x+w] # specify roi
img2 = roi.copy() # Duplicate roi array ---①

img[y:y+h, x+w:x+w+w] = roi # Add roi to new coordinates, create 2 suns
cv2.rectangle(img, (x,y), (x+w+w, y+h), (0,255,0)) # Display rectangle in 2 sun areas

cv2.imshow("img", img) # print the original image
cv2.imshow("roi", img2) # output only roi

cv2.waitKey(0)
cv2.destroyAllWindows()
```

One more duplicate of the sun from the original image was shown in two, as well as a new window in the upper left corner.

#### Dragging the Mouse to Show a Point of Interest
The coordinates and size (height, width) of the desired area are required to display a region of interest. It is, however, not difficult to enter it numerically every time. Wouldn't dragging the mouse to display the region of interest be more convenient? The code below shows how to save a region of interest specified by dragging the mouse as a file while displaying only the region of interest in a new window.


```
# Designate, mark, and save the region of interest with the mouse (roi_crop_mouse.py)

import cv2
import numpy as np

isDragging = False # Save mouse drag state
x0, y0, w, h = -1,-1,-1,-1 # Save area selection coordinates
blue, red = (255,0,0),(0,0,255) # color value

def onMouse(event,x,y,flags,param): # Mouse event handle function ---①
    global isDragging, x0, y0, img # reference global variable
    if event == cv2.EVENT_LBUTTONDOWN: # Left mouse button down, start dragging ---②
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE: # mouse movement ---③
        if isDragging: # Dragging in progress
            img_draw = img.copy() # Duplicate image for rectangular figure representation
            cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2) # Show drag progress area
            cv2.imshow('img', img_draw) # Outputs the squared figure to the screen
    elif event == cv2.EVENT_LBUTTONUP: # Left mouse button up ---④
        if isDragging: # stop dragging
            isDragging = False
            w = x - x0 # Calculate drag area width
            h = y - y0 # Calculate the height of the drag area
            print("x:%d, y:%d, w:%d, h:%d" % (x0, y0, w, h))
            if w > 0 and h > 0: # if width and height are positive, drag direction is correct ---⑤
                img_draw = img.copy() # Duplicate image to display rectangle drawing in selection
                # mark the red square in the selection area
                cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2)
                cv2.imshow('img', img_draw) # Display the image drawn in the red square
                roi = img[y0:y0+h, x0:x0+w] # Designate only the selected area from the original image as ROI ---⑥
                cv2.imshow('cropped', roi) # Display the ROI specified area in a new window
                cv2.moveWindow('cropped', 0, 0) # Move the new window to the top left corner of the screen
                cv2.imwrite('./cropped.jpg', roi) # Save only the ROI area as a file ---⑦
                print("cropped.")
            else:
                cv2.imshow('img', img) # If the drag direction is wrong, output the original image without a square figure.
                print("Drag the area from the top left to the bottom right.")

img = cv2.imread('../img/sunset.jpg')
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse) # Register mouse event ---⑧
cv2.waitKey()
cv2.destroyAllWindows()
```

I declared a callback function called onMouse() in the preceding code. This callback function divides events into three categories: (1) When the left mouse button is pushed, (2) when it is pressed and dragged, and (3) when it is released. When the left mouse button is pressed, set the variable isDragging to True to remember that the drag has begun, and define the starting position as x0, y0. When you drag while holding down the mouse, the image is copied and displayed as a blue rectangle from (x0, y0) to (x, y) of the replicated image. (x0,y0) is the starting point of the mouse drag, and (x,y) is the current location of the mouse. Finally, when you let go of the left mouse button, isDragging becomes False, the width of the drag area is w, and the height is h. If both w and h are positive, the selected region is highlighted in red and presented in a new window. It also saves photos of specific locations as files. The following is the output of running the code:

However, writing code like this every time you want to indicate a region of interest with the mouse is time-consuming. OpenCV has a function that can help with this. This function lets you specify the area of interest without having to write code to handle mouse events.


ret = cv2.selectROI(win_name, img, showCrossHair=True, fromCenter=False)
win_name: Name
of the window to display the region of interestimg: Image
to display the region of interestshowCrossHair: Whether
to show a cross in the center of the selectionfromCenter: Specify
the starting point of the mouse as the center of the areaRet: the coordinates and size of the selected area (x, y, w, h); Deselection specifies all as 0


To display the selection, the code below employs the cv2.selectROI() function. Drag the area of interest with the mouse and then press Space or Enter to open it in a new window. To cancel, hit 'c' after dragging.

```
# Designate, display, and save the region of interest as selectROI (roi_select_img.py)

import cv2, numpy as np

img = cv2.imread('../img/sunset.jpg')

x,y,w,h = cv2.selectROI('img', img, False)
if w and h:
     roi = img[y:y+h, x:x+w]
     cv2.imshow('cropped', roi) # Display the ROI specified area in a new window
     cv2.moveWindow('cropped', 0, 0) # Move the new window to the top left corner of the screen
     cv2.imwrite('./cropped2.jpg', roi) # Save only the ROI area to a file

cv2.waitKey(0)
cv2.destroyAllWindows()
```
There is a function cv2.imshow ('cropped', roi) in the code above that floats the area of interest in a new window, but no code that pops up the original picture, the img. When I run the code, though, the original image appears as well. This is accomplished with cv2.selectROI ('img', img, false). The cv2.selectROI() function displays the original image, which aids in mouse event management.



## Install Google Chrome Browser on Ubuntu 20.04

You can install Google Chrome browser by downloading the Debian binary package or by simply installing the Chrome sources lists and then installing the Chrome browser from these sources lists.

### Update System Package Cache

Before you can proceed, update your package cache.

```
sudo apt update
```

### Install Google Chrome using DEB Binary Package

Download Google Chrome DEB binary package from Google Chrome page.

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -P /tmp
```

Then install it using APT so as to deal with required dependencies automatically.

```
sudo apt install /tmp/google-chrome-stable_current_amd64.deb
```
Run the code below to see the version of chrome installed 
```
google-chrome --version
```

### Sign in Google Account

Before you can begin to setup Chrome Remote Desktop on Ubuntu 20.04 login to your Google account on your browser using your gmail account.

### Install Chrome Remote Desktop Extension

Next, you navigate to Chrome extensions page and search for Chrome remote desktop.

Click Add to Chrome to install the extension.

After the installation, you should be able to see the Chrome remote desktop icon just beside your search address bar on the right.
### Install Chrome Remote Desktop Package

Next, install Chrome remote desktop package which provides the required host components;

```
wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb -P /tmp
sudo apt install /tmp/chrome-remote-desktop_current_amd64.deb

```

You can as well navigate to the download folder, /tmp, in this case, and run the command;

```
cd /tmp
sudo apt install ./chrome-remote-desktop_current_amd64.deb
```

Enable Remote Desktop Connections

To allow remote access to your Ubuntu 20.04 via Chrome remote desktop tool, you need to enable this by opening the Chrome remote desktop extension or just using the remote desktop access address, https://remotedesktop.google.com/access and clicking TURN ON as shown in the screenshot below;


If you do not see the TURN ON button, simply create the Chrome remote desktop configuration directory on your home directory;

```
mkdir ~/.config/chrome-remote-desktop
```
Once you create the directory, reload the access URL above.

Next, enter the name of your system;
Click Next to set the remote connection PIN. Ensure that the PIN is at least 6 digits.
Once you set the PIN, click START to run Chrome Remote Desktop.

If prompted for authentication to run Chrome remote desktop, authenticate and proceed.
Chrome Remote Desktop is now up and running on your Ubuntu 20.04.
