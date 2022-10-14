## OpenCV_lesson4 Managing windows and handling events

This post will demonstrate how to manage windows as well as handle keyboard and mouse events.

#### Managing windows

Let's begin by examining the five functions that handle windows.

The function cv2.namedWindow(winname, flags) creates a window with the name winname. The stipulations are as follows:

winname: window name

flags: used as a window separator window choice (cv2. WINDOW NORMAL: The user can resize the window; cv2. WINDOW AUTOSIZE: The window cannot be resized to the same size as the image)

Using the cv2.moveWindow(winname, x, y) method, the window can be moved to the specified place.

winname: window name

to change location x, y: new location (x, y coordinates)


The cv2.resizeWindow(winname, width, height) function resizes the winname window to the specified width and height (width, height).

Invoking cv2.destroyWindow(winname) closes the window associated with winname.

The function cv2.destroyAllwindows() dismisses all active windows.

The code example below utilizes the five functions listed above. It produces a window with the name 'origin' and the color gray to indicate how to move, resize, and close the window. Please review the remarks.

```
# window management (win.py)

import cv2

file_path = '../img/yeosu.jpg'
img = cv2.imread(file_path) # read image as default
img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE) # read image in grayscale

cv2.namedWindow('origin') # Create window with name origin
cv2.namedWindow('gray', cv2.WINDOW_NORMAL) # Create window with name gray
cv2.imshow('origin', img) # show image in origin window
cv2.imshow('gray', img_gray) # gray display image in window

cv2.moveWindow('origin', 0, 0) # change window position
cv2.moveWindow('gray', 100, 100) # change window position

cv2.waitKey(0) # Press any key
cv2.resizeWindow('origin', 200, 200) # Resize window (not changed)
cv2.resizeWindow('gray', 100, 100) # Resize window (changed))

cv2.waitKey(0) # Press any key
cv2.destroyWindow("gray") # gray close the window

cv2.waitKey(0) # Press any key
cv2.destroyAllWindows() # Close all windows

```

#### Handling keyboard events

Let's now examine how to process keyboard events. The cv2.waitKey(delay) function, which we have already utilized, halts the program for delay milliseconds and returns the key hit on the keyboard. Returns -1 if there is no keyboard input for the dalay time. The default value of delay is 0, which means keyboard input would be awaited forever.

The code below displays an image of Yeosu Bambada on the screen, and hitting the h, j, k, and l keys moves the image by 10 pixels to the left, right, top, and bottom, respectively. Using esc or q to close the window.


```
# Handle key events (event_key.py)

import cv2

img_file = "../img/yeosu.jpg"
img = cv2.imread(img_file)
title = 'IMG' # window name
x, y = 100, 100 # initial coordinates

while True:
     cv2.imshow(title, img)
     cv2.moveWindow(title, x, y)
     key = cv2.waitKey(0) & 0xFF # Wait for keyboard input indefinitely, 8-bit masking
     print(key, chr(key)) # keyboard input value, print character value
     if key == ord('h'): # 'h' key to move left
         x -= 10
     elif key == ord('j'): # If 'j' key, move down
         y += 10
     elif key == ord('k'): # If 'k' key, move up
         y -= 10
     elif key == ord('l'): # 'l' key to move right
         x += 10
     elif key == ord('q') or key == 27: # quit if 'q' or 'esc'
         break
         cv2.destroyAllWindows()
     cv2.moveWindow(title, x, y ) # Move window to new coordinates
```

#### Handling mouse events

The cv2.setMouseCallback(windowName, onMouse, param=None) function can handle mouse events. The parameters are as follows:

windowName: the name of a window

to register the onMouse event, a pre-defined mouse callback method for handling the event must be declared.



The onMouse(evnet, x, y, flags, param) callback function manages mouse events and mouse coordinates. In this case, the event includes mouse movement, left button press, left button release, right button press, right button release, double-clicking the left button, scrolling the wheel, etc. cv2. There are twelve events beginning with EVENT_. (Example: cv2. EVENT MOSEMOVE: mouse movement; cv2. EVENT LBUTTONDOWN: left button push) Flags enable you to handle events as though you were holding down keys such as controls, shifts, and alts. Even if you do not use flags and param, you must include them in the definition of your callback function. Otherwise, you will get an error.



After executing the code below, clicking the mouse will cause a black circle to be drawn on the screen.

```
# Draw a circle with mouse events (event_mouse_circle.py)

import cv2

title = 'mouse event' # window title
img = cv2.imread('../img/blank_500.jpg') # read white image
cv2.imshow(title, img) # show white image

def onMouse(event, x, y, flags, param): # Implement the amuse callback function ---①
     print(event, x, y, ) # print parameters
     if event == cv2.EVENT_LBUTTONDOWN: # If the left button is pressed ---②
         cv2.circle(img, (x,y), 30, (0,0,0), -1) # Draw a black circle with a diameter of 30 at the coordinates
         cv2.imshow(title, img) # Display the drawn image again ---③

cv2.setMouseCallback(title, onMouse) # Register the mouse callback function in the GUI window ---④

while True:
     if cv2.waitKey(0) & 0xFF == 27: # exit with esc
         break
cv2.destroyAllWindows()
```

Use flags in the following code. These are the arguments supplied to flag:

- cv2.EVENT_FLAG_CTRLKEY(8): Ctrl presses
- cv2.EVENT_FLAG_SHIFTKEY (16): Shift-press event.
- cv2. EVENT_FLAG_ALTKEY (32): Press Alt

As illustrated in the preceding code, a black circle is drawn when the mouse is clicked. When the control and shift keys are simultaneously pushed and the mouse is clicked, a green circle is drawn; when the control key is pressed and the mouse is clicked, a red circle is created; and when the shift key is pressed and the mouse is clicked, a blue circle is drawn.

```
# Draw a circle using flags (event_mouse_circle_flag.py)

import cv2

title = 'mouse event' # window title
img = cv2.imread('../img/blank_500.jpg') # read white image
cv2.imshow(title, img) # show white image

colors = {'black':(0,0,0),
         'red' : (0,0,255),
         'blue':(255,0,0),
         'green': (0,255,0) } # predefined color

def onMouse(event, x, y, flags, param): # Implement the amuse callback function ---①
    print(event, x, y, flags) # print parameters
    color = colors['black']
    if event == cv2.EVENT_LBUTTONDOWN: # If the left button is pressed ---②
        # When both the control key and the shift key are pressed
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY :
            color = colors['green']
        elif flags & cv2.EVENT_FLAG_SHIFTKEY : # if shift key is pressed
            color = colors['blue']
        elif flags & cv2.EVENT_FLAG_CTRLKEY : # if control key is pressed
            color = colors['red']
        # Draw a black circle with a diameter of 30 at the coordinates
        cv2.circle(img, (x,y), 30, color, -1)
        cv2.imshow(title, img) # Display the drawn image again ---③

cv2.setMouseCallback(title, onMouse) # Register the mouse callback function in the GUI window ---④

while True:
    if cv2.waitKey(0) & 0xFF == 27: # exit with esc
        break
cv2.destroyAllWindows()
```


If you press the control flags & cv2.EVENT_FLAG_CTRLKEY returns True.

You have just learnt how to manage windows and handle mouse and keyboard events.