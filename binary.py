import numpy
from scipy.misc import imread
import cv2
im_gray = cv2.imread('outfile.jpg', cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

thresh = 200

im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('bw_image.png', im_bw)


im=imread("bw_image.png")
numpy.savetxt("foo.dat",im,delimiter=",")


i=im.shape[0]
a = numpy.zeros(shape=(i,2))
numpy.savetxt("a.dat",a,delimiter=",")
for j in range(i):
	num_zeros = (im[j,:] == 0).sum()
	a[j-1] = [i-j,num_zeros]


numpy.savetxt("foooo.dat",a,delimiter=",")