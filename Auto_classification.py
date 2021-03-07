import os
import sys
import time
import shutil
import threading
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QCheckBox, QMenu, QVBoxLayout, QHBoxLayout, \
    QGroupBox, QLineEdit, QPushButton, QTextEdit, QComboBox, QSlider, QInputDialog
from PyQt5.QtGui import QPixmap, QImage, QColor
from PyQt5.QtCore import QDir, Qt, QRect, QSize, QCoreApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread, QRect
from AC_aux import *


class Ui_AcDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.acc = None

    def initUI(self):
        self.setWindowTitle('Auto classification')
        hbox = QHBoxLayout()
        vb = QVBoxLayout()
        vb.addLayout(self.createInfoGroup())
        vb.addLayout(hbox)
        self.setLayout(vb)
        self.show()

    def createInfoGroup(self):
        box = QHBoxLayout()
        self.btn = QPushButton('설명보기')
        self.btn.clicked.connect(self.get_Help_Info)
        box.addWidget(self.btn)
        self.btn2 = QPushButton('바로이용')
        self.btn2.clicked.connect(self.run_AC)
        box.addWidget(self.btn2)

        self.infomsg = QTextEdit()
        self.infomsg.setFixedWidth(500)
        self.infomsg.setFixedHeight(300)
        self.infomsg.setStyleSheet("background-color: black; border: 1px solid gray;")
        self.infomsg.setTextColor(QColor(255, 255, 0))
        self.infomsg.append(' Deerworld의 자동사진분류 프로그램입니다.')
        self.infomsg.append(' > 사진, 동영상 파일들의 속성을 읽어 파일들을')
        self.infomsg.append('    날짜별로 리네이밍 해주는 프로그램입니다.')
        self.infomsg.append('    (날짜가 중복되면 _1, _2로 리네이밍합니다.)')
        self.infomsg.append("\n 이용을 원하는 메뉴를 선택해주세요.")

        cbox = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox.addLayout(box)
        vbox.addLayout(cbox)
        vbox.addWidget(self.infomsg)
        return vbox

    ### Functions # ====================================================================================================== #
    def get_Help_Info(self):
        self.infomsg.clear()
        self.infomsg.append(" 1. Auto_classification폴더 안에 있는 APV폴더로 이동합니다.")
        self.infomsg.append("\n 2. APV폴더 안에 변환을 원하는 jpg, gif, mp4등의 파일을 넣습니다.")
        self.infomsg.append("\n 3. 2번이 끝났으면 '바로이용'버튼을 눌러주세요!")
        self.infomsg.append("\n *참고 : 변환이 끝난 파일은 바탕화면에 photo, video폴더 안으로 이동됩니다.")

    def run_AC(self):
        bool = self.make_Directory()
        if (bool == False):
            self.infomsg.clear()
            self.infomsg.append(" 변환 중...\n")
            RVS = RENAME_VIDEO_SEQUENTIALLY()
            RVS.renaming_Function_Video()
            RPS = RENAME_PHOTO_SEQUENTIALLY()
            RPS.renaming_Function_Photo()
            self.infomsg.append(" 변환이 완료되었습니다!")
            self.infomsg.append("\n 사진 : {}개".format(RPS.Count))
            self.infomsg.append("\n 동영상 : {}개".format(RVS.Count))
        else:
            self.infomsg.clear()
            self.infomsg.append(" APV폴더에 변환할 파일이 없거나 지원하지 않는 파일 형식입니다.")

    def make_Directory(self):
        bool = False
        cnt = 0
        home = os.path.expanduser('~')
        currnent_Working_Directory = os.getcwd()
        desktop = home + "\Desktop"
        files = os.listdir("{}/APV".format(currnent_Working_Directory))
        if (len(files) == 0):
            bool = True
            return bool
        else:
            directories = os.listdir(desktop)
            if ("photo" not in directories):
                os.mkdir("{}/photo".format(desktop))
            if ("video" not in directories):
                os.mkdir("{}/video".format(desktop))

            for file in files:
                splited_File_Type = file.split('.')[1]
                if (splited_File_Type == "jpg" or splited_File_Type == "jpeg" or splited_File_Type == "png" or splited_File_Type == "gif"):
                    cnt += 1
                    shutil.move("{}/APV/{}".format(currnent_Working_Directory, file), "{}/photo/{}".format(desktop, file))
                elif (splited_File_Type == "avi" or splited_File_Type == "mp4" or splited_File_Type == "mpeg"):
                    cnt += 1
                    shutil.move("{}/APV/{}".format(currnent_Working_Directory, file), "{}/video/{}".format(desktop, file))
            if (cnt == 0):
                bool = True
            return bool


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_AcDialog()
    sys.exit(app.exec_())
