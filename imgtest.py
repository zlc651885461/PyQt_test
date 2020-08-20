import sys
from PyQt5.QtGui import  QIcon
from PyQt5.QtWidgets import QWidget,QApplication
class IconClass(QWidget):
    def __init__(self,parent=None):
        super(IconClass,self).__init__(parent)
        self.initUI()
    def initUI(self):
        self.setGeometry(400,200,500,600)#坐标，宽高
        self.setWindowTitle("显示图标的窗口")
        self.setWindowIcon(QIcon('ABC.ico'))#设置窗体图标

if __name__=="__main__":
    app=QApplication(sys.argv)
    icon=IconClass()
    icon.show()
    sys.exit(app.exec_())