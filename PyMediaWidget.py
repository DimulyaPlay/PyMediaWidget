import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QSystemTrayIcon, QMenu, QLabel
from PyQt5.QtGui import QIcon, QPainter, QLinearGradient, QColor, QPalette, QCursor
from PyQt5.QtCore import Qt, QPoint
import pyautogui


class MediaControlWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # Прозрачный фон
        self.oldPosition = QPoint(10,10)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Управление плеером')
        self.setGeometry(10, 10, 110, 110)

        self.layout = QHBoxLayout()

        # Стилизация кнопок
        buttonStyle = """
        QPushButton {
            border: 2px solid #8f8f91;
            border-radius: 6px;
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #f6f7fa, stop:1 #dadbde);
            min-height: 20px;
            font-size: 12px;
            min-width: 20px;
        }
        QPushButton:pressed {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #dadbde, stop:1 #f6f7fa);
        }
        """

        # Создание кнопок
        self.playPauseButton = QPushButton('▶️⏸️')
        self.playPauseButton.clicked.connect(self.playPause)
        self.layout.addWidget(self.playPauseButton)

        self.prevButton = QPushButton('⏮️')
        self.prevButton.clicked.connect(self.prevTrack)
        self.layout.addWidget(self.prevButton)

        self.nextButton = QPushButton('⏭️')
        self.nextButton.clicked.connect(self.nextTrack)
        self.layout.addWidget(self.nextButton)

        # Добавляем кнопки управления громкостью
        self.volumeDownButton = QPushButton('🔉')
        self.volumeDownButton.clicked.connect(self.volumeDown)
        self.layout.addWidget(self.volumeDownButton)

        self.volumeUpButton = QPushButton('🔊')
        self.volumeUpButton.clicked.connect(self.volumeUp)
        self.layout.addWidget(self.volumeUpButton)


        # Создаем лейбл для перемещения
        self.moveLabel = QLabel('👌', self)
        self.moveLabel.setAlignment(Qt.AlignCenter)
        self.moveLabel.setStyleSheet("font-size: 20px;")
        self.layout.addWidget(self.moveLabel)

        # Применение стилей
        self.playPauseButton.setStyleSheet(buttonStyle)
        self.nextButton.setStyleSheet(buttonStyle)
        self.prevButton.setStyleSheet(buttonStyle)
        self.volumeUpButton.setStyleSheet(buttonStyle)
        self.volumeDownButton.setStyleSheet(buttonStyle)
        self.setLayout(self.layout)

    # перезаписываем пресс и мув ивенты для перетаскивания виждета по экрану
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button()==2:
            sys.exit(0)

    def mouseMoveEvent(self, event):
        self.drag = True
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    def playPause(self):
        pyautogui.press('playpause')

    def nextTrack(self):
        pyautogui.press('nexttrack')

    def prevTrack(self):
        pyautogui.press('prevtrack')

    def volumeUp(self):
        pyautogui.press('volumeup')

    def volumeDown(self):
        pyautogui.press('volumedown')

def main():
    app = QApplication(sys.argv)
    ex = MediaControlWidget()
    ex.show()
    sys.exit(app.exec_())

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

if __name__ == '__main__':
    main()


