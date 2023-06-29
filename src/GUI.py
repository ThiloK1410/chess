import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess Configurator")
        self.setWindowIcon(QIcon('../media/icons/knight_icon.ico'))
        self.resize(500, 300) # width, height

app = QApplication(sys.argv)

window = MyApp()
window.show()

app.exec()

