#匯入必要的library
from __future__ import print_function
from imutils import paths
from scipy.io import loadmat
from skimage import io
import argparse
import dlib
import cv2
import re
 
#讀入相關的參數
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--class", required=True, help="Path to the CALTECH-101 class images")
args = vars(ap.parse_args())

options = dlib.simple_object_detector_training_options()
images = [] #存放相片圖檔
boxes = [] #存放Annotations
 
#依序處理path下的每張圖片

for imagePath in paths.list_images(args["class"]):
    #從圖片路徑名稱中取出ImageID
    imageID = imagePath[imagePath.rfind("/") + 1:]
    img = cv2.imread(imagePath)
    left, top, height, width = 1, 1, img.shape[0], img.shape[1]
    
    #取出annotations資訊繪成矩形物件，放入boxes變數中。
    bb = [dlib.rectangle(left = left, top = top, right = width, bottom = height)]
    boxes.append(bb)
    
    #將圖片放入images變數
    images.append(io.imread(imagePath))

#丟入三個參數開始訓練
print("[INFO] training detector...")
detector = dlib.train_simple_object_detector(images, boxes, options)
 
# 將訓練結果匯出到檔案
print("[INFO] dumping classifier to file...")
regex = re.compile(r'/.+')
output = regex.findall(args["class"])[0].replace("/","")
detector.save("output/" + output)

# 圖形化顯示Histogram of Oriented Gradients（簡稱HOG）
win = dlib.image_window()
win.set_image(detector)
dlib.hit_enter_to_continue()
