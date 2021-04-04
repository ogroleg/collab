import sys
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Calculator'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 250
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # create label
        self.label = QLabel('No result yet', self)
        self.label.move(20, 200)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(100, 40)
        self.textbox_2 = QLineEdit(self)
        self.textbox_2.move(20, 80)
        self.textbox_2.resize(100, 40)

        # Create a button in the window
        self.button = QPushButton('Multiply', self)
        self.button_2 = QPushButton('Add', self)
        self.button_3 = QPushButton('minus', self)
        self.button_4 = QPushButton('divide', self)
        self.button.move(20, 120)
        self.button_2.move(120, 120)
        self.button_3.move(220, 120)
        self.button_4.move(320, 120)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.button_2.clicked.connect(self.on_click_2)
        self.button_3.clicked.connect(self.on_click_3)
        self.button_4.clicked.connect(self.on_click_4)
        self.show()

    @pyqtSlot()
    def on_click(self):
        first_number = int(self.textbox.text())
        second_number = int(self.textbox_2.text())
        result = first_number * second_number
        #QMessageBox.question(self, 'Calculator', f'Here is the result: {result}', QMessageBox.Abort | QMessageBox.Save, QMessageBox.Save)
        self.label.setText(f'Result: {result}')
        self.textbox.setText("")
        self.textbox_2.setText("")

    @pyqtSlot()
    def on_click_2(self):
        first_number = int(self.textbox.text())
        second_number = int(self.textbox_2.text())
        result = first_number + second_number
        #QMessageBox.question(self, 'Calculator', f'Here is the result: {result}', QMessageBox.Abort | QMessageBox.Save, QMessageBox.Save)
        self.label.setText(f'Result: {result}')
        self.textbox.setText("")
        self.textbox_2.setText("")

    @pyqtSlot()
    def on_click_3(self):
        first_number = int(self.textbox.text())
        second_number = int(self.textbox_2.text())
        result = first_number - second_number
        #QMessageBox.question(self, 'Calculator', f'Here is the result: {result}', QMessageBox.Save | QMessageBox.Ok, QMessageBox.Save)
        self.label.setText(f'Result: {result}')
        self.textbox.setText("")
        self.textbox_2.setText("")

    @pyqtSlot()
    def on_click_4(self):
        first_number = int(self.textbox.text())
        second_number = int(self.textbox_2.text())
        result = first_number / second_number
        #QMessageBox.question(self, 'Calculator', f'Here is the result: {result}', QMessageBox.Abort | QMessageBox.Save, QMessageBox.Save)
        self.label.setText(f'Result: {result}')
        self.textbox.setText("")
        self.textbox_2.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
