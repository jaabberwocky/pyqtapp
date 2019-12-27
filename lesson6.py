import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

        def __init__(self):
            super().__init__()
            self.init_ui()

        def init_ui(self):
            self.le = QtWidgets.QLineEdit()
            self.b = QtWidgets.QPushButton("Clear")

            self.le.setPlaceholderText("Enter text here")
            self.b.clicked.connect(self.btn_click)

            v_box = QtWidgets.QVBoxLayout()
            v_box.addWidget(self.le)
            v_box.addWidget(self.b)

            self.setLayout(v_box)

            self.setWindowTitle("PyQt5 Lesson 6")
            self.show()
        
        def btn_click(self):
            self.le.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    a_window = Window()
    sys.exit(app.exec_())