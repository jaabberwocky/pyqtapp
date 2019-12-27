import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()

    # widgets
    l = QtWidgets.QLabel(w) # add label to window, so pass it as arg
    l.setText("Look at me")

    b = QtWidgets.QPushButton(w)
    b.setText("Push me")

    globe = QtGui.QPixmap('globe.png').scaledToWidth(64)
    p = QtWidgets.QLabel(w)
    p.setPixmap(globe)

    # box layout
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)

    ## this makes it all centred by stacking two Stretch on top of each widget for each horizontal box
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(l)
    h_box.addStretch()

    h_box2 = QtWidgets.QHBoxLayout()
    h_box2.addStretch()
    h_box2.addWidget(p)
    h_box2.addStretch()
    
    v_box.addLayout(h_box)
    v_box.addLayout(h_box2)
    w.setWindowTitle('pyqt5')
    w.setGeometry(100, 100, 300, 200)
    w.setLayout(v_box)

    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()