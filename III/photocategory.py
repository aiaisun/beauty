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
import sys
import json


cup = dlib.fhog_object_detector("output/cup")
forestPark = dlib.fhog_object_detector("output/forestPark")
waterNang = dlib.fhog_object_detector("output/waterNang")
yehliu = dlib.fhog_object_detector("output/yehliu")
turtleIsland = dlib.fhog_object_detector("output/turtleIsland")
detectors = [cup, forestPark, waterNang, yehliu, turtleIsland]
detectorList = ["cup", "forestPark", "waterNang", "yehliu", "turtleIsland"]
photoDetectorList = []
for imgPath in paths.list_images("spot/test1"):

    #load image
    # print(imgPath)
    image = dlib.load_rgb_image(imgPath)
    
    #show detector
    [boxes, confidences, detector_idxs] = dlib.fhog_object_detector.run_multiple(detectors, image, upsample_num_times=1, adjust_threshold=0.0)
    detectorName = detectorList[detector_idxs[0]]
    
    # add in list
    photoDetectorList.append(detectorName)
    # print("detector '{}' found box {} with confidence {}.".format(detectorName, boxes[0], confidences[0]))
    
# result = {
#     "From" : sys.argv[2]
# }
str1 = "1"

photoDetectorList_json = json.dumps(photoDetectorList)
photoDetectorList_json2 = json.dumps(str1)
print(str(photoDetectorList_json))
# print('{"a":123}')
sys.stdout.flush()