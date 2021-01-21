# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 15:03:27 2021

@author: Asia
"""

import cv2
import numpy as np
import os as os

"""
Our library:
"""
import trackbars_library as track

def runWatershedAlgorithm(name,runType):

    img_name = name.split("/")[-1]
    directory = os.path.dirname(name)

    img = cv2.imread(name)
    
    (h, w, d) = img.shape

    img_cropped = img[0:600,0:1024]
    
    img_gray = cv2.cvtColor(img_cropped,cv2.COLOR_BGR2GRAY)
    img_equalized = cv2.equalizeHist(img_gray)
    
    if runType == '2':
        temp1, img_thresh, temp2 = track.trackbaring(img_equalized, img_cropped, "thresh_binary")
        #temp1, edged, temp2 = track.trackbaring(thresh, None, "Canny")
    else:
        ret, img_thresh = cv2.threshold(img_equalized,50,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    kernel = np.ones((3,3),np.uint8)
    
    img_opened = cv2.morphologyEx(img_thresh,cv2.MORPH_OPEN,kernel,iterations=2)
    img_background = cv2.dilate(img_opened,kernel,iterations=2)
    
    #foreground = np.uint8(sure_fg)
    unknown = cv2.subtract(img_background,img_thresh)
    
    ret, markers = cv2.connectedComponents(img_thresh)
    
    img_black = np.zeros([600,1024,3],dtype=np.uint8)
    
    markers = markers+1
    markers[unknown==255] = -1
    
    markers = cv2.watershed(img_cropped,markers)
      
    img_black[markers==-1] = [0,0,255]
    
    img_gray = cv2.cvtColor(img_black,cv2.COLOR_BGR2GRAY)
    img_dilated = cv2.dilate(img_gray,kernel,iterations = 1)  
    
    img_cropped[img_dilated == 76] = [0,0,220]
    
    out_dir = directory + str("/output/")
    
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    out_dir  = out_dir + str(img_name)
    
    cv2.imwrite(out_dir,img_cropped)
    
    return img_cropped, out_dir, img_dilated