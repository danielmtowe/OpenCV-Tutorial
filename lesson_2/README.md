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

When I run the code, a new window will open with zebra Photo. (FYI, the photo above was taken by me; use the photo you took to reverse the code.) The image can be read using the cv2.imread() function. The cv2.imshow() function outputs the read picture to the screen. When you press any key on the keyboard, the window disappears. If there is no cv2.waitKey() in the code, the window will appear and then disappear. This is because cv2.wiatKey() does the ability to pop up a photo until a key is entered. After you've entered the key, use cv2.destroyAllWindows() function to turn off all window windows.


Let's now print a black-and-white image. cv2 as a parameter of cv2.imread (). When you pass an IMREAD_GRAYSCALE, it is imported as a black and white image. The code below is the same as the code above and cv2.IMREAD_GRAYSCALE is only used as a parameter.

cv2.imread(path, flag)
path: image file pathflag
: Set
how images are read - cv2.IMREAD_COLOR (default): Imports as a color image. Ignores the transparency (alpha value).
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
<div style="text-align: justify">
The photo file I read is placed in a variable called img when I run the cv2.imread() function in the previous code. You can save a photo file contained in the img variable to your own PC by calling the cv2.imwrite() function. The code that reads the original color file, zebra.jpg, converts it to gray, and saves the gray photo as zebra_gray.jpg is shown below.
</div>


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

cap = cv2.VideoCapture(video_file) # Create a video capture object
if cap.isOpened(): # Check capture object initialization
     while True:
         ret, img = cap.read() # Read next frame
         if ret: # frame read normal
             cv2.imshow(video_file, img) # Display on screen
             cv2.waitKey(25) # 25ms delay (assume 40fps)
         else: # Unable to read next frame,
             break # finished playing
else:
     print("can't open video.") # Failed to initialize capture object
cap.release() # Release capture resource
cv2.destroyAllWindows()
```

cv2. VideoCapture(video file) reads the first frame of a movie file and saves it to the capture object cap. It should be noted that the complete video is not included in the cap. It just contains the video's initial frame. cap.isOpened() checks whether the cap object has been successfully initialized to the supplied file. If initialization is successful, returns True; otherwise, returns False. In an infinite loop, call cap.read() to read frames from the file in sequence. If you read the frame correctly, ret will be True and img will be the image of the frame. If it is not correctly read, ret is False and image is None. If the next frame read fails, there is an issue with the file or device, or the file has reached its conclusion. To display the frame image on the screen, use cv2.imshow(video file, img). The video file argument of imshow is the title of the window that displays on the screen, and the img argument is the frame image object to display on the screen. After all of the code has been completed, the resource must be returned by calling the cap.release() function.


The above code is simple to understand if you consider a video to be the total of multiple frame images. Does it look like a moving video when you show a fractured frame image in rapid succession? The code above also works by displaying a single frame image in real time. The frame would skip too fast to be visible without the cv2.waitKey(25) function. However, after a 25ms delay, each frame is presented on the screen, allowing us to watch the film. Latency is the value returned by cv2.waitKey(). If you enter a number less than 25, the video appears to play quicker, and if you enter a number more than 25, the video appears to play slowly.


### Reading camera (webcam) frames
You can read live videos with your webcam in addition to the video files that have already been recorded. You can run the code below if your laptop or PC has a webcam. When you run the code below, you will see a window where you can watch yourself through camera.

```
# read camera (webcam) frame (video_cam.py)

import cv2

cap = cv2.VideoCapture(0) # Connect camera device number 0
if cap.isOpened(): # Check capture object connection
     while True:
         ret, img = cap.read() # read next frame
         if ret:
             cv2.imshow('camera', img) # Show next frame image
             if cv2.waitKey(1) != -1: # Wait for key input for 1ms
                 break # Stop on any key input
         else:
             print('no frame')
             break
else:
     print("can't open camera.")
cap.release() # Release resource
cv2.destroyAllWindows()
```


It's nearly identical to the video frame execution code. The distinction is that cv2.VideoCapture(0) and cv.waitKey(1)!= -1. To begin, cv2. VideoCapture() accepts the path to the video file as a parameter, but it also accepts the camera device number. Entering the movie file's path returns the capture object for that movie, whilst entering the camera device number associates it with the webcam. Camera device numbers begin with 0. If you just have one webcam, the parameter can be set to 0.


When reading a frame from the camera, unlike reading a video file, there is no set end to the file and no condition to leave the infinite loop. If the user pushes any key in the cv.waitKey(1)!= -1 code, the loop is broken and exited. If there is no key input for the specified duration, the cv2.waitKey() function returns -1. Any key you enter will result in a break because -1 is not returned.


### Take a photo with your webcam
You can also save an image of a specific frame from your camera or video. You can use the cv2.imwrite() function to save a specified frame. The code below displays a frame on the screen using a webcam and then saves the frame as an image file by pressing any key. It's the equivalent of taking a selfie with your camera.

```
# Take a picture with a webcam (video_cam_take_pic.py)

import cv2

cap = cv2.VideoCapture(0) # Connect camera 0
if cap.isOpened() :
     while True:
         ret, frame = cap. read() # read camera frame
         if ret:
             cv2.imshow('camera',frame) # Show frame on screen
             if cv2.waitKey(1) != -1: # press any key
                 cv2.imwrite('photo.jpg', frame) # Save the frame to 'photo.jpg'
                 break
         else:
             print('no frame!')
             break
else:
     print('no camera!')
cap.release()
cv2.destroyAllWindows()

```

When you run the above code, the webcam will be activated and you will be able to see yourself on the screen. When you press a key, the current frame is taken and saved as an image.


### Recording with a webcam

I found out that you can save a single frame from your webcam as an image, just like when you take a selfie. cv2. The VideoWriter() function can also be used to save several frames as a movie.

cv2. In VideoWriter (file path, fourcc, fps, width, height), file path is the path to the movie file, fourcc is the video encoding format (codec information), fps is the number of frames to be stored per second, and width and height are the width and height of the frames. If you run the code below and press any key, all the frames before you pressed the key are saved as a movie called record.avi.

```
# Record with webcam (video_cam_rec.py)

import cv2

cap = cv2.VideoCapture(0) # Connect camera 0
if cap.isOpened:
    file_path = './record.avi' # File path name to save
    fps = 30.0 # FPS, frames per second
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # Encoding format character
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height)) # frame size
    out = cv2.VideoWriter(file_path, fourcc, fps, size) # Create a VideoWriter object
    while True:
        ret, frame = cap. read()
        if ret:
            cv2.imshow('camera-recording',frame)
            out.write(frame) # Save the file
            if cv2.waitKey(int(1000/fps)) != -1:
                break
        else:
            print("no frame!")
            break
    out.release() # close the file
else:
    print("can't open camera!")
cap.release()
cv2.destroyAllWindows()
```


cv2. I constructed a VideoWriter() object and placed it in the out variable. When out.write(frame) is used, the current frame is saved.

This function examines the attributes of a video or camera. cv2.CAP_PROP_FRAME_WIDTH represents the frame width, while cv2.CAP_PROP_FRAME_HEIGHT represents the frame height. Therefore, cap.get(cv2.CAP PROP FRAME WIDTH) gets the object's frame width.

Note that FPS stands for frames per second, and FPS can be used to obtain latency.

```
Latency = 1000 / fps
```

The reason 1000 is calculated is because 1 second (1s) is 1,000 milliseconds (1,000 ms). The code then sets the latency to cv2.waitKey(int(1000/fps)).
