from PIL import Image
import numpy as np
import time

img = Image.new("RGB", (600, 400))

width = img.width

height = img.height


np_img = np.array(img)

start_time = time.clock()

def escape_test(pixel_x, pixel_y, x, y, real, img, itr):
	if itr > 500:
		return None

	if real*real+img*img >= 4:
		if itr < 20:
			np_img[pixel_y-1,pixel_x-1] = (30, itr*5, 100)
		else:
			np_img[pixel_y-1,pixel_x-1] = (200, itr, 200)
					
		return None

	z_2_real = real*real-img*img + x
	z_img =  2*real*img + y
	z_real = z_2_real

	return escape_test(pixel_x, pixel_y, x, y, z_real, z_img, itr+1)
	

for x in range(width):
	x_coor = float((x-(2/3)*width)/((1/6)*width))

	for y in range(height):
		
		y_coor =float((y-0.5*height)/(0.25*height))
		z_real = float(0)
		z_img = float(0)
		
		escape_test(x, y, x_coor, y_coor, z_real, z_img, 1)
	

end_time = time.clock()
fractal = Image.fromarray(np_img)
print(end_time - start_time)
fractal.save("mandelbrot.png")

