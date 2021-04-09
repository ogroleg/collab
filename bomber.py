import functools
import random
import sys
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from test import App


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Bomber'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 250
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.buttons = []

        # TODO: add random integer numbers here
        self.bomb_row = 3
        self.bomb_column = 3

        # TODO: replace ... with numbers
        for row in range(3):
            for column in range(3):
                button = QPushButton(f'Multiply {x}', self)
                # TODO: replace ... with numbers (coordinates)
                button.move(10, 50)

                self.buttons.append(button)

                # TODO: add missing variables here
                button.clicked.connect(functools.partial(
                    self.on_click_button,
                    button = button,
                    button_row = button_row,
                    button_column = button_column
                ))

                # connect button to function on_click

                self.show()

            @pyqtSlot()
            def on_click_button(self, button, button_row, button_column):
                # TODO: finish this function
                if button_row == self.bomb_row and button_column == self.bomb_column:  # it's the bomb!
                    button.setText("It's a bomb!")
                    QMessageBox.question(self, 'Result', '...', QMessageBox.OK, QMessageBox.OK)
                else:  # not a bomb, mark button as empty
                    button.setText('empty')

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())
