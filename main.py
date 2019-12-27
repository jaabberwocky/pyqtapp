import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w) # add label to window, so pass it as arg
    l1.setText("Hello world")

    l2 = QtWidgets.QLabel(w)
    l2.setPixmap(QtGui.QPixmap('globe.png').scaledToWidth(64))

    w.setWindowTitle('Tobias PyQt5 Lesson 1')
    w.setGeometry(100, 100, 300, 200)
    l1.move(130, 20)
    l2.move(120, 90)
    w.show()
    sys.exit(app.exec_())

window()