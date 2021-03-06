import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class Color_slider(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 280, 270)
		self.setWindowTitle("Paint test")
		self.show
	
	def paintEvent(self, event):
		qp = QPainter()
		qp.begin(self)
		self.drawLines(qp)
		qp.end()

	def drawLines(self, qp):
		pen = QPen(Qt.black, 2, Qt.SolidLine)
		qp.setPen(pen)
		qp.drawLine(20, 40, 250, 40)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Color_slider()
	sys.exit(app.exec_())
	
	
