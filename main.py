import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle('Tobias PyQt5 Lesson 1')
    w.show()
    sys.exit(app.exec_())

window()