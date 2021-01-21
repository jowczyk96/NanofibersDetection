# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:39:20 2021

@author: KKA
"""
import cv2
import numpy as np

def empty_function(*args):
    pass

def trackbaring(image, image_color, function_type):
    """
    INPUT:
    image - 3D array of (grayscale) image in BGR scale (OpenCV default scale)
    function_type - string of what function type should be applied.
    ["Canny", "threshold", "otsu", "HoughLinesP", "Laplacian", "adaptiveThreshold",
     "medianBlur", "GaussianBlur", "erode", "dilate", "MORPH_OPEN", "MORPH_COLSE"]
    defaults - list of default values for trackbars, by default sets all 0
    
    OUTPUT:
    result - given method result
    showing - result showing in window w/o text (mostly drawn over original BGR image)
    trackbars - list of chosen parameter values (last one mainly for debugging)
    """
    defaults=[0,0,0,0,0]
    win_name = "Trackbars"

    cv2.namedWindow(win_name)
    cv2.resizeWindow(win_name, 500,100)
    
    # Show window on top left corner on primary screen
    cv2.moveWindow(win_name, 10,50)
    
    # The one inserted in methods, when needed converted to grayscale
    img = image.copy()
    
    ##################### INITIALISING TRACKBARS ###############################
    # Depending on function_type the trackbars are created
    if function_type == "Canny":
        trackbar_names = ["canny_th1", "canny_th2"]#, "kernel_size", "dilate_iter"]
        cv2.createTrackbar(trackbar_names[0], win_name, defaults[0], 255, empty_function)
        cv2.createTrackbar(trackbar_names[1], win_name, 255, 255, empty_function)
        # cv2.createTrackbar(trackbar_names[2], win_name, 2, 7, empty_function)
        # cv2.createTrackbar(trackbar_names[3], win_name, 1, 5, empty_function)
    
    elif function_type == "threshold":
        trackbar_names = ["threshold", "th_type"]
        # Some thershold types seem to be doing nothing...
        threshold_type = [cv2.THRESH_BINARY,
                          cv2.THRESH_BINARY_INV,
                          cv2.THRESH_TRUNC,
                          cv2.THRESH_TOZERO,
                          cv2.THRESH_TOZERO_INV]
        cv2.createTrackbar(trackbar_names[0], win_name, defaults[0], 255, empty_function)
        cv2.createTrackbar(trackbar_names[1], win_name, defaults[1], len(threshold_type)-1, empty_function)
    
    elif function_type == "thresh_binary":
        # Needs grayscale as input
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        trackbar_names = ["threshold"]
        cv2.createTrackbar(trackbar_names[0], win_name, 50, 255, empty_function)
        
    elif function_type == "HoughLinesP":
        # Needs grayscale as input
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        trackbar_names = ["min len", "max gap"]
        #cv2.createTrackbar(trackbar_names[0], win_name, 1, 99, empty_function)
        #cv2.createTrackbar(trackbar_names[1], win_name, 0, 89, empty_function)
        #cv2.createTrackbar(trackbar_names[2], win_name, 100, 255, empty_function)
        cv2.createTrackbar(trackbar_names[0], win_name, 40, 500, empty_function)
        cv2.createTrackbar(trackbar_names[1], win_name, 5, 250, empty_function)
        
    elif function_type == "Laplacian":
        # Needs grayscale as input
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        trackbar_names = ["kernel_r"]
        cv2.createTrackbar(trackbar_names[0], win_name, defaults[0], 15, empty_function)
        
    elif function_type == "adaptiveThreshold":
        # Needs grayscale as input
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        trackbar_names = ["adp_meth", "th_type", "kernel_r", "mean_C"]
        adaptive_type = [cv2.ADAPTIVE_THRESH_MEAN_C,
                         cv2.ADAPTIVE_THRESH_GAUSSIAN_C]
        threshold_type = [cv2.THRESH_BINARY,
                          cv2.THRESH_BINARY_INV]
        cv2.createTrackbar(trackbar_names[0], win_name, defaults[0], len(adaptive_type)-1, empty_function)
        cv2.createTrackbar(trackbar_names[1], win_name, defaults[1], len(threshold_type)-1, empty_function)
        cv2.createTrackbar(trackbar_names[2], win_name, defaults[2], 500, empty_function)
        cv2.createTrackbar(trackbar_names[3], win_name, defaults[3], 50, empty_function)
        
    elif function_type == "medianBlur":
        trackbar_names = ["kernel_r"]
        cv2.createTrackbar(trackbar_names[0], win_name, defaults[0], 49, empty_function)
        
    elif function_type == "GaussianBlur":
        trackbar_names = ["kernel_r", "std_x", "std_y"]
        cv2.createTrackbar(trackbar_names[0], win_name, defaults[0], 49, empty_function)
        cv2.createTrackbar(trackbar_names[1], win_name, defaults[1], 100, empty_function)
        cv2.createTrackbar(trackbar_names[2], win_name, defaults[2], 100, empty_function)
        
    elif function_type == "erode":
        trackbar_names = ["kernel", "iterations"]
        cv2.createTrackbar(trackbar_names[0], win_name, defaults[0], 100, empty_function)
        cv2.createTrackbar(trackbar_names[1], win_name, defaults[1], 10, empty_function)
        
    elif function_type == "dilate":
        trackbar_names = ["kernel", "iterations"]
        cv2.createTrackbar(trackbar_names[0], win_name, defaults[0], 100, empty_function)
        cv2.createTrackbar(trackbar_names[1], win_name, defaults[1], 10, empty_function)
        
    elif function_type == "MORPH_OPEN":
        trackbar_names = ["kernel", "iterations"]
        cv2.createTrackbar(trackbar_names[0], win_name, defaults[0], 100, empty_function)
        cv2.createTrackbar(trackbar_names[1], win_name, defaults[1], 10, empty_function)
        
    elif function_type == "MORPH_CLOSE":
        trackbar_names = ["kernel", "iterations"]
        cv2.createTrackbar(trackbar_names[0], win_name, defaults[0], 100, empty_function)
        cv2.createTrackbar(trackbar_names[1], win_name, defaults[1], 10, empty_function)
        
    else:
        cv2.destroyAllWindows()
        raise Exception("Wrong function_type. Library doesn't include '{}'".format(function_type))
    
    ############################# LIVE TRACKBARS ###############################
    # Making trackbars work
    while True:
        # Get trackbar values
        trackbars = []
        for i in range(len(trackbar_names)):
            trackbars.append(cv2.getTrackbarPos(trackbar_names[i], win_name))
        
        # So the initial image won't get overdrawn, this is always BGR!
        
        #showing = image_color.copy()
        
        ####################### FUNCTION CALCULATION ###########################
        """
        Let OpenCV do it's magic with methods and draw it over the original input image
        Depends on function_type
        
        result - should not be changed between original method output and return
        img - is the one that should always be inserted to OpenCV method, it has correct colorscale
        showing - is first a copy of original BGR and used only to draw onto
        when copying result into showing, it should be guaranteed that it's BGR
        """
        if function_type == "Canny":
            result = cv2.Canny(img, trackbars[0], trackbars[1])
            # kernel = np.ones((trackbars[2], trackbars[2]), np.uint8)
            # result = cv2.dilate(result,kernel,iterations = trackbars[3])
            showing=result.copy()
            #showing[result==255, 2] = result[result==255] # Draws red, BGR!
        
        elif function_type == "threshold":
            result = cv2.threshold(img, trackbars[0], 255, threshold_type[trackbars[1]])[1]
            #showing[result==255] = result[result==255] # Draws white, all channels
            showing=result.copy()
            
        elif function_type == "thresh_binary":
            print(str(trackbars[0]))
            ret, result = cv2.threshold(img, trackbars[0], 255, cv2.THRESH_BINARY)
            #showing[result==255, 2] = result[result==255] # Draws red, BGR
            
            showing=result.copy()
      
            
        elif function_type == "HoughLinesP":
            showing = image_color.copy()
            result = cv2.HoughLinesP(img,
                                     1,
                                     np.pi/180,
                                     100,
                                     None,
                                     minLineLength=trackbars[0],
                                     maxLineGap=trackbars[1])
            if result is not None:
                for i in range(0, len(result)):
                    l = result[i][0]
                    cv2.line(showing, (l[0], l[1]), (l[2], l[3]), (255,0,0), 2, cv2.LINE_AA)
                    
        elif function_type == "Laplacian":
            result = cv2.Laplacian(img, ksize=2*trackbars[0]+1, ddepth=cv2.CV_FEATURE_PARAMS_HOG)
            # Set all channels constant where result>0
            # Setting them all zero is not good because on dark areas
            # it cannot then be seen which areas are also altered
            # Color transition is better (low cyan -> bright red-ish)
            showing[result>0, :] = 64
            showing[result>0, 2] = result[result>0] # Draws red, keeps other const, BGR
            
        elif function_type == "adaptiveThreshold":
            result = cv2.adaptiveThreshold(img, 255,
                                           adaptive_type[trackbars[0]],
                                           threshold_type[trackbars[1]],
                                           trackbars[2]*2+3,
                                           trackbars[3])
            showing[result==255, 2] = result[result==255] # Draws red, BGR
            
        elif function_type == "medianBlur":
            result = cv2.medianBlur(img, trackbars[0]*2+3) # outputs BGR here
            showing = result
            # saves memory compared to np.copy() and SHOULDN'T make a diference
        elif function_type == "GaussianBlur":
            result = cv2.GaussianBlur(img,
                                      (trackbars[0]*2+1, trackbars[0]*2+1),
                                      sigmaX = trackbars[1]*0.1,
                                      sigmaY = trackbars[2]*0.1) # outputs BGR here
            showing = result
            
        elif function_type == "erode":
            kernel = np.ones((trackbars[0]+1, trackbars[0]+1),np.uint8)
            result = cv2.erode(img,
                               kernel,
                               iterations=trackbars[1]) # outputs BGR here
            showing = result
            
        elif function_type == "dilate":
            kernel = np.ones((trackbars[0]+1, trackbars[0]+1),np.uint8)
            result = cv2.dilate(img,
                                kernel,
                                iterations=trackbars[1]) # outputs BGR here
            showing = result
            
        elif function_type == "MORPH_OPEN":
            kernel = np.ones((trackbars[0]+1, trackbars[0]+1),np.uint8)
            result = cv2.morphologyEx(img, cv2.MORPH_OPEN,
                                      kernel, iterations=trackbars[1]) # outputs BGR here
            showing = result
            
        elif function_type == "MORPH_CLOSE":
            kernel = np.ones((trackbars[0]+1, trackbars[0]+1),np.uint8)
            result = cv2.morphologyEx(img, cv2.MORPH_CLOSE,
                                      kernel, iterations=trackbars[1]) # outputs BGR here
            showing = result
        
        showing_temp = showing.copy()
        showing_temp = cv2.rectangle(showing_temp,(3,25),(250,5),color=(0,0,0),thickness=-1)
        cv2.putText(showing_temp,                   # image
                    "Press 'esc' to save and close!",    # text
                    (5, 20),                        # location
                    cv2.FONT_HERSHEY_SIMPLEX,       # font
                    0.5,                            # size
                    (255, 0, 0),                    # BGR
                    1,                              # thickness
                    cv2.LINE_AA)                    # ?
        cv2.imshow(win_name, showing_temp)
        
        # Code exits "while true loop" by pressing letter 'c'
        key = cv2.waitKey(1) & 0xFF
        if key == 27:#:
            break
    
    # Wrap it up
    cv2.destroyAllWindows()
    
    return result, showing, trackbars





