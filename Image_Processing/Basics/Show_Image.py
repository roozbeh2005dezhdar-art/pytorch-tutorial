import cv2
import os

# The image is likely in the same folder as the script
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'image.jpg')

print(f"Looking for image at: {image_path}")
img_color = cv2.imread(image_path)

if img_color is None:
    print(f"ERROR: Could not load image from {image_path}")
    print(f"Files in script folder: {os.listdir(script_dir)}")
    exit()

cv2.imshow('Window Title', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()