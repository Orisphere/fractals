from PIL import Image
cimport numpy as np
import numpy as np
import time
from cython.parallel cimport prange
from cython.view cimport array as cvarray

class Mandelbrot_set()
	width
	height

	def __init__(self, h, w):
		self.height = h
		self.width = w


def main():
	
	cdef int w = self.width 
	cdef int h = self.height
	cdef double x_coor, y_coor, z_real, z_img, z_2_real
	cdef int x, y, i	
	cdef np.ndarray[np.uint8_t, ndim=3] np_img = np.zeros((h, w, 3), dtype=np.uint8)
	start_time = time.clock()


	for x in range(w):
		x_coor = (x-(4.0/6.0)*w)/((1.0/6.0)*width)

		for y in range(h):
		
			y_coor = (y-0.50*h)/(0.25*height)
			z_real = 0
			z_img = 0
				
			for i in range(1000):
			
				if z_real*z_real+z_img*z_img >= 4:
					if i < 20:
						np_img[y-1,x-1] = 25, i*5, 100
					else:
						np_img[y-1,x-1] = 200, i, 200
					break
			
				z_2_real = z_real*z_real-z_img*z_img + x_coor
				z_img =  2*z_real*z_img + y_coor
				z_real = z_2_real


	end_time = time.clock()
	fractal = Image.fromarray(np_img)
	print(end_time - start_time)
	fractal.save("mandelbrot_c.png")


main()
