import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# QIcon 아이콘을 사용하기 위한 모듈
# QPushButton 버튼을 사용하기 위한 모듈
# QMainWindow 아래 활성화를 표기하기 위한 모듈


class MyApp(QWidget):

    switch_window2 = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('img/ddang.jpg'))

        self.setWindowTitle("땡칠이 박물관")
        self.setGeometry(500, 200, 520, 500)

        btn_a = QPushButton("기념관", self)
        btn_a.move(20, 50)
        btn_a.resize(btn_a.sizeHint())
        btn_a.clicked.connect(self.ddang)

        btn_b = QPushButton("기념관2", self)
        btn_b.move(20, 100)
        btn_b.resize(btn_b.sizeHint())
        btn_b.clicked.connect(self.ddang_a)

        btn_c = QPushButton("기념관3", self)
        btn_c.move(20, 150)
        btn_c.resize(btn_c.sizeHint())
        btn_c.clicked.connect(self.ddang_b)

        btn_d = QPushButton("기념관4", self)
        btn_d.move(20, 200)
        btn_d.resize(btn_d.sizeHint())
        btn_d.clicked.connect(self.ddang_c)

        btn_q = QPushButton("종료", self)
        btn_q.move(20, 250)
        btn_q.resize(btn_c.sizeHint())
        btn_q.clicked.connect(self.quit)

    def ddang(self):
        layout = QGridLayout()

        g4 = QLabel(self)
        graph4 = QPixmap('img\ddang.jpg')
        graph4 = graph4.scaledToWidth(600)
        g4.setPixmap(graph4)
        layout.addWidget(g4, 1, 1)

        self.button = QPushButton('Go back')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button,0,1)
        self.setLayout(layout)

    def ddang_a(self):
        layout = QGridLayout()

        g4 = QLabel(self)
        graph4 = QPixmap('img\ddang_a.jpg')
        graph4 = graph4.scaledToWidth(600)
        g4.setPixmap(graph4)
        layout.addWidget(g4, 1, 1)

        self.button = QPushButton('Go back')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button,0,1)
        self.setLayout(layout)

    def ddang_b(self):
        layout = QGridLayout()

        g4 = QLabel(self)
        graph4 = QPixmap('img\ddang_b.jpg')
        graph4 = graph4.scaledToWidth(600)
        g4.setPixmap(graph4)
        layout.addWidget(g4, 1, 1)

        self.button = QPushButton('Go back')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button,0,1)
        self.setLayout(layout)

    def ddang_c(self):
        layout = QGridLayout()

        g4 = QLabel(self)
        graph4 = QPixmap('img\ddang_c.jpg')
        graph4 = graph4.scaledToWidth(600)
        g4.setPixmap(graph4)
        layout.addWidget(g4, 1, 1)

        self.button = QPushButton('Go back')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button,0,1)
        self.setLayout(layout)


    def switch(self):
        self.line.backspace()

    def quit(self):
        btn_check = QMessageBox.question(self, '경고', '그거 누르면 땡칠이 사라짐',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if btn_check == QMessageBox.Yes:
            sys.exit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())