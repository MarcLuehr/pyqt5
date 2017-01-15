import sys
from PyQt5.QtWidgets import QApplication, QDialog
from testWidget import Ui_Form

def handleClick(self):
	print("click")


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Form()
ui.setupUi(window)

ui.exitButton.clicked.connect(handleClick)

window.show()
sys.exit(app.exec_())
