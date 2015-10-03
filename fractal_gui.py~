import sys
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from mandelbrot_set import Mandelbrot
from new_dialog import Zoom_dialog
from main_design import Ui_MainWindow
from fractal_label import Fractal_label



class Fractal_gui(QMainWindow, Ui_MainWindow):

	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.initUI()

	def initUI(self):
		self.fractal = Mandelbrot(w=300, h=200)
		self.fractal.to_image()
		
		self.history = []
		self.history.append(self.fractal)
		self.current_index = 0
		
		p = QPixmap()
		p.loadFromData(Mandelbrot.to_string_object(self.fractal.image))
		self.label.setScaledContents(False)
		self.label.set_label(p)
		self.label.dblclicked.connect(self.showDialog)
		self.label.moved.connect(self.updateStatusBar)
	
		self.actionUndo.triggered.connect(self.undo)
		self.actionRedo.triggered.connect(self.redo)	

		self.show()

	def showDialog(self):
		x = self.sender().clickpos.x()
		y = self.sender().clickpos.y()
		w, h = self.fractal.get_size()
		w2 = self.label.size().width()
		h2 = self.label.size().height()
		
		x_coor = x*(w/w2)
		y_coor = y*(h/h2)
		
		im = self.fractal.get_thumbnail(x_coor, y_coor)
		pixmap = QPixmap()
		pixmap.loadFromData(Mandelbrot.to_string_object(im))
		coors = self.fractal.get_coors(x_coor,y_coor)
		
		d = Zoom_dialog()
		d.set_fractal(pixmap)
		d.set_coors(str(coors))	
		
		if d.exec_():
			zoom = int(d.get_zoom())*self.fractal.get_zoom()
			m = Mandelbrot(z=zoom,center=coors)
			m.to_image()
			p = QPixmap()
			p.loadFromData(Mandelbrot.to_string_object(m.image))
			self.label.set_label(p)
			self.fractal = m
			self.history.append(m)
			self.current_index += 1
	
	def undo(self):
		if self.current_index > 0: 
			self.fractal = self.history[self.current_index-1]
			p = QPixmap()
			p.loadFromData(Mandelbrot.to_string_object(self.fractal.image))		
			self.label.set_label(p)
			self.current_index -= 1
	
	def redo(self):
		if self.current_index < len(self.history)-1: 
			self.fractal = self.history[self.current_index+1]
			p = QPixmap()
			p.loadFromData(Mandelbrot.to_string_object(self.fractal.image))		
			self.label.set_label(p)
			self.current_index += 1


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
