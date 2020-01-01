import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidget, QListWidgetItem, QLabel
from PyQt5.QtGui import QIcon, QPicture
from PyQt5.QtCore import QSize, QTimer
from pointClickerGame import pointclickergame

pcg = pointclickergame()
pcg.load()

def EXIT():
    global pcg
    pcg.save()
    exit(0)

def CLICK(Score, PPS):
    global pcg
    pcg.command(0)
    Score.setText("Score : " + str(pcg.score))
    PPS.setText("PPS : " + str(pcg.pps))

def BUY(items_list):
    global pcg
    pcg.command(int( str(str(items_list[0].text()).split("\t")[0]).split("Autoclick")[1]))

def UPDATE(Score, PPS, Timer, List):
    global pcg
    pcg.add_pps()
    Score.setText("Score : " + str(pcg.score))
    PPS.setText("PPS : " + str(pcg.pps))
    for i in range(1, List.count()):
        List.item(i-1).setText(pcg.upgrades[i].name + "\t" + str(pcg.upgrades[i].amount) + "\t" + str(pcg.upgrades[i].cost))
    Timer.start(1000)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initList()
        self.initUI()
        self.show()

    def initList(self):
        global pcg
        self.List = QListWidget(self)
        self.List.setGeometry(10, 120, 380, 180)
        for i in range(1, pcg.upgrades_capacity):
            item = QListWidgetItem(pcg.upgrades[i].name + "\t" + str(pcg.upgrades[i].amount) + "\t" + str(pcg.upgrades[i].cost))
            item.setToolTip(pcg.upgrades[i].description)
            self.List.insertItem(i-1, item)
        self.List.setStyleSheet("background-color: #7d25f7; color: black; font-size: 26px;")
        self.List.show()

    def initUI(self):
        global pcg
        self.setGeometry(250, 100, 400, 400)
        self.setWindowTitle("PointClicker")
        self.setWindowIcon(QIcon("images/ico.png"))
        self.setMinimumSize(400, 400)
        self.setMaximumSize(400, 400)
        self.setStyleSheet("background-color: #254cf7")

        self.ScoreLabel = QLabel("Score : " + str(pcg.score), self)
        self.ScoreLabel.setGeometry(10, 10, 300, 25)
        self.ScoreLabel.setStyleSheet("color: yellow; font-size: 26px;")
        self.ScoreLabel.show()
        
        self.PPSLabel = QLabel("PPS : " + str(pcg.pps), self)
        self.PPSLabel.setGeometry(250, 10, 300, 25)
        self.PPSLabel.setStyleSheet("color: yellow; font-size: 26px;")
        self.PPSLabel.show()

        self.Button = QPushButton(QIcon("images/button.jpg"), "Click!", self)
        self.Button.setGeometry(140, 40, 120, 50)
        self.Button.setIconSize(QSize(45, 45))
        self.Button.setStyleSheet("background-color: #7d25f7; color: black; font-size: 26px;")
        self.Button.clicked.connect(lambda: CLICK(self.ScoreLabel, self.PPSLabel))
        self.Button.show()

        self.ButtonExit = QPushButton("Exit", self)
        self.ButtonExit.setStyleSheet("background-color: #7d25f7; color: black; font-size: 26px;")
        self.ButtonExit.move(65, 350)
        self.ButtonExit.setMinimumHeight(40)
        self.ButtonExit.clicked.connect(EXIT)
        self.ButtonExit.show()

        self.ButtonBuy = QPushButton("Buy", self)
        self.ButtonBuy.setGeometry(200, 350, 90, 40)
        self.ButtonBuy.setStyleSheet("background-color: #7d25f7; color: black; font-size: 26px;")
        self.ButtonBuy.clicked.connect(lambda: BUY(self.List.selectedItems()))
        self.ButtonBuy.show()

        self.Timer = QTimer(self)
        self.Timer.start(1000)
        self.Timer.timeout.connect(lambda: UPDATE(self.ScoreLabel, self.PPSLabel, self.Timer, self.List))

def main():
    application = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(application.exec())

if(__name__ == "__main__"):
    main()
