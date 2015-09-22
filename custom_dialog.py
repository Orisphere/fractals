import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QColorDialog, QDialog, QHBoxLayout,QInputDialog, QLabel, QComboBox, QDialogButtonBox)
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5 import QtCore
from PIL import Image
from mandelbrot_set import Mandelbrot

class Custom_dialog(QDialog):
	def __init__(self):
		super(Custom_dialog, self).__init__()
		self.init_dialog()
	
	def init_dialog(self):
		self.setGeometry(300, 300, 250, 150)
		hbox = QHBoxLayout(self)
		button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
		
		zoom = QComboBox(self)
		zoom.addItem("1")
		zoom.addItem("10")
		zoom.addItem("100")
		
		zoom.activated[str].connect(self.on_activated)
		hbox.addWidget(button_box)	
		self.show()
	
	def on_activated(self):
		print("Made it")

if __name__ == '__main__':

	app = QApplication(sys.argv)
	c = Custom_dialog()
	sys.exit(app.exec_())
