from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QGroupBox, \
    QGridLayout, QLabel
import sys
import time
from PyQt5.QtCore import Qt, QTime, QTimer


class SudokuLabel(QLabel):
    int_value = -1

    def __init__(self):
        QLabel.__init__(self)

    def get_value(self):
        return self.int_value

    def set_value(self, new_value):
        self.int_value = new_value


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return -1, -1


def is_in_grid(grid, val):
    for row in grid:
        if val in row:
            return True
    return False


class App(QDialog):
    labels = []
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    tried_locs = []

    def __init__(self):
        super().__init__()
        self.horizontalGroupBox = QGroupBox("")
        self.title = 'Sudoku Board'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        QTimer.singleShot(5000, self.solveBoard)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_grid_layout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()

    def showEvent(self, event):
        self.initUI()

    def solveBoard(self):
        if len(self.labels) == 0:
            return
        e_r, e_c = find_empty(self.board)
        if e_r == -1 and e_c == -1:
            return True
        empty_row = self.board[e_r]
        empty_col = [sub[e_c] for sub in self.board]

        grid_row_index = int(e_r / 3) * 3
        grid_col_index = int(e_c / 3)

        g_c = [sub[grid_col_index * 3:grid_col_index * 3 + 3] for sub in self.board[grid_row_index:grid_row_index + 3]]
        for cur_row_index in range(1, 10):
            time.sleep(1)
            self.labels[9 * e_r + e_c].setText(str(cur_row_index))
            self.labels[9 * e_r + e_c].setStyleSheet("background-color: red;")
            self.repaint()
            if cur_row_index not in empty_row and \
                    cur_row_index not in empty_col and \
                    is_in_grid(g_c, cur_row_index) is False:
                self.board[e_r][e_c] = cur_row_index
                if self.solveBoard():
                    return True
        self.board[e_r][e_c] = 0
        self.labels[9 * e_r + e_c].setText("")
        self.labels[9 * e_r + e_c].setStyleSheet("background-color: white;")
        return False

    def create_grid_layout(self):
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        layout.setSpacing(0)
        for i in range(9):
            for j in range(9):
                style_val = "background-color: white;"
                label = SudokuLabel()
                font = QFont()
                font.setBold(True)
                font.setPointSize(20)
                label.setAlignment(Qt.AlignCenter)
                label.setFont(font)
                cur = self.board[i][j]
                if cur != 0:
                    label.setText(str(cur))
                    label.set_value(cur)
                else:
                    label.set_value(0)
                label.setFixedSize(80, 60)
                if j % 3 == 0 and j != 0:
                    style_val += "border-left: 3px solid black;"
                if i == 3 or i == 6:
                    style_val += "border-top: 3px solid black;"
                label.setStyleSheet(style_val)
                self.labels.append(label)
                layout.addWidget(label, i, j)
        self.horizontalGroupBox.setLayout(layout)


if __name__ == '__main__':
    li = [1, 2, 4]
    b = li[1]
    b = 55
    print(li)
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
