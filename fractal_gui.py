import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QColorDialog, QDialog, QHBoxLayout,QInputDialog, QLabel, QComboBox, QMainWindow)
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL import Image
from mandelbrot_set import Mandelbrot
from new_dialog import Zoom_dialog
from main_design import Ui_MainWindow
from fractal_label import Fractal_label


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
		self.fractal = Mandelbrot(w=300, h=200)
		self.fractal.to_image()
		
		pixmap = QPixmap('mandelbrot_c.png')
		scaled_pixmap = pixmap.scaled(900, 600, aspectRatioMode=Qt.KeepAspectRatio)	

		self.label.setPixmap(scaled_pixmap)
		self.label.setScaledContents(False)
		
		self.label.dblclicked.connect(self.showDialog)
		self.label.moved.connect(self.updateStatusBar)
		self.show()
	
	def showDialog(self):
		x = self.sender().clickpos.x()
		y = self.sender().clickpos.y()
		w, h = self.fractal.get_size()
		w2 = self.label.size().width()
		h2 = self.label.size().height()
		x_coor = x*(w/w2)
		y_coor = y*(h/h2)
		self.fractal.get_thumbnail(x_coor, y_coor)
		pixmap = QPixmap('thumbnail.png')
		coors = self.fractal.get_coors(x_coor,y_coor)
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
 
	def updateStatusBar(self):
		x = self.sender().movepos.x()
		y = self.sender().movepos.y()
		w, h = self.fractal.get_size()
		w2 = self.label.size().width()
		h2 = self.label.size().height()
		x_coor = x*(w/w2)
		y_coor = y*(h/h2)
		coors = self.fractal.get_coors(x_coor,y_coor)
		self.statusbar.showMessage(str(coors))




if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Fractal_gui()
	sys.exit(app.exec_())
