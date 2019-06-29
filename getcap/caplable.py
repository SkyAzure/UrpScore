import os
import sys
import shutil


from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QIcon, QPixmap, QFont, QRegExpValidator
from PyQt5.QtWidgets import (QWidget, QMessageBox, QApplication, QDesktopWidget, QLabel, QLineEdit, QGridLayout,
                             QPushButton)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.imgnum = 0
        self.i = 0
        self.errnum = 0
        #获得验证码地址 imgpath
        self.imgpath = os.path.abspath(os.path.join(os.getcwd(), "../..")) + "/capimg/"
        #获得验证码img.jpg列表 img_names
        self.img_names = os.listdir(self.imgpath)
        #遍历得到剩余验证码数量，保存到imgnum
        for img_name in self.img_names:
            self.imgnum += 1
        #事例属性self.capimg 为QLabel加载图片
        self.capimg = QPixmap(self.imgpath+self.img_names[0])
        self.capimgLabel =  QLabel(self)
        self.capimgLabel.setPixmap(self.capimg)

        #文字提示
        self.imgnumLabel = QLabel("剩余："+str(self.imgnum)+"张验证码")#需要Enter更新
        font1 = QFont()
        font1.setFamily('楷体')
        font1.setBold(True)
        font1.setPointSize(18)
        font1.setWeight(80)
        self.imgnumLabel.setFont(font1)

        captextLabel = QLabel("请输入验证码，按Enter键提交")

        self.captextEdit = QLineEdit()
        #输入限制：大小写字母和数字，
        #最大长度：4
        my_regex = QRegExp("[a-zA-Z0-9]+$")
        my_validator = QRegExpValidator(my_regex, self.captextEdit)
        self.captextEdit.setValidator(my_validator)
        self.captextEdit.setMaxLength(4);
        #设计字体样式
        self.captextEdit.setFrame(False)
        self.captextEdit.setAlignment(Qt.AlignCenter)
        self.captextEdit.setStyleSheet("color:red")
        font2 = QFont()
        font2.setFamily('微软雅黑')
        font2.setBold(True)
        font2.setPointSize(18)
        font2.setWeight(50)
        self.captextEdit.setFont(font2)

        put_Btn = QPushButton('提交')
        put_Btn.clicked.connect(self.getcap)
        self.captextEdit.returnPressed.connect(self.getcap)

        self.errorLabel = QLabel("重复的验证码或错误的个数"+str(self.errnum))

        grid = QGridLayout()

        grid.addWidget(self.imgnumLabel, 0, 0, 1, 1, Qt.AlignCenter | Qt.AlignTop)
        grid.addWidget(self.capimgLabel, 1,0,1,1,Qt.AlignCenter | Qt.AlignVCenter)
        grid.addWidget(captextLabel, 2,0,1,1,Qt.AlignCenter | Qt.AlignBottom)
        grid.addWidget(self.captextEdit, 3,0,1,1,Qt.AlignCenter)
        grid.addWidget(put_Btn, 4,0,1,1,Qt.AlignCenter)
        grid.addWidget(self.errorLabel, 5, 0, 1, 1, Qt.AlignCenter | Qt.AlignBottom)



        self.setLayout(grid)

        self.resize(720, 360)
        self.center()

        self.setWindowTitle('手工打码(skyazure)')
        self.setWindowIcon(QIcon('G:\code\captcha\logo.png'))
        self.show()
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



    def getcap(self):
        self.i += 1
        if self.imgnum ==0:
            self.capimgLabel.setText("已完成,请退出")
            reply = QMessageBox.question(self, 'Message',"是否退出", QMessageBox.Yes |QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.close()
            else:
                self.close()
        captext = self.captextEdit.text() #获取文本框内容

        #界面更新
        self.captextEdit.clear()
        self.imgnum = self.imgnum-1
        self.imgnumLabel.setText("剩余："+str(self.imgnum)+"张验证码,已完成"+str(self.i)+"张")

        OldPath = self.imgpath + self.img_names[self.i-1]
        self.capimg = QPixmap(self.imgpath + self.img_names[self.i])
        self.capimgLabel.setPixmap(self.capimg)
        #self.capimgLabel.repaint()

        #操作文件
        MidPath = self.imgpath + captext+".jpg"
        NewPath = os.path.abspath(os.path.join(os.getcwd(), "../..")) + "/capfinsh/"+captext+".jpg"
        try:
            os.rename(OldPath, MidPath)
            shutil.move(MidPath,NewPath)
        except WindowsError:
            self.errnum += 1
            self.errorLabel.setText("重复的验证码或错误的个数"+str(self.errnum))

        #print(captext)


    #def closeEvent(self, event):
    #
    #     reply = QMessageBox.question(self, 'Message',
    #         "做完了么就退出?", QMessageBox.Yes |
    #         QMessageBox.No, QMessageBox.No)
    #
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    sys.exit(app.exec_())