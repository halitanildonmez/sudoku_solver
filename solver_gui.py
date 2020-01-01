import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber, QDialog, QPushButton, QVBoxLayout, QGroupBox, \
    QGridLayout, QHBoxLayout, QLabel, QFrame
import sys
from PyQt5.QtGui import QPainter, QBrush, QPen, QLinearGradient, QColor
from PyQt5.QtCore import Qt, QRectF


class App(QDialog):
    def __init__(self):
        super().__init__()
        self.horizontalGroupBox = QGroupBox("")
        self.title = 'Sudoku Board'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_grid_layout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()

    def create_grid_layout(self):
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        layout.setSpacing(0)

        counter = 0
        for i in range(9):
            for j in range(9):
                style_val = "background-color: white;"
                b = QLabel()
                b.setAlignment(Qt.AlignCenter)
                b.setText(str(counter))
                b.setFixedSize(80, 60)
                if j % 3 == 0 and j != 0:
                    style_val += "border-left: 3px solid black;"
                if i == 3 or i == 6:
                    style_val += "border-top: 3px solid black;"
                b.setStyleSheet(style_val)
                layout.addWidget(b, i, j)
                counter += 1

        self.horizontalGroupBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
