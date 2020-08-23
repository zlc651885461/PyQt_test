import sys
from PyQt5.QtWidgets import QApplication, QWidget
from a import Ui_Form


class Myform(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn.clicked.connect(self.count)
        self.i = 0  # 设置计数器变量。

    def count(self):
        # 设置标签的文本为变量的值
        self.label.setText('%d' % self.i)
        self.i += 1  # 变量自增


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    w.show()
    app.exec_()