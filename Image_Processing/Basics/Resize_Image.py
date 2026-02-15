import cv2

img = cv2.imread('image.jpg')
if img is None:
    print("Error: Image not found")
    exit()

# Resize to specific dimensions (width, height)
resized = cv2.resize(img, (300, 200))

# Or resize by scale factor (0.5 = half size)
# resized = cv2.resize(img, None, fx=0.5, fy=0.5)

cv2.imshow('Resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()