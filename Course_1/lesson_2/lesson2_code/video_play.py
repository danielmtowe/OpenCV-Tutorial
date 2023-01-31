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