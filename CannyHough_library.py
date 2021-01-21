# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:32:27 2021

@author: Asia
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import os as os

"""
Our library:
"""
import trackbars_library as track

def empty_function(*args):
    pass

def runCannyAlgorithm(name,runType):

    img_name = name.split("/")[-1]
    directory = os.path.dirname(name)    

    img = cv2.imread(name)
    
    (h, w, d) = img.shape
    
    img_cropped = img[0:600,0:1024]
    
    kernel = (5,5)
    blurred = cv2.GaussianBlur(img_cropped, kernel, sigmaX = 5, sigmaY = 5)
    
    kernel = np.ones((5,5),np.uint8)
    img_cleaned = cv2.erode(blurred,kernel,iterations = 0)
    
    plt.figure(figsize = (16,16))
    plt.imshow(img_cleaned,cmap = 'gray')
    
    img_cleaned = cv2.dilate(img_cleaned,kernel,iterations = 0)
    
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    img_cleaned = cv2.filter2D(img_cleaned, -1, kernel)
    
    image_copy = img_cleaned.copy()
    
    lower_gray = np.array([100,100,100])
    upper_gray = np.array([250,250,250])
    
    gray = cv2.cvtColor(img_cleaned, cv2.COLOR_RGB2GRAY)
    
    if runType == '2':
        temp1, thresh, temp2 = track.trackbaring(gray, img_cleaned, "thresh_binary")
        #temp1, edged, temp2 = track.trackbaring(thresh, None, "Canny")

    else:
        ret, thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    edged = cv2.Canny(thresh, 100, 255)
    
    
    
    dilated = cv2.dilate(edged,kernel,iterations = 1)
    final = dilated
    
    contours, hierarchy = cv2.findContours(final,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.drawContours(img_cropped,contours,contourIdx=-1, color=(0,0,255),thickness=1)
    
    out_dir = directory + str("/output/")
    
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    out_dir  = out_dir + str(img_name)
    
    cv2.imwrite(out_dir,img_cropped)
    
    return img_cropped, out_dir, edged


def runHoughAlgorithm(img2hough,directory,runType):
    
    img_cropped_lines = cv2.imread(directory)
    
    if runType == '2':

        temp1, img_cropped_lines, temp2 = track.trackbaring(img2hough, img_cropped_lines, "HoughLinesP")
        
    else:
        linesP = cv2.HoughLinesP(img2hough, 1, np.pi / 180, 100, None, 40, maxLineGap=5)
         
        if linesP is not None:
                for i in range(0, len(linesP)):
                    l = linesP[i][0]
                    cv2.line(img_cropped_lines, (l[0], l[1]), (l[2], l[3]), (255,10,10), 2, cv2.LINE_AA)
            
    cv2.imwrite(directory,img_cropped_lines)
    
    return img_cropped_lines, directory
    
