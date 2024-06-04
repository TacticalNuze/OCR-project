#Importing libraries
import matplotlib.pyplot as plt
import cv2 as cv 
from glob import glob
import numpy as np
import pandas as pd
import os


#Rescaling images
def Rescale(img,scale=0.75):
    height=int(img.shape[0]*scale)
    width=int(img.shape[1]*scale)
    dimensions=(height,width)

    return cv.resize(img,dimensions,interpolation=cv.INTER_CUBIC)

#Transforming image into greyscale
def Grey(img):
    greyImg=cv.cvtColor(img,code=cv.COLOR_BGR2GRAY)
    return greyImg
#Blurring 
def Blur(img):
    newImg=cv.medianBlur(img,3)
    return newImg
#Thresholding
def Threshold(img,threshold=125):
    thresh,newImg=cv.threshold(img,threshold,220,cv.THRESH_BINARY)
    return newImg
def adaptiveThreshold(img):
    newImg=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
    return newImg
#Sharpening
kernel_sharp=np.array([[-1,-1,-1,],
                       [-1,9,-1],
                       [-1,-1,-1]])
def Sharpen(img,kernel_sharp=kernel_sharp):
    return cv.filter2D(img,-1,kernel_sharp)

#Basic printed document processing
def docProcessing(InputFolder="C:\\Users\\hp\\Documents\\Code projects\\OCR benchmark\\Pictures",OutputFolder="C:\\Users\\hp\\Documents\\Code projects\\OCR benchmark\\TreatedPictures",threshold=125,adapt=1,grey=1,blur=1,thresh=0,show=1,sharp=1):
    """This function is basic pipeline for processing printed documents, change the parameters for grey, blur or thresh to 0 to not proceed with said operation.
    The letters added to name of file stand for: 
    G: Greyscale
    B: Blurred
    T: Simple threshold
    A: Adaptive threshold
    S: Sharpened
    """
    #Changing the work directory to path given in argument
    os.chdir(f"{InputFolder}")
    listofimages=os.listdir()

    #Listing all images found in directory
    for imgpath in listofimages:
        os.chdir(f"{InputFolder}")
        name=""
        newImg=cv.imread(imgpath)
        
        if grey:
            newImg=Grey(newImg)
            name+="G"
    
        if blur:
            newImg=Blur(newImg)
            name+="B"

        if thresh:
            newImg=Threshold(newImg,threshold)
            name+="T"

        if adapt:
            newImg=adaptiveThreshold(newImg)
            name+="A"
        if sharp:
            newImg=Sharpen(newImg)
            name+="S"
        if show:
            cv.imshow(f"{name} "+imgpath,newImg)
            cv.waitKey(0)
        

        #Saving treated files in directory of choice
        os.chdir(str(OutputFolder))
        cv.imwrite(f'{name} '+imgpath,newImg)
        print(f"The dimensions of the image are {newImg.shape}")
    
    


