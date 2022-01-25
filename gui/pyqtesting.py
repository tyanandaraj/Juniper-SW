import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    # initializing QMainWindow object (constructor)
    def __init__(self):
        #
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Juniper Networks Loopback Verification")
        self.initUI()

    def initUI(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Hello World!")
        self.label1.move(100, 50)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Click")
        # connecting button click event to appropriate function
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        self.label1.setText("You pressed the button")
        self.update()

    def update(self):
        self.label1.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    # Assures "clean exit" when x button clicked
    sys.exit(app.exec_())

window()
