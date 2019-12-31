import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setGeometry(250, 100, 400, 400)
        self.setWindowTitle("PointClicker")


def main():
    application = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(application.exec())

if(__name__ == "__main__"):
    main()
