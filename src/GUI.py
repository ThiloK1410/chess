import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

# defining of the applications layout and functionality
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess Configurator")
        self.setWindowIcon(QIcon('../media/icons/knight_icon.ico'))
        self.resize(500, 300) # width, height
        self.setMinimumSize(200, 100)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # widgets
        self.inputField = QLineEdit()
        button = QPushButton("&Say Hello", clicked=self.say_hello)
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def say_hello(self):
        inputText = self.inputField.text()
        self.output.setText("Hello {0}".format(inputText))

# creates the application and runs it
app = QApplication(sys.argv)

# style for the applications widgets
app.setStyleSheet('''
    QWidget {
        font-size: 25px;
    }
    
    QPushButtion {
        font-size: 20px;
    }
''')

# adds window to the application, MyApp() is the predefined program from above
window = MyApp()
window.show()

app.exec()

