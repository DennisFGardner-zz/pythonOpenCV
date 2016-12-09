# is this how I make comments

#import numpy as np
#import cv2
#
#img = cv2.imread('headshot.jpg',0)
#
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

from pylab import *
#import Image

from PIL import Image

im = Image.open('headshot.jpg').convert('L')
#im = im.convert('L')

#print im

print 2

im = array(im)

imshow(im)

print 'helloworld'