from dialog2 import Ui_Dialog
from PyQt5.QtWidgets import QDialog

class Iter_dialog(QDialog, Ui_Dialog):

	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.setupUi(self)
		self.iters = self.lineEdit.text()

	def set_old_iter(self, text):
		self.currentIter = text

	def get_iter(self):
		return self.iters

