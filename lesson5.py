import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton("Push me")
        self.l = QtWidgets.QLabel("I have not been clicked yet!")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("PyQt5 Lesson 5")

        # button behaviour
        self.b.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        # note: the properties of each QWidget is returned in a function, and not attribute
        if self.l.text() == "I have been clicked!":
            self.l.setText("I have not been clicked yet!")
        else:
            self.l.setText("I have been clicked!")
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a_window = Window()
    sys.exit(app.exec_())