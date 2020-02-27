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
photoDetectedList = []

# print('{"a":123}')
# sys.stdout.flush()

imgPaths = sys.argv[1]
imgPaths = imgPaths.split(',')


# imgPaths = [ 'public/tmp_uploads/cup.jpg',
#   'public/tmp_uploads/forestPark.jpg',
#   'public/tmp_uploads/turtleIsland.jpg',
#   'public/tmp_uploads/waterNang.jpg' ]


#define userAlbum
userAlbum = "user{}".format(sys.argv[2])

n = 0
# for imgPath in paths.list_images("spot/test1"):
for imgPath in imgPaths:
    n+=1
    #load image
    image = dlib.load_rgb_image(imgPath)
    
    #show detector
    [boxes, confidences, detector_idxs] = dlib.fhog_object_detector.run_multiple(detectors, image, upsample_num_times=1, adjust_threshold=0.0)
    
    # name dectector
    if not detector_idxs:
        detectorName = "Others"
        
    else:
        if confidences[0] > 0.5:
            detectorName = detectorList[detector_idxs[0]]
        else:
            detectorName =  "Others"

    
    # add in list
    photoDetectedList.append(detectorName)
    # print("detector '{}' found box {} with confidence {}.".format(detectorName, boxes[0], confidences[0]))
    
    #create folder
    folderPath = r"public/user/{}/{}".format(userAlbum, detectorName)
    if not os.path.isdir(folderPath):
        os.makedirs(folderPath) #for linux
    # os.makedirs("public\user\{}\{}".format(userAlbum, detectorName)) for linux
    
    #save image
    img = io.imread(imgPath)
    io.imsave(r"public/user/{}/{}/{}.jpg".format(userAlbum, detectorName, n),img) #for linux
    # io.imsave("public\user\{}\{}\{}.jpg".format(userAlbum, detectorName, detector_idxs[0]),img) #for linux


# count detector num
photoDetectedList2 = list(set(photoDetectedList))

detectorNum = len(photoDetectedList2)


result = {
    "detectorNum" : detectorNum,

}
for detector in photoDetectedList2:
    imgPathList = []
    for imgPath in paths.list_images(r"public/user/{}/{}".format(userAlbum,detector)):
        imgPathList.append(imgPath)

    result[detector] = imgPathList



photoDetectedList_json = json.dumps(result)
# photoDetectedList_json = json.dumps("888") #test
print(str(photoDetectedList_json))
# print('{"a":123}')
sys.stdout.flush()