#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video Classifier:
-------------------------------------------------------------------------------
Author: G. Hiemstra

"""
# Load required libraries
import os
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import pandas as pd
from natsort import natsorted
import numpy as np

"""
## Step 1. Extract the frames from the video and store it in a folder
#  ----------------------------------------------------------------------------
"""

# Specify folder location of video
video_file_loc = "/home/glenn/python_map/advert.mp4"

# Create new folder to store
newpath = "/home/glenn/python_map/video_frames_container"
if not os.path.exists(newpath):
    os.makedirs(newpath)

# Set working directory to new folder
os.chdir(newpath)

# Check current working directory
print("Current Working Directory:", os.getcwd())

# Define helper function to extract frames from video 
def getFrame(sec, name_video_file, pathOut):
    
    if not os.path.exists(pathOut):
        os.makedirs(pathOut)
    
    vidcap = cv2.VideoCapture(name_video_file)
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames, image = vidcap.read()
    
    if hasFrames:
        # save frame as JPG file
        cv2.imwrite(pathOut + '/' + "frame_"+str(sec+1)+".jpg", image)
        print("Extracting frame from video: " + "frame "+str(sec+1)+" sec.jpg")
    return hasFrames

# Write function to extract images from video
def extract_images_from_video(name_video_file, pathOut, sec =0, frameRate =1):
    frameRate = frameRate
    success = getFrame(sec, name_video_file, pathOut)
    while success:
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec, name_video_file, pathOut)
 
# Give folder a name where you store the files
output_dir = "data_frames_container"
    
# Run function
extract_images_from_video(pathOut =output_dir,
                          name_video_file= "advert.mp4",
                          frameRate = 1)

# Make list containing all names of the videoframes
name_list_videoframes = os.listdir(output_dir)

# Naturally sort folder list on alphabetic order
name_list_videoframes = natsorted(name_list_videoframes)

# Check it worked
print(name_list_videoframes)


"""
## Step 2. Classify the images of the video
#  ----------------------------------------------------------------------------
"""

# Show image
print(name_list_videoframes[44])

# read input image
image = cv2.imread(output_dir + '/' + name_list_videoframes[44])

# apply object detection
bbox, label, conf = cv.detect_common_objects(image)

print(label, conf)


# Extract unique values from list
list(set(label))

# Put the results in a dataframe
pd.DataFrame(data = conf)















