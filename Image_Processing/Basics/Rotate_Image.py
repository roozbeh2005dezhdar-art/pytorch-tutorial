import cv2

img = cv2.imread('image.jpg')
if img is None:
    print("Error: Image not found")
    exit()

# Get image dimensions
h, w = img.shape[:2]

# Get rotation matrix (rotate 45 degrees)
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)  # angle, scale

# Apply rotation
rotated = cv2.warpAffine(img, matrix, (w, h))

cv2.imshow('Rotated 45°', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()