from imutils import paths
import argparse
import dlib
import cv2
 
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--detector", required=True, help="Path to trained object detector")
ap.add_argument("-t", "--testing", required=True, help="Path to directory of testing images")
args = vars(ap.parse_args())
 
#載入訓練好的detector
detector = dlib.simple_object_detector(args["detector"])
 
#載入測試圖片逐張進行
for testingPath in paths.list_images(args["testing"]):
#讀取圖片並執行dector並產生矩形物件以便用於標記辨識出的部份
    image = cv2.imread(testingPath)
    boxes = detector(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
 
#在圖片上繪出該矩形
    for b in boxes:
        (x, y, w, h) = (b.left(), b.top(), b.right(), b.bottom())
        cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)
 
#顯示圖片
        cv2.imshow("Image", image)
        cv2.waitKey(0)
