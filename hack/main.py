import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# QIcon 아이콘을 사용하기 위한 모듈
# QPushButton 버튼을 사용하기 위한 모듈
# QMainWindow 아래 활성화를 표기하기 위한 모듈

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('img/ddang.jpg'))

        self.setWindowTitle("해킹툴")
        self.setGeometry(500, 200, 520, 130)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

        btn_a = QPushButton("에임핵", self)
        btn_a.move(10, 50)
        btn_a.resize(btn_a.sizeHint())
        btn_a.clicked.connect(self.btn_click_boho)

        btn_b = QPushButton("인터넷 기록 뽑기", self)
        btn_b.move(200, 50)
        btn_b.resize(btn_b.sizeHint())
        btn_b.clicked.connect(self.test)

        btn_c = QPushButton("바이러스 파일 넣기", self)
        btn_c.move(400, 50)
        btn_c.resize(btn_c.sizeHint())
        btn_c.clicked.connect(self.test2)

        btn_q = QPushButton("종료", self)
        btn_q.move(200, 100)
        btn_q.resize(btn_c.sizeHint())
        btn_q.clicked.connect(self.quit)

    def test(self):
        print("1")
    def test2(self):
        print("2")

    def btn_click_boho(self):
        btn_check = QMessageBox.question(self, '에임핵', '진짜?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if btn_check == QMessageBox.Yes:

            self.statusBar.showMessage("활성 상태")
        elif btn_check == QMessageBox.No:
            self.statusBar.showMessage("비활성 상태")


    def quit(self):
        btn_check = QMessageBox.question(self, '경고', '그거 눌러도 되는거 맞아?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if btn_check == QMessageBox.Yes:
            sys.exit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())