from tkinter import *
import tkinter.filedialog as fdialog
import cv2
import stitch
import numpy as np
import random
import matplotlib.pyplot as plt

def findFeatures(img):
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(img, None)

    img = cv2.drawKeypoints(img, keypoints, outImage = None)

    return keypoints, descriptors

def matchFeatures(keypointsleft, keypointsright, featuresleft, featuresright, leftimage, rightimage):
    matcher = cv2.BFMatcher()
    matches = matcher.knnMatch(featuresright, featuresleft, k=2)
    
    return matches

def stitch():
    leftimage=cv2.imread('image_left.png')
    rightimage=cv2.imread('image_right.png')
    
    keypointsleft, featuresleft = findFeatures(leftimage)
    keypointsright, featuresright = findFeatures(rightimage)
    
    keypoints = [keypointsleft,keypointsright]
    
    matches = matchFeatures(keypointsleft, keypointsright, featuresleft, featuresright, leftimage, rightimage)
    good_features=[]

    for m in matches:
        if m[0].distance < 0.5 *m[1].distance:
            good_features.append(m)
            matches = np.asarray(good_features)

    if len(matches[:, 0]) >= 4:
        source = np.float32([keypointsright[m.queryIdx].pt for m in matches[:,0]]).reshape(-1, 1, 2)
        destination = np.float32([keypointsleft[m.trainIdx].pt for m in matches[:,0]]).reshape(-1, 1, 2)
        
        H, masked = cv2.findHomography(source, destination, cv2.RANSAC, 5.0)
    else:
        raise AssertionError("Cannot find enough keypoints")

    final = cv2.warpPerspective(rightimage, H, (leftimage.shape[1] + rightimage.shape[1], leftimage.shape[0]))
    final[0: leftimage.shape[0], 0: leftimage.shape[1]] = leftimage
    
    final=cv2.resize(final,(350,350))
    cv2.imwrite('final.png',final)
    