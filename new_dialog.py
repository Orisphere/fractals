from design import Ui_Dialog
from PyQt5.QtWidgets import QDialog

class Zoom_dialog(QDialog, Ui_Dialog):

	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.zoom = self.comboBox.currentText()
		self.comboBox.activated[str].connect(self.set_zoom)

	def set_zoom(self, text):
		self.zoom = text

	def get_zoom(self):
		return self.zoom

	def set_fractal(self, pixmap):
		self.fractal_label.setPixmap(pixmap)

	def set_coors(self, coors):
		self.label.setText(coors)

