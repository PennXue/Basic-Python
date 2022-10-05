import matplotlib.pyplot as plt
import skimage.io as io
import numpy as np

#part greyscale
def image_to_greyscale(image_filename , weighting):
    image = io.imread(image_filename)
    row = image.shape[0] # all the row pixels in image
    col = image.shape[1] # all the column pixels in image 
    image[:,:,:] =  weighting[0]*image[:,:,[0]]+weighting[1]*image[:,:,[1]]+weighting[2]*image[:,:,[2]] #apply the formula of greyscale  
    new_image = np.zeros((row,col)) # a new array of zeros
    for ro in range(row):
        for co in range(col):
            new_image[ro,co] = image[ro,co,[0]]/255 # change it to 2Darray and reverse it, which normalizes it to range(0,1)
    return new_image

#part combine
def combine_images(file1, file2, topleft1,topleft2, height, width):
    image1 = io.imread(file1)
    image2 = io.imread(file2)
    new_width1 = image1.shape[1] + width #extra width for region beyond the image bound
    new_height1 = image1.shape[0] + height #extra height for region beyond the image bound
    new_width2 = image2.shape[1] + width #extra width for region beyond the image bound
    new_height2 = image2.shape[0] + height #extra height for region beyond the image bound
    new_image1 = np.zeros([new_height1,new_width1,3]) #array full of zeros
    new_image2 = np.zeros([new_height2,new_width2,3]) 
    for row in range(new_image1.shape[0]): 
        if row < image1.shape[0]: #row number of new_image should less than image1
            for col in range(new_image1.shape[1]):
                if col < image1.shape[1]: 
                    new_image1[row,col] = image1[row,col] #switch the pixel in the black image to the appropriate pixel in the image
    for row in range(new_image1.shape[0]): #same step for second image
        if row < image2.shape[0]:
            for col in range(new_image1.shape[1]):
                if col < image2.shape[1]:
                    new_image2[row,col] = image2[row,col]
    image_1 = new_image1[topleft1[0]:topleft1[0]+height, topleft1[1]:topleft1[1]+width] #bound the selected region of first image
    image_2 = new_image2[topleft2[0]:topleft2[0]+height, topleft2[1]:topleft2[1]+width] #bound the selected region of second image
    black = np.zeros([height , width*2 ,3]) # make another full black image of size height * (width*2)
    black[:,0:width] = image_1[:,:] #left half is the first image
    black[:,width:width*2] = image_2[:,:] #right half is the second image
    black = np.array(black,dtype=int) # change the dtype of array to integer, otherwise, it won't show
    return black