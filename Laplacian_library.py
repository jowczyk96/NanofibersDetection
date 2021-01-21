# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:18:12 2021

@author: Asia
"""

import cv2
import os as os

"""
Our library:
"""
import trackbars_library as track

def runLaplacianAlgorithm(name, runType):

    img_name = name.split("/")[-1]
    directory = os.path.dirname(name)
    
    img_original = cv2.imread(name, cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(img_gray,(3,3),2)

    img_filtered = cv2.Laplacian(img_blurred, ksize=3, ddepth=cv2.CV_64F)

    img_filtered = cv2.convertScaleAbs(img_filtered)
    
    img_cropped = img_original[0:600,0:1024] 
    
    if runType == '2':
        temp1, img_thresh, temp2 = track.trackbaring(img_filtered, img_cropped, "thresh_binary")
        #temp1, edged, temp2 = track.trackbaring(thresh, None, "Canny")
    else:
    
        ret, img_thresh = cv2.threshold(img_filtered,100,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    markers = [[1,1]]
    
    for x in range(1,599):
        for y in range(1,1023):
            if img_thresh[x,y] == 255: 
                    img_cropped[x,y,2] = 255
                    markers.append([x,y])
    
    
    out_dir = directory + str("/output/")
    
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    out_dir  = out_dir + str(img_name)
    
    cv2.imwrite(out_dir,img_cropped)
    
    return img_cropped, out_dir, img_thresh
