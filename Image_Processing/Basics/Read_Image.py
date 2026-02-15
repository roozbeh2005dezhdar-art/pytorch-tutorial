import cv2

# Read image
img = cv2.imread('image.jpg')

# Check if loaded
if img is None:
    print("Error: Image not found")
    exit()

print(f"Image loaded: {img.shape}")
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()