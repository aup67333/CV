import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget


class MainWindow(QWidget):
    def __init__(self):
        # Window
        super(MainWindow, self).__init__()
        self.resize(200, 150)
        self.setWindowTitle("PySide6 Demo")

        # QLabel
        self.label = QLabel(self)
        self.label.setGeometry(65, 65, 100, 10)
        self.label.setText("Hello World!")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())