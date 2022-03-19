from sre_constants import CHCODES
import sys
import PySide6
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMainWindow,
    QVBoxLayout,
    QLabel,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Counter App")

        self.counter = 0

        self.counter_label = QLabel(str(self.counter))
        self.counter_label.setAlignment(Qt.AlignCenter)
        self.counter_label.setFont(QFont("Arial", 22))

        self.increment_btn = QPushButton("Increment")
        self.increment_btn.clicked.connect(self.increment)

        self.decrement_btn = QPushButton("Decrement")
        self.decrement_btn.clicked.connect(self.decrement)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.counter_label)
        v_layout.addWidget(self.increment_btn)
        v_layout.addWidget(self.decrement_btn)
        v_layout.setAlignment(Qt.AlignHCenter)

        container = QWidget()
        container.setLayout(v_layout)

        self.setCentralWidget(container)

    def increment(self):
        self.counter += 1
        self.counter_label.setText(str(self.counter))

    def decrement(self):
        self.counter -= 1
        self.counter_label.setText(str(self.counter))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
