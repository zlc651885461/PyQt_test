import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
# from ui.DemoNew import Ui_MainWindow as dn
from ui.fangan import Ui_MainWindow as fy


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    # ui_dn = dn()
    ui_fy = fy()
    # 事件绑定
    # ui.ReadExcelButton.clicked.connect(ui.openfile())
    # ui.ReadExcelButton.clicked.connect(ui.creat_table_show())
    # 向窗口添加控件
    # ui_dn.setupUi(mainWindow)
    ui_fy.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())