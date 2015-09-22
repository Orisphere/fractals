from PIL import Image
cimport numpy as np
import numpy as np
import time

class Mandelbrot():
	width = 0
	height = 0
	it = 0
	zoom = 0.0
	center_x = 0.0
	center_y = 0.0
	array = []
	rgb = []

	def __init__(self, w=900, h=600, i=1000, z=1, center=(-0.5,0.0)):
		self.height = h
		self.width = w
		self.it = i
		self.zoom = z*0.25
		self.center_x = center[0]
		self.center_y = center[1]
		self.array = self.generate_array()
	
	def generate_array(self):
		
		cdef int w = self.width 
		cdef int h = self.height
		cdef double z = self.zoom
		cdef double c_x = self.center_x
		cdef double c_y = self.center_y
		cdef double x_coor, y_coor, z_real, z_img, z_2_real
		cdef int x, y, i	
		cdef np.ndarray[np.uint16_t, ndim=2] np_img = np.zeros((h, w), dtype=np.uint16)
		cdef iterations = self.it
		for x in range(w):
			x_coor = ((x-0.50*w)/((<float>h/w)*z*w)+c_x)

			for y in range(h):
			
				y_coor = ((y-0.50*h)/(z*h)+c_y)
				z_real = 0
				z_img = 0
					
				for i in range(iterations):
				
					if z_real*z_real+z_img*z_img >= 4:
						np_img[y-1,x-1] = i
				
						break
					z_2_real = z_real*z_real-z_img*z_img + x_coor
					z_img =  2*z_real*z_img + y_coor
					z_real = z_2_real
		
		return np_img 
	
	def to_rgb_array(self):
		cdef int w = self.width 
		cdef int h = self.height
		cdef int x, y	
	
		rgb = np.ndarray((h, w, 3), dtype=np.uint8)
	
		for x in range(w):

			for y in range(h):
			
				i = self.array[y-1, x-1]
				if i == 0:
					rgb[y-1, x-1] = 0, 0, 0
				if 0<i<20:
					color = i*10
					rgb[y-1, x-1] = color, 0, 255-color
				if i>=20:
					color= i*10%255
					rgb[y-1, x-1] = 0, 255, color

		self.rgb = rgb
		return rgb

	
	def to_image(self):
		
		fractal = Image.fromarray(self.to_rgb_array())
		fractal.save("mandelbrot_c.png")
		return fractal

	def get_thumbnail(self, x,y):
		tn = self.rgb[y-70:y+70,x-70:x+70]
		thumbnail = Image.fromarray(tn)
		thumbnail.save("thumbnail.png")
		return None

	def get_coors(self, x, y):
		z = self.zoom
		h = self.height
		w = self.width
		c_x = self.center_x 
		c_y = self.center_y

		x_coor = ((x-0.50*w)/((h/w)*z*w)+c_x)
		y_coor = ((y-0.50*h)/(z*h)+c_y)
		return (x_coor, y_coor)

	def get_zoom(self):
		return self.zoom*4
