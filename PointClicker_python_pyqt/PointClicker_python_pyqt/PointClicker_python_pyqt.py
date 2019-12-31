import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidget
from PyQt5.QtGui import QIcon, QPicture
from PyQt5.QtCore import QSize
from pointClickerGame import pointclickergame

pcg = pointclickergame()
pcg.load()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.initList()

    def initList(self):
        global pcg
        self.List = QListWidget(self)
        self.List.setGeometry(10, 120, 380, 180)
        for i in range(0, pcg.upgrades_capacity):
            self.List.insertItem(i, pcg.upgrades[i].name + "\t" + str(pcg.upgrades[i].amount) + "\t" + str(pcg.upgrades[i].cost))
        self.List.setStyleSheet("background-color: #7d25f7; color: black; font-size: 26px;")
        self.List.show()

    def initUI(self):
        self.setGeometry(250, 100, 400, 400)
        self.setWindowTitle("PointClicker")
        self.setWindowIcon(QIcon("images/ico.png"))
        self.setMinimumSize(400, 400)
        self.setMaximumSize(400, 400)
        self.setStyleSheet("background-color: #254cf7")

        self.Button = QPushButton(QIcon("images/button.jpg"), "Click!", self)
        self.Button.setGeometry(140, 30, 120, 50)
        self.Button.setIconSize(QSize(45, 45))
        self.Button.setStyleSheet("background-color: #7d25f7; color: black; font-size: 26px;")
        self.Button.show()

        self.ButtonExit = QPushButton("Exit", self)
        self.ButtonExit.setStyleSheet("background-color: #7d25f7; color: black; font-size: 26px;")
        self.ButtonExit.move(65, 350)
        self.ButtonExit.setMinimumHeight(40)
        self.ButtonExit.clicked.connect(lambda: exit(0))
        self.ButtonExit.show()

        self.ButtonBuy = QPushButton("Buy", self)
        self.ButtonBuy.setGeometry(200, 350, 90, 40)
        self.ButtonBuy.setStyleSheet("background-color: #7d25f7; color: black; font-size: 26px;")
        self.ButtonBuy.show()

def main():
    application = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(application.exec())

if(__name__ == "__main__"):
    main()
