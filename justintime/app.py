import sys
import os
from time import strftime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLCDNumber, QVBoxLayout
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer


class Example(QWidget):

    now = QTime.currentTime()
    timeLeft = 0


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btnPom = QPushButton('Pomodoro', self)
        btnPom.clicked.connect(self.setPom)
        btnPom.resize(btnPom.sizeHint())
        btnPom.move(0, 0)

        btnBreak = QPushButton('Short Break', self)
        btnBreak.clicked.connect(self.setBreak)
        btnBreak.resize(btnBreak.sizeHint())
        btnBreak.move(95, 0)

        btnLBreak = QPushButton('Long Break', self)
        btnLBreak.clicked.connect(self.setLBreak)
        btnLBreak.resize(btnLBreak.sizeHint())
        btnLBreak.move(200, 0)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Time)
        self.timer.start(1000)

        self.lcdTime = QLCDNumber(self)
        self.lcdTime.display(strftime("%H" + ":" + "%M" + ":" + "%S"))
        self.lcdTime.setDigitCount(8)
        self.lcdTime.setGeometry(0, 175, 400, 100)
        lcdTimePal = self.lcdTime.palette()
        lcdTimePal.setColor(lcdTimePal.WindowText, Qt.green)
        lcdTimePal.setColor(lcdTimePal.Light, Qt.green)
        self.lcdTime.setPalette(lcdTimePal)

        self.lcdCountdown = QLCDNumber(self)
        self.lcdCountdown.display('00:00')
        self.lcdCountdown.setDigitCount(5)
        self.lcdCountdown.setGeometry(0, 75, 400, 100)
        lcdCountPal = self.lcdTime.palette()
        lcdCountPal.setColor(lcdTimePal.WindowText, Qt.red)
        lcdCountPal.setColor(lcdTimePal.Light, Qt.red)
        self.lcdCountdown.setPalette(lcdCountPal)

        self.setGeometry(0, 0, 400, 300)
        self.setWindowTitle('Justin Time')
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        self.show()

    def Time(self):
        self.lcdTime.display(strftime("%H" + ":" + "%M" + ":" + "%S"))

        if self.timeLeft > 1:
            self.timeLeft -= 1
        elif self.timeLeft == 1:
            os.system("""osascript -e 'display notification "{}" with title "{}"'""".format("Time Expired!", "Your time is up!"))
            self.timeLeft -= 1

        minutes = int(self.timeLeft / 60)
        seconds = self.timeLeft % 60

        if minutes < 10:
            minutes = '0' + str(minutes)

        if seconds < 10:
            seconds = '0' + str(seconds)

        timeString = str(minutes) + ':' + str(seconds)
        self.lcdCountdown.display(timeString)


    def setPom(self):
        self.timeLeft = 1500

    def setBreak(self):
        self.timeLeft = 300

    def setLBreak(self):
        self.timeLeft = 900


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    #clock = DigitalClock()
    #clock.show()
