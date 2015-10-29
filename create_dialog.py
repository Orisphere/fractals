from ui_create_dialog import Ui_Create_dialog
from PyQt5.QtWidgets import QDialog

class Create_dialog(QDialog, Ui_Create_dialog):

	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.setupUi(self)

