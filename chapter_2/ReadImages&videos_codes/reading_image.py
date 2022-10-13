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