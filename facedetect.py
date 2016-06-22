from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import cv2
import sys
import numpy as np
import argparse
import imutils
import cv2
import shutil

# Get user supplied values
# imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="path to images directory")
args = vars(ap.parse_args())

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# loop over the image paths
imagePaths = list(paths.list_images(args["images"]))

# faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for imagePath in imagePaths:
    # Read the image
    image = cv2.imread(imagePath)
    image1 = imutils.resize(image, width=min(2048, image.shape[1]))
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    # faces = faceCascade.detectMultiScale(
    #     gray,
    #     scaleFactor=1.05,
    #     minNeighbors=3,
    #     minSize=(30, 30),
    #     flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    # )

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=6
    )

    # print "Found {0} faces!".format(len(faces))



    filename = imagePath[imagePath.rfind("/") + 1:]
    print(filename)
    print("Found faces={0} ".format(len(faces)))

    if len(faces) > 0:
        shutil.move(imagePath, "people/" + filename)
 
    # Draw a rectangle around the faces
    #for (x, y, w, h) in faces:
     #   cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # cv2.imshow("Faces found", image)
    # cv2.waitKey(0)
