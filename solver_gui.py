from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QGroupBox, \
    QGridLayout, QLabel
import sys
from PyQt5.QtCore import Qt


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

    def __init__(self):
        super().__init__()
        self.horizontalGroupBox = QGroupBox("")
        self.title = 'Sudoku Board'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.startTimer(5000)

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

    def timerEvent(self, *args, **kwargs):
        e_r, e_c = find_empty(self.board)
        print("timer? ", e_r, " ", e_c)
        if e_r == -1 and e_c == -1:
            return
        empty_row = self.board[e_r]
        empty_col = [sub[e_c] for sub in self.board]
        rr = int(e_r / 3) * 3
        cc = int(e_c / 3)
        g_c = [sub[cc * 3:cc * 3 + 3] for sub in self.board[rr:rr + 3]]
        for r_c in range(1, 10):
            if r_c not in empty_row and r_c not in empty_col and is_in_grid(g_c, r_c) is False:
                self.labels[9*e_r + e_c].setText(str(r_c))
                self.labels[9*e_r + e_c].setStyleSheet("background-color: red;")
                self.board[e_r][e_c] = r_c

    def create_grid_layout(self):
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        layout.setSpacing(0)
        for i in range(9):
            for j in range(9):
                style_val = "background-color: white;"
                label = SudokuLabel()
                label.setAlignment(Qt.AlignCenter)
                cur = self.board[i][j]
                if cur != 0:
                    label.setText(str(cur))
                    label.set_value(cur)
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
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
