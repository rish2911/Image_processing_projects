# -*- coding: utf-8 -*-
"""prob_1_3DRGB.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1InrJWQwDY8pc_WLakXkQz_ofbe5w_hjJ
"""

import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
import os

"""using the glob library to recursively find all the images"""

def cum_def_fun(img):
    cdf = []
    for i in  range(255):
        cdf.append((((np.shape((np.where(img<=i))))[1])/img.size))
    return cdf

def hist_eq(img):
    
    eq_img = np.copy(img)
    eq_img_c = np.copy(img)
    for i in  range(255):
        eq_img[np.where(img==i)] = np.floor((((np.shape((np.where(img<=i))))[1])/img.size)*(np.max(img)-np.min(img)))
    return eq_img, eq_img_c

frames =[]

frames = sorted(os.listdir('images/'))
video_output = cv2.VideoWriter('Histo_eq.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, (1224,370))

for i in range(25):
    
    image_og = cv2.imread('images/' + str(i) +'.png')
    # cdf = cum_def_fun(image_og)
    eq_img,_ = hist_eq(image_og)
    video_output.write(eq_img)
    # cv2.imshow('1',eq_img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()