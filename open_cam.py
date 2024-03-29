import cv2
from send_email import read_photo, send_email
import time

# Initialize the camera
cam = cv2.VideoCapture(0)

current_time = time.time() # Get the current time

# Try to capture a screenshot
ret, frame = cam.read()
if ret:
    # Save the screenshot
    img_name = "Screenshot_0.png"
    cv2.imwrite(img_name, frame)
else:
    print("Failed to grab frame")

# Release and close the camera
cam.release()
cv2.destroyAllWindows()


# Read the photo and send the email
img = read_photo()

send_email(img)


