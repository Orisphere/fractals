from io import BytesIO
cimport numpy as np
import numpy as np
from PIL import Image, ImageQt
import time

class Mandelbrot():

	def __init__(self, w=900, h=600, i=1000, z=1, center=(-0.5,0.0)):
		self.height = h
		self.width = w
		self.it = i
		self.zoom = z*0.25
		self.center_x = center[0]
		self.center_y = center[1]
		self.colors = [[255, 255, 0], [180, 255, 0], [30, 255, 0], [0, 255, 130], 
				[0, 255, 255], [0, 180, 255], [0, 30, 255], [130, 0, 255],
				[180, 0, 255], [255, 0, 255]] 
		self.generate_array()
		self.to_rgb_array()
		self.to_image()

	def generate_array(self):
		
		cdef int w = self.width 
		cdef int h = self.height
		cdef double z = self.zoom
		cdef double c_x = self.center_x
		cdef double c_y = self.center_y
		cdef double x_coor, y_coor, z_real, z_img, z_2_real
		cdef int x, y, i	
		cdef np.ndarray[np.uint16_t, ndim=2] np_img = np.zeros((h, w), dtype=np.uint16)
		cdef int iterations = self.it
		for x in range(w):
			x_coor = ((x-0.50*w)/((<float>h/w)*z*w)+c_x)

			for y in range(h):
			
				y_coor = ((y-0.50*h)/(z*h)+c_y)
				z_real = 0
				z_img = 0
					
				for i in range(iterations):
				
					if z_real*z_real+z_img*z_img >= 4:
						np_img[y,x] = i
				
						break
					z_2_real = z_real*z_real-z_img*z_img + x_coor
					z_img =  2*z_real*z_img + y_coor
					z_real = z_2_real
	
		self.array = np_img
		return None

	
	def to_rgb_array(self):
		cdef int w = self.width 
		cdef int h = self.height
		cdef int x, y	
	
		rgb = np.ndarray((h, w, 3), dtype=np.uint8)
	
		for x in range(w):

			for y in range(h):
			
				i = self.array[y, x]
				if i == 0:
					rgb[y, x] = [0, 0, 0]
				else:	
					rgb[y, x] = self.colors[i%10]
				
		self.rgb = rgb
		return None 

	def inc_itr(self, it):
		cdef int w = self.width 
		cdef int h = self.height
		cdef double z = self.zoom
		cdef double c_x = self.center_x
		cdef double c_y = self.center_y
		cdef double x_coor, y_coor, z_real, z_img, z_2_real
		cdef int x, y, i	
		cdef int iterations = it
		cdef np.ndarray[np.uint16_t, ndim=2] np_img = self.array 
		iterable = np.nditer(self.array, flags=['multi_index'])

		while not iterable.finished:
			if iterable[0] == 0: 
				y, x = iterable.multi_index
				x_coor = ((x-0.50*w)/((<float>h/w)*z*w)+c_x)
				y_coor = ((y-0.50*h)/(z*h)+c_y)
				z_real = 0
				z_img = 0
					
				for i in range(iterations):
				
					if z_real*z_real+z_img*z_img >= 4:
						np_img[y,x] = i
				
						break
					z_2_real = z_real*z_real-z_img*z_img + x_coor
					z_img =  2*z_real*z_img + y_coor
					z_real = z_2_real
			iterable.iternext()
		self.it = it
		self.array = np_img
		return None 
	


	def to_image(self):
		
		fractal = Image.fromarray(self.rgb)
		self.image = fractal
		return None
	
	def save_image(self, filename):
		self.image.save(filename+".png")
		return None

	def to_string(self):
		return self.image.tobytes()

	def to_string_object(image):
		s = BytesIO()
		image.save(s, format="PNG")
		return s.getvalue()
	
	def get_thumbnail(self, x,y):
		tn = self.rgb[max(y-70, 0):min(y+70, self.height),
				max(x-70, 0):min(x+70, self.width)]
		thumbnail = Image.fromarray(tn)
		return thumbnail

	def get_coors(self, x, y):	#Converts pixel coors to x,y coors
		z = self.zoom
		h = self.height
		w = self.width
		c_x = self.center_x 
		c_y = self.center_y

		x_coor = ((x-0.50*w)/((h/w)*z*w)+c_x)
		y_coor = ((y-0.50*h)/(z*h)+c_y)
		return (x_coor, y_coor)
	
	def get_iter(self, x, y): #x, y are pixel coordinates
		return self.array[y, x]
	
	def get_zoom(self):
		return self.zoom*4

	def get_size(self):
		return self.width, self.height
