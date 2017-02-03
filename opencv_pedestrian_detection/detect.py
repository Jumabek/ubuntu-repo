from __future__ import print_function
from imutils.object_detection import non_max_suppression 
from imutils import paths
import numpy as np
import argparse 
import imutils
import cv2
import os.path

ap = argparse.ArgumentParser()
ap.add_argument("-i","--images",required=True,help = "path to images directory")
args = vars(ap.parse_args())

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

if os.path.isfile(args["images"]):
    imagePath = args["images"]
    image = cv2.imread(imagePath)
    image = imutils.resize(image, width=min(400,image.shape[1]))
    orig = image.copy()
    
    #detect people in the image
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
    padding=(8,8), scale=1.05)  
    
    for (x,y,w,h) in rects:
        cv2.rectangle(orig,(x,y),(x+w,y+h),(0,0,255),2)
        
    #NMS
    rects = np.array([[x,y,x+w,y+h] for (x,y,w,h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    
    #draw after NMS
    for(xA, yA,xB, yB) in pick:
        cv2.rectangle(image,(xA,yA),(xB,yB),(0,255,0),2)
        
    #show some infor about BB
    filename = imagePath[imagePath.rfind("/") + 1:]
    print("[INFO] {}: {} original boxes, {} after suppression".format(
        filename, len(rects), len(pick)))
    
    #show the output images 
    cv2.imshow("before NMS",orig)
    cv2.imshow("after NMS",image)
    
    cv2.imwrite(filename,orig)
    cv2.imwrite(filename[:filename.rfind(".")]+"_nms.jpg",image)
    
    cv2.waitKey(0)
else:
    for imagePath in paths.list_images(args["images"]):
        image = cv2.imread(imagePath)
        image = imutils.resize(image, width=min(400,image.shape[1]))
        orig = image.copy()
        
        #detect people in the image
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
        padding=(8,8), scale=1.05)  
        
        for (x,y,w,h) in rects:
            cv2.rectangle(orig,(x,y),(x+w,y+h),(0,0,255),2)
            
        #NMS
        rects = np.array([[x,y,x+w,y+h] for (x,y,w,h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
        
        #draw after NMS
        for(xA, yA,xB, yB) in pick:
            cv2.rectangle(image,(xA,yA),(xB,yB),(0,255,0),2)
            
        #show some infor about BB
        filename = imagePath[imagePath.rfind("/") + 1:]
        print("[INFO] {}: {} original boxes, {} after suppression".format(
            filename, len(rects), len(pick)))
    
        #show the output images 
        cv2.imshow("before NMS",orig)
        cv2.imshow("after NMS",image)
        cv2.waitKey(0)