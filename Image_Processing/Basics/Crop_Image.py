import cv2

img = cv2.imread('image.jpg')
if img is None:
    print("Error: Image not found")
    exit()

# Crop [y1:y2, x1:x2]
cropped = img[50:200, 100:300]  # rows 50-200, columns 100-300

cv2.imshow('Cropped', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()