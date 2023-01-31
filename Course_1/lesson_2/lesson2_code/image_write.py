import cv2

img_file = 'images/zebra.jpg'
save_file = 'images/zebra_gray.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img) # Save as file, format depends on extension
cv2.waitKey()
cv2.destroyAllWindows()