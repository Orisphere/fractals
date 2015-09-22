from PIL import Image
from math import sqrt, floor
import numpy as np
import time

img = Image.new("RGB", (600, 400))

width = img.width

height = img.height


np_img = np.array(img)

start_time = time.clock()

def complex_square(z): 
	real = z[0]
	imaginary = z[1]
	result = (real*real-imaginary*imaginary, 2*real*imaginary)
	return result


def complex_abs(z):
	real = z[0]
	imaginary = z[1]
	result = sqrt(real*real+imaginary*imaginary)
	return result

def complex_sum(z1, z2):
	real = z1[0] + z2[0]
	imaginary = z1[1] + z2[1]
	result = (real, imaginary)
	return result





for x in range(width):
	x_coor = float((x-(2/3)*width)/((1/6)*width))

	for y in range(height):
		
		y_coor =float((y-0.5*height)/(0.25*height))
		z_real = float(0)
		z_img = float(0)
		
		for i in range(500):

			if z_real*z_real+z_img*z_img >= 4:
				if i < 20:
					np_img[y-1,x-1] = (25, i*5, 100)
				else:
					np_img[y-1,x-1] = (200, i, 200)
				break
			
			z_real = z_real*z_real-z_img*z_img + x_coor
			z_img =  2*z_real*z_img + y_coor



end_time = time.clock()
fractal = Image.fromarray(np_img)
print(end_time - start_time)
fractal.save("mandelbrot.png")

