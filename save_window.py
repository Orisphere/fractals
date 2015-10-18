from save_dialog import Ui_Dialog
from PyQt5.QtWidgets import QDialog

class Save_dialog(QDialog, Ui_Dialog):

	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.setupUi(self)


	def get_filename(self):
		return self.fileName.text()

