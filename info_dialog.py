from ui_info_dialog import Ui_Info_dialog
from PyQt5.QtWidgets import QDialog

class Info_dialog(QDialog, Ui_Info_dialog):

	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.setupUi(self)

