"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

Note: We are using an actual image that will be represented as a 3D array (2 space dimensions and one color dimension). We use scipy for the image format and matplotlib for displaying the image.
"""

from math import ceil
import copy

def rotate(input_mat):
    new_mat = input_mat[:, :, :]
    N = len(new_mat)
    for lay in range(ceil(N/2)):
        end = N - lay-1
        for i in range(end - lay):
            temp =copy.deepcopy(new_mat[lay][i+lay]) # Top-Left
            new_mat[lay][i+lay] = new_mat[end-i][lay] # BottomLeft to TopLeft
            new_mat[end-i][lay] = new_mat[end][end-i] # BottomRight to BottomLeft
            new_mat[end][end-i] = new_mat[i+lay][end] # BottomRight to TopRight
            new_mat[i+lay][end] = temp # TopLeft to TopRight

def crop_square(img):
    x,y,_ = img.shape
    crop_dim  = min(x, y)
    return img[:crop_dim,:crop_dim,:]

from scipy import misc
f = misc.face()
# misc.imsave('face.png', f)


import matplotlib as mtpl
mtpl.use('TkAgg')

import matplotlib.pyplot as plt

f = crop_square(f)
plt.imshow(f)

rotate(f)
plt.imshow(f)
plt.show()
