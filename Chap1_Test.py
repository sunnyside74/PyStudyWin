from PyQt5.QtWidgets import *
import sys

# Button Click Event Function
def btnClick():
	print('Button Clicked')


app = QApplication(sys.argv)

dlg = QDialog()
dlg.setWindowTitle("타이틀")
dlg.setGeometry(100,100,500,500)

vbox = QVBoxLayout()

btn = QPushButton('요걸 클릭해라')
btn.clicked.connect( btnClick ) 		# Event 등록 -> 콘솔에 출력됨
lineEdit = QLineEdit()
vbox.addWidget(btn)
vbox.addWidget(lineEdit)

dlg.setLayout(vbox)

dlg.show()		# dialog 창을 생성함

app.exec_() 	# 큐메모리 감시 (무한loop ==> Close Event)
print("hello")
