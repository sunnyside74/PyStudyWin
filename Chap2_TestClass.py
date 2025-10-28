from PyQt5.QtWidgets import *
import sys

class ClassMyWindow:
	def __init__(self):
		self.dlg = QDialog()
		self.dlg.setWindowTitle("타이틀")
		self.dlg.setGeometry(100,100,500,500)

		self.vbox = QVBoxLayout()

		self.btn = QPushButton('요걸 클릭해라')
		self.btn.clicked.connect( btnClick ) 		# Event 등록 -> 콘솔에 출력됨
		self.lineEdit = QLineEdit()
		self.vbox.addWidget(self.btn)
		self.vbox.addWidget(self.lineEdit)

		self.dlg.setLayout(self.vbox)
		self.dlg.show()		# dialog 창을 생성함
		
		
# Button Click Event Function
def btnClick():
	print('Button Clicked')


app = QApplication(sys.argv)

myWindow = ClassMyWindow()

app.exec_() 	# 큐메모리 감시 (무한loop ==> Close Event)
print("hello")
