import cv2
import numpy as np 
from scipy.ndimage import gaussian_filter

def downsampling(image_):

    downsampled_= np.zeros((image_.shape[0], image_.shape[1],3), np.uint8)
    downsampled_fit = np.zeros((image_.shape[0], image_.shape[1],3), np.uint8)
    i, j= 0, 0
    
    for x in range (0, image_.shape[0], 3):
        for y in range(0, image_.shape[1], 3):
            
            downsampled_[x,y,0]= image_[x,y,0]
            downsampled_[x,y,1]= image_[x,y,1]
            downsampled_[x,y,2]= image_[x,y,2]
            
    for x in range (0, downsampled_.shape[0], 3):
        j=0
        for y in range(0, downsampled_.shape[1], 3):
            
            downsampled_fit[i,j,0]= downsampled_[x,y,0]
            downsampled_fit[i,j,1]= downsampled_[x,y,1]
            downsampled_fit[i,j,2]= downsampled_[x,y,2]
            j+=1
        i+=1
        

   


    return cv2.merge((downsampled_fit[:,:,0],
                      downsampled_fit[:,:,1],
                      downsampled_fit[:,:,2]))

def blur_(imagee_):
    return gaussian_filter(imagee_, sigma=1, radius=150)



image_= cv2.imread('lowdyn_image.jpg')
bimage= blur_(image_)

print(image_.shape)

downsampled_image= downsampling(bimage)

print(downsampled_image.shape)
cv2.imshow('',downsampled_image)
