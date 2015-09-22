import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QColorDialog, QDialog, QHBoxLayout,QInputDialog, QLabel, QComboBox, QMainWindow)
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL import Image
from mandelbrot_set import Mandelbrot
from new_dialog import Zoom_dialog
from main_design import Ui_MainWindow


def to_QImage(fractal):
	w, h = fractal.size
	data = fractal.tobytes()
	qimage = QImage(data, w, h, QImage.Format_RGB32)
	return qimage


class Fractal_gui(QMainWindow, Ui_MainWindow):

	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.initUI()

	def initUI(self):
		self.fractal = Mandelbrot()
		self.fractal.to_image()

		pixmap = QPixmap('mandelbrot_c.png')
		scaled_pixmap = pixmap.scaled(900, 600, aspectRatioMode=Qt.KeepAspectRatio)	
		self.label.setPixmap(scaled_pixmap)
		self.label.setScaledContents(False)
		self.show()
	
	
	def showDialog(self, x, y):
		self.fractal.get_thumbnail(x, y)
		pixmap = QPixmap('thumbnail.png')
		coors = self.fractal.get_coors(x,y)
		d = Zoom_dialog()
		d.set_fractal(pixmap)
		d.set_coors(str(coors))	
		
		if d.exec_():
			zoom = int(d.get_zoom())*self.fractal.get_zoom()
			m = Mandelbrot(z=zoom,center=coors)
			m.to_image()
			pixmap = QPixmap('mandelbrot_c.png')
			self.label.setPixmap(pixmap)
			self.fractal = m



	def mousePressEvent(self, QMouseEvent):
		xpos = QMouseEvent.x()
		ypos = QMouseEvent.y()
		self.showDialog(xpos, ypos)
		print (xpos, ypos)


def main():
	app = QApplication(sys.argv)
	w = Fractal_gui()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()	
