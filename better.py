import cv2
import argparse
import os
from datetime import datetime

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Open the video capture
video = cv2.VideoCapture(0)

# Loop through the video frames
while True:
    # Read a frame from the video capture
    check, frame = video.read()

    # If the frame was not read successfully, break the loop
    if frame is None:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame using the face cascade
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

    # Loop through the detected faces
    for x, y, w, h in faces:
        # Draw a rectangle around the face
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # Get the current time and format it for the filename
        current_time = datetime.now().strftime('%Y-%b-%d-%H-%S-%f')

        # Save the image to a file
        cv2.imwrite("face detected" + str(current_time) + ".jpg", img)

    # Display the frame to the user
    cv2.imshow("home sure", frame)

    # Wait for the user to press a key
    key = cv2.waitKey(1)

    # If the user pressed 'q', break the loop
    if key == ord('q'):
        break

# When the loop is finished, release the video capture and destroy all windows
video.release()
cv2.destroyAllWindows()

# Parse the command-line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-ext", "--extension", required=False, default='jpg', help="extension of the images to be used")
ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
args = vars(ap.parse_args())

# Get the directory path and the extension
dir_path = '.'
ext = args['extension']
output = args['output']

# Get the list of image filenames
images = []
for f in os.listdir(dir_path):
    if f.endswith(ext):
        images.append(f)

# Sort the list of filenames
images.sort()

# Get the first image to get the size
image_path = os.path.join(dir_path, images[0])
frame = cv2.imread(image_path)
height, width, channels = frame.shape

# Create the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output, fourcc, 5.0, (width, height))

# Loop through the images and write them to the
