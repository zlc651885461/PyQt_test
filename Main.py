import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
from src.fangan import Ui_MainWindow as fy


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui_fy = fy()
    # 事件绑定
    # src.ReadExcelButton.clicked.connect(src.openfile())
    # src.ReadExcelButton.clicked.connect(src.creat_table_show())
    # 向窗口添加控件
    # ui_dn.setupUi(mainWindow)
    ui_fy.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())