import sys
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from mandelbrot_set import Mandelbrot
from new_dialog import Zoom_dialog
from main_window import Ui_MainWindow
from fractal_label import Fractal_label
from iter_dialog import Iter_dialog
from save_dialog import Save_dialog
from info_dialog import Info_dialog
from create_dialog import Create_dialog



class Fractal_gui(QMainWindow, Ui_MainWindow):

	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.initUI()

	def initUI(self):
		fractal = Mandelbrot(w=300, h=200)
		self.label.setScaledContents(False)
		self.updateLabel(fractal)

		self.history = []
		self.history.append(self.fractal)
		self.current_index = 0
		
		
		self.label.dblclicked.connect(self.showDialog)
		self.label.moved.connect(self.updateStatusBar)
	
		self.actionUndo.triggered.connect(self.undo)
		self.actionRedo.triggered.connect(self.redo)
	#	self.actionExit.triggered.connect(self.quit())
		self.actionSave_As.triggered.connect(self.saveDialog)
		self.actionSave.triggered.connect(self.save)
		self.actionGet_Info.triggered.connect(self.infoDialog)
	#	self.actionCreate.triggered.connect(self.createDialog)
		self.incItr.triggered.connect(self.iterMenu)

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
			self.updateLabel(m)
			self.updateHistory()
	
	def saveDialog(self):
		d = Save_dialog()

		if d.exec_():
			filename = d.get_filename()
			self.fractal.save_image(filename)
	
	def createDialog(self):
		d = Create_dialog()

		if d.exec_():
			print("hi")

	def save(self):
		self.saveDialog()

	
	def iterMenu(self):
		current_iter = str(self.fractal.it)
		d = Iter_dialog()
		d.currentItr.setText(current_iter)

		if d.exec_():
			iters = d.get_iter()
			self.fractal.inc_itr(int (iters))
			self.fractal.to_rgb_array()
			self.fractal.to_image()
			self.updateLabel(self.fractal)
			self.updateHistory()

	
	def infoDialog(self):
		x = str(self.fractal.center_x)
		y = str(self.fractal.center_y)
		height = str(self.fractal.height)
		width = str(self.fractal.width)
	
		zoom = str(self.fractal.get_zoom())
		iters = str(self.fractal.it)
		center = '(' + x + ', '+ y + ')'
		size = width + 'x' + height
		d = Info_dialog()
		d.center.setText(center)
		d.iters.setText(iters)
		d.zoom.setText(zoom)
		d.dims.setText(size)
		d.exec_()

		
	
	def undo(self):
		if self.current_index > 0: 
			self.updateLabel(self.history[self.current_index-1])
			self.current_index -= 1
	
	def redo(self):
		if self.current_index < len(self.history)-1: 
			self.updateLabel(self.history[self.current_index+1])
			self.current_index += 1


	def updateLabel(self, frac):
		self.fractal = frac

		p = QPixmap()
		p.loadFromData(Mandelbrot.to_string_object(frac.image))
		self.label.set_label(p)

	
	def updateHistory(self):
		self.current_index += 1

		if (self.current_index + 1) > len(self.history):
			self.history.append(self.fractal)
		else:
			self.history[self.current_index] = self.fractal
			del self.history[self.current_index+1:]

		if len(self.history) > 10:
			self.history = self.history[self.current_index-9:]
			self.current_index = len(self.history)-1
	

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
