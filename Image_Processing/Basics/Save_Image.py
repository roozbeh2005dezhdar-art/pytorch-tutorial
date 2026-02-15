import cv2

# Load image first
img = cv2.imread('image.jpg')
if img is None:
    print("Error: Image not found")
    exit()

# Save image
success = cv2.imwrite('output.png', img)

if success:
    print("Image saved as output.png")
else:
    print("Save failed")