# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  E-Yantra Robotics Competition
*                  ================================
*  This software is intended to check version compatiability of open source software
*  Theme: ANT BOT
*  MODULE: Task1.2
*  Filename: Task1.2.py
*  Version: 1.0.0  
*  Date: October 31, 2018
*  
*  Author: e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
"""

"""
ArUco ID Dictionaries: 4X4 = 4-bit pixel, 4X4_50 = 50 combinations of a 4-bit pixel image
List of Dictionaries in OpenCV's ArUco library:
DICT_4X4_50	 
DICT_4X4_100	 
DICT_4X4_250	 
DICT_4X4_1000	 
DICT_5X5_50	 
DICT_5X5_100	 
DICT_5X5_250	 
DICT_5X5_1000	 
DICT_6X6_50	 
DICT_6X6_100	 
DICT_6X6_250	 
DICT_6X6_1000	 
DICT_7X7_50	 
DICT_7X7_100	 
DICT_7X7_250	 
	 
DICT_ARUCO_ORIGINAL
Reference: http://hackage.haskell.org/package/opencv-extra-0.2.0.1/docs/OpenCV-Extra-ArUco.html
Reference: https://docs.opencv.org/3.4.2/d9/d6a/group__aruco.html#gaf5d7e909fe8ff2ad2108e354669ecd17
"""

import numpy as np
import cv2
import cv2.aruco as aruco
import sys
import math
from aruco_lib import angle_calculate
from aruco_lib import calculate_Robot_State
from aruco_lib import mark_Aruco
from aruco_lib import detect_Aruco

def aruco_detect(path_to_image):
    '''
    you will need to modify the ArUco library's API using the dictionary in it to the respective
    one from the list above in the aruco_lib.py. This API's line is the only line of code you are
    allowed to modify in aruco_lib.py!!!
    '''
    img = cv2.imread(path_to_image)     #give the name of the image with the complete path
    id_aruco_trace = 0
    det_aruco_list = {}
    img2 = img[0:400,0:400,:]   #separate out the Aruco image from the whole image
    cv2.imshow('frame',img2)
    det_aruco_list = detect_Aruco(img2)
    
    if det_aruco_list:
            img3 = mark_Aruco(img2,det_aruco_list)
            id_aruco_trace = calculate_Robot_State(img3,det_aruco_list)
            print(id_aruco_trace)
            cv2.imshow('image',img2)
            cv2.waitKey(0)
	
      #  Code for triggering color detection on ID detected
    
            cv2.destroyAllWindows()
           

def color_detect(img):
    '''
    #code for color Image processing to detect the color and shape of the 2 objects at max.
    #mentioned in the Task_Description document. Save the resulting images with the shape
    #and color detected highlighted by boundary mentioned in the Task_Description document.
    #The resulting image should be saved as a jpg. The boundary should be of 25 pixels wide.
    
    '''
    i=6
    j=3
    
    image=cv2.imread('Image1.jpg')
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret , threshold = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    _, contours,_=cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image,contours,i,(0,0,255),25)
    #cv2.drawContours(image,contours,j,(0,255,0),25)
    
    result_image = image
    img = image[0:400,0:400,:]

    aruco_list = detect_Aruco(img)
    
    M1 = cv2.moments(contours[i])
    cx1= int(M1['m10']/M1['m00'])
    cy1= int(M1['m01']/M1['m00'])
    
    M2 = cv2.moments(contours[j])
    cx2= int(M2['m10']/M2['m00'])
    cy2= int(M2['m01']/M2['m00'])
    
    
    tuple1 =(cx1,cy1)
    tuple2 =(cx2,cy2)
    
    calculate_Robot_State(img,aruco_list)
    mark_Aruco(img,aruco_list)
    
    print(tuple1)
    print(tuple2)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(result_image,str(tuple1),(cx1,cy1), font, 0.5,(0,0,0),2,cv2.LINE_AA)
    cv2.putText(result_image,str(tuple2),(cx2,cy2), font, 0.5,(0,0,0),2,cv2.LINE_AA)
   
    cv2.imshow("ColorImage",result_image)
    cv2.waitKey(0)

    
    
    



    
    
    

     

    



if __name__ == "__main__":    
    aruco_detect('Image2.jpg')
    color_detect('Image2.jpg')
    
