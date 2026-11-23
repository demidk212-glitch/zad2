import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        x = random.randint(0, self.width())
        y = random.randint(50, self.height())
        d = random.randint(10, 100)
        self.circles.append((x, y, d))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        for x, y, d in self.circles:
            painter.drawEllipse(x - d // 2, y - d // 2, d, d)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())