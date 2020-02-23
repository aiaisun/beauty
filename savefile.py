#匯入必要的library
from __future__ import print_function
from imutils import paths
from scipy.io import loadmat
from skimage import io
import argparse
import dlib
import cv2
import re
import os


cup = dlib.fhog_object_detector("output/cup")
forestPark = dlib.fhog_object_detector("output/forestPark")
waterNang = dlib.fhog_object_detector("output/waterNang")
yehliu = dlib.fhog_object_detector("output/yehliu")
turtleIsland = dlib.fhog_object_detector("output/turtleIsland")
detectors = [cup, forestPark, waterNang, yehliu, turtleIsland]
detectorList = ["cup", "forestPark", "waterNang", "yehliu", "turtleIsland"]


#define user
num += 1
usr = "user{}".format(num)
print(usr)

for imgPath in paths.list_images("spot/test1"):

    #load image
    print(imgPath)
    image = dlib.load_rgb_image(imgPath)
    
    #show detector
    [boxes, confidences, detector_idxs] = dlib.fhog_object_detector.run_multiple(detectors, image, upsample_num_times=1, adjust_threshold=0.0)
    detectorName = detectorList[detector_idxs[0]]
    
    ########todo!!!!! no detetor save to others
    
    #create folder
    os.makedirs("{}/{}".format(usr, detectorName))
    
    #save image
    img = io.imread(imgPath)
    io.imsave("{}/{}/{}.jpg".format(usr, detectorName, detector_idxs[0]),img)
    print("detector '{}' found box {} with confidence {}.".format(detectorName, boxes[0], confidences[0]))
