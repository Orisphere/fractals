from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, QObject, Qt


class Fractal_label(QLabel):
	dblclicked = pyqtSignal()
	moved = pyqtSignal()

	def __init__(self, parent=None):
		super().__init__(parent)
		self.setMouseTracking(True)
		
	def mouseMoveEvent(self, event):
		self.movepos = event.pos()
		self.moved.emit()
	#if event.buttons() == Qt.LeftButton:
		#	print(event.oldPos())
	
	def mouseDoubleClickEvent(self, event):
		self.clickpos = event.pos()
		self.dblclicked.emit()

	
	def set_label(self, pixmap):
		scaled_pixmap = pixmap.scaled(900, 600, aspectRatioMode=Qt.KeepAspectRatio)	
		self.setPixmap(scaled_pixmap)

