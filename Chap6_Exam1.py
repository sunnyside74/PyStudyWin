# Exam 1
# Spin입력 1과

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

# xml --> 객체로 변환
class ClassMyWindow:
    def __init__(self):
        self.dlg = loadUi('Exam1.ui')
        self.dlg.pushButton.clicked.connect( self.btnClick ) 		# Event 등록 -> 콘솔에 출력됨
        self.dlg.show()		# dialog 창을 생성함
        
    # Button Click Event Function
    def btnClick(self):
        # self.dlg.lineEdit.setText("헬로 파이썬")
        self.dlg.lineEdit.clear()

        self.a = self.dlg.spinBox_1.value()
        self.b = self.dlg.spinBox_2.value()

        self.dlg.lineEdit.setText(self.a + self.b)
        

app = QApplication(sys.argv)
myWindow = ClassMyWindow()
app.exec_() 	# 큐메모리 감시 (무한loop ==> Close Event)
print("hello")

