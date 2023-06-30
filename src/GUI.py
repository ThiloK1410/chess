import sys
from PyQt6.QtCore import QFile, QTextStream
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, \
    QLabel
from PyQt6.QtGui import QIcon


# defining of the applications layout and functionality
class GUI(QWidget):
    timer_modes = ["Bullet", "Blitz", "Rapid", "Classical"]
    game_modes = ["Computer", "Two Player", "Analysis Board"]
    current_timer = {"timer": 0, "increment": 0}

    def __init__(self):

        # defining the window
        super().__init__()
        self.setWindowTitle("Chess Configurator")
        self.setWindowIcon(QIcon('../media/icons/knight_icon.ico'))
        self.setMinimumSize(700, 100)  # width, height

        # creating the layouts
        page_layout = QVBoxLayout()
        self.setLayout(page_layout)
        btn_layout = QHBoxLayout()
        custom_timer_layout = QHBoxLayout()

        # defining the widgets
        self.gamemode_label = QLabel("Set Timer:")

        self.bullet_btn = QPushButton("Bullet 1+0")
        self.blitz_btn = QPushButton("Blitz 3+2")
        self.rapid_btn = QPushButton("Rapid 10+5")
        self.classical_btn = QPushButton("Classical 30+20")

        self.custom_radio_btn = QRadioButton("Set Custom Time")
        self.custom_radio_btn.toggled.connect(self.toggle_custom_settings)

        self.timer_label = QLabel("Timer:")
        self.incr_label = QLabel("Increment:")

        self.timer_edit = QLineEdit()
        self.timer_edit.setPlaceholderText("in minutes")

        self.incr_edit = QLineEdit()
        self.incr_edit.setPlaceholderText("in seconds")

        # giving the widgets names for referral in css
        self.timer_label.setObjectName("timer_label")
        self.incr_label.setObjectName("incr_label")

        # adding widgets to the layout
        page_layout.addWidget(self.gamemode_label)
        page_layout.addLayout(btn_layout)

        buttons = [self.bullet_btn, self.blitz_btn, self.rapid_btn, self.classical_btn]
        for x in buttons: btn_layout.addWidget(x)

        page_layout.addLayout(custom_timer_layout)

        custom_timer_layout.addWidget(self.custom_radio_btn)
        self.custom_settings_widgets = [self.timer_label, self.timer_edit, self.incr_label, self.incr_edit]
        for x in self.custom_settings_widgets: custom_timer_layout.addWidget(x)
        self.toggle_custom_settings(False)

        # Apply styles from a CSS file
        with open("style.css", "r") as fh:
            app.setStyleSheet(fh.read())

    def set_current_timer(self, timer, increment):
        self.current_timer["timer"] = timer
        self.current_timer["increment"] = increment

    def toggle_custom_settings(self, checked):
        for x in self.custom_settings_widgets:
            x.setEnabled(checked)


# starts the PyQt Applet
if __name__ == '__main__':
    app = QApplication([])
    window = GUI()
    window.show()
    app.exec()
