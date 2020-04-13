import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette

def main():
    app = QApplication([])
    app.setStyle('Fusion')

    qp = QPalette()
    qp.setColor(QPalette.ButtonText, Qt.black)
    qp.setColor(QPalette.Window, Qt.red)
    qp.setColor(QPalette.Button, Qt.gray)

    app.setPalette(qp)

    w = QWidget()
    w.setWindowTitle('Musketeers')

    grid = QGridLayout(w)

    grid.addWidget(QPushButton('Button one'), 0, 0)
    grid.addWidget(QPushButton('Button two'), 0, 1)
    grid.addWidget(QPushButton('Button three'), 1, 0)
    grid.addWidget(QPushButton('Button four'), 1, 1)
    grid.addWidget(QPushButton('Button five'), 2, 0, 1, 0)

    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()