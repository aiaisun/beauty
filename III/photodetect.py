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

# imgPath = "spot/test2/forestPark.jpg"
imgPath = sys.argv[1]
image = dlib.load_rgb_image(imgPath)

#show detector
[boxes, confidences, detector_idxs] = dlib.fhog_object_detector.run_multiple(detectors, image, upsample_num_times=1, adjust_threshold=0.0)
detectorName = detectorList[detector_idxs[0]]

result = {
    "Name" : detectorName,
    "photoPath" : imgPath
}
with open("spot/{}.json".format(detectorName),"r") as f:
    data = json.load(f)
resultjson = json.dumps(data)
print(str(resultjson))
# print('{"a":123}')
sys.stdout.flush()