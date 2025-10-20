from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys

# xml --> 객체로 변환
class ClassMyWindow:
	def __init__(self):
		self.dlg = loadUi('myqt.ui')
		self.dlg.pushButton.clicked.connect( self.btnClick ) 		# Event 등록 -> 콘솔에 출력됨
		self.dlg.show()		# dialog 창을 생성함
		
	# Button Click Event Function
	def btnClick(self):
		print('Button Clicked')


app = QApplication(sys.argv)

myWindow = ClassMyWindow()

app.exec_() 	# 큐메모리 감시 (무한loop ==> Close Event)
print("hello")
