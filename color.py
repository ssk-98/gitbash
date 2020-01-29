import numpy
import cv2
import cv2.aruco as aruco

def color_detect(img):
    '''
    #code for color Image processing to detect the color and shape of the 2 objects at max.
    #mentioned in the Task_Description document. Save the resulting images with the shape
    #and color detected highlighted by boundary mentioned in the Task_Description document.
    #The resulting image should be saved as a jpg. The boundary should be of 25 pixels wide.
    
    '''
    image = cv2.imread('Image1.jpg')
    blurred = cv2.pyrMeanShiftFiltering(image,31,91)
    gray = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
    ret , threshold = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    _, contours,_=cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    print(len(contours))
    cv2.drawContours(image,contours,1,(255,0,0),25)
    cv2.drawContours(image,contours,3,(0,255,0),25)
    cv2.imshow("ColorImage",image)
    cv2.waitKey(0)



color_detect('Image1.jpg')
