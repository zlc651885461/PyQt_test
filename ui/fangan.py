# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fangan.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from PyQt5.QtGui import QIcon,QBrush,QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pandas as pd
import json
import os

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.start_time = None
        self.end_time = None
        self.flag_start = False
        self.frame_v_header = None
        self.frame_h_header = None
        self.path_openfile = None
        self.path_to_excel = None
        self.btn_dict = {}
        self.frame_rows = 0
        self.frame_cols = 0
        self.colnum_dict = {
            "电气领班W": 0,
            "高配A": 1,
            "高配B": 2,
            "变电站C": 3,
            "变电站D": 4,
            "变电站E": 5,
            "柴发G": 6,
            "柴发H": 7,
            "暖通领班K": 8,
            "冷站I": 9,
            "冷站J": 10,
            "精密空调L": 11,
            "环境处M": 12,
        }

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1596, 885)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setIconSize(QtCore.QSize(128, 128))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # tableweidget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet("border:2px groove gray;"
                                       "selection-background-color:rgb(169,169,169);"
                                       "background-color:transparent;"
                                       "gridline-color:none")
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 6)

        # table背景图片
        self.tableBack = QtWidgets.QLabel(self.centralwidget)
        self.tableBack.setObjectName("tableBack")
        self.tableBack.setPixmap(QtGui.QPixmap('./static/数据中心全景图.jpg'))
        self.tableBack.setScaledContents(True)  # 设置图片自动适应大小
        self.gridLayout.addWidget(self.tableBack, 2, 0, 1, 6) #添加到整体布局
        self.tableBack.setAutoFillBackground(True)
        # 创建透明度
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.9)
        self.tableBack.setGraphicsEffect(op)
        self.tableBack.stackUnder(self.tableWidget)  # 将背景图片放到表格下层

        # 左上角图标
        self.ABCImg = QtWidgets.QLabel(self.centralwidget)
        self.ABCImg.setMaximumSize(QtCore.QSize(180, 61))
        self.ABCImg.setObjectName("ABCImg")
        self.ABCImg.setPixmap(QtGui.QPixmap('./static/LabelABC.png'))
        self.ABCImg.setScaledContents(True)
        self.gridLayout.addWidget(self.ABCImg, 0, 0, 1, 1)
        # 中间标题
        self.ABCDC_label = QtWidgets.QLabel(self.centralwidget)
        self.ABCDC_label.setMaximumSize(QtCore.QSize(551, 41))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(20)
        self.ABCDC_label.setFont(font)
        self.ABCDC_label.setTextFormat(QtCore.Qt.AutoText)
        self.ABCDC_label.setObjectName("ABCDC_label")
        self.gridLayout.addWidget(self.ABCDC_label, 0, 1, 1, 1)
        # 布局
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # 角色按钮
        self.W_Button = QtWidgets.QPushButton(self.centralwidget)
        self.W_Button.setMaximumSize(QtCore.QSize(126, 28))
        self.W_Button.setObjectName("W_Button")
        self.horizontalLayout_4.addWidget(self.W_Button)
        self.A_Button = QtWidgets.QPushButton(self.centralwidget)
        self.A_Button.setMaximumSize(QtCore.QSize(126, 28))
        self.A_Button.setObjectName("A_Button")
        self.horizontalLayout_4.addWidget(self.A_Button)
        self.B_Button = QtWidgets.QPushButton(self.centralwidget)
        self.B_Button.setMaximumSize(QtCore.QSize(126, 28))
        self.B_Button.setObjectName("B_Button")
        self.horizontalLayout_4.addWidget(self.B_Button)
        self.C_Button = QtWidgets.QPushButton(self.centralwidget)
        self.C_Button.setMaximumSize(QtCore.QSize(126, 28))
        self.C_Button.setObjectName("C_Button")
        self.horizontalLayout_4.addWidget(self.C_Button)
        self.D_Button = QtWidgets.QPushButton(self.centralwidget)
        self.D_Button.setMaximumSize(QtCore.QSize(126, 28))
        self.D_Button.setObjectName("D_Button")
        self.horizontalLayout_4.addWidget(self.D_Button)
        self.E_Button = QtWidgets.QPushButton(self.centralwidget)
        self.E_Button.setMaximumSize(QtCore.QSize(126, 28))
        self.E_Button.setObjectName("E_Button")
        self.horizontalLayout_4.addWidget(self.E_Button)
        self.G_Button = QtWidgets.QPushButton(self.centralwidget)
        self.G_Button.setMaximumSize(QtCore.QSize(126, 28))
        self.G_Button.setObjectName("G_Button")
        self.horizontalLayout_4.addWidget(self.G_Button)
        self.H_Button = QtWidgets.QPushButton(self.centralwidget)
        self.H_Button.setMaximumSize(QtCore.QSize(126, 28))
        self.H_Button.setObjectName("H_Button")
        self.horizontalLayout_4.addWidget(self.H_Button)
        self.K_Button = QtWidgets.QPushButton(self.centralwidget)
        self.K_Button.setMaximumSize(QtCore.QSize(126, 28))
        self.K_Button.setObjectName("K_Button")
        self.horizontalLayout_4.addWidget(self.K_Button)
        self.I_Button = QtWidgets.QPushButton(self.centralwidget)
        self.I_Button.setMaximumSize(QtCore.QSize(126, 28))
        self.I_Button.setObjectName("I_Button")
        self.horizontalLayout_4.addWidget(self.I_Button)
        self.J_Button = QtWidgets.QPushButton(self.centralwidget)
        self.J_Button.setMaximumSize(QtCore.QSize(126, 28))
        self.J_Button.setObjectName("J_Button")
        self.horizontalLayout_4.addWidget(self.J_Button)
        self.L_Button = QtWidgets.QPushButton(self.centralwidget)
        self.L_Button.setMaximumSize(QtCore.QSize(126, 28))
        self.L_Button.setObjectName("L_Button")
        self.horizontalLayout_4.addWidget(self.L_Button)
        self.M_Button = QtWidgets.QPushButton(self.centralwidget)
        self.M_Button.setMaximumSize(QtCore.QSize(126, 28))
        self.M_Button.setObjectName("M_Button")
        self.horizontalLayout_4.addWidget(self.M_Button)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 6)

        # 功能按钮:开始演练，导入模板，导出模板
        self.btn_begin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_begin.setMaximumSize(QtCore.QSize(128, 28))
        self.btn_begin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_begin.setObjectName("btn_begin")
        self.gridLayout.addWidget(self.btn_begin, 0, 4, 1, 1)
        self.btn_read_excel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_read_excel.setMaximumSize(QtCore.QSize(128, 28))
        self.btn_read_excel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_read_excel.setObjectName("btn_read_excel")
        self.gridLayout.addWidget(self.btn_read_excel, 0, 3, 1, 1)
        self.btn_to_excel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_to_excel.setMaximumSize(QtCore.QSize(128, 28))
        self.btn_to_excel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_to_excel.setObjectName("btn_to_excel")
        self.gridLayout.addWidget(self.btn_to_excel, 0, 5, 1, 1)

        # lcdNumber计时器
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setStyleSheet("border: 3px solid gray; color: white; background: black;")
        self.lcdNumber.setMaximumSize(QtCore.QSize(180, 90))
        self.gridLayout.addWidget(self.lcdNumber, 0, 2, 1, 1)
        # 设计一个定时器
        self.timer = QtCore.QTimer()
        self.timer.start(10)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 连接到槽函数
        self.disable_btn()
        self.timer.timeout.connect(self.clock)
        self.btn_read_excel.clicked.connect(self.openfile)
        self.btn_begin.clicked.connect(self.task_begin)
        self.btn_to_excel.clicked.connect(self.save_event)
        self.W_Button.clicked.connect(lambda: self.btn_task(self.W_Button.text()))
        self.A_Button.clicked.connect(lambda: self.btn_task(self.A_Button.text()))
        self.B_Button.clicked.connect(lambda: self.btn_task(self.B_Button.text()))
        self.C_Button.clicked.connect(lambda: self.btn_task(self.C_Button.text()))
        self.D_Button.clicked.connect(lambda: self.btn_task(self.D_Button.text()))
        self.E_Button.clicked.connect(lambda: self.btn_task(self.E_Button.text()))
        self.G_Button.clicked.connect(lambda: self.btn_task(self.G_Button.text()))
        self.H_Button.clicked.connect(lambda: self.btn_task(self.H_Button.text()))
        self.K_Button.clicked.connect(lambda: self.btn_task(self.K_Button.text()))
        self.I_Button.clicked.connect(lambda: self.btn_task(self.I_Button.text()))
        self.J_Button.clicked.connect(lambda: self.btn_task(self.J_Button.text()))
        self.L_Button.clicked.connect(lambda: self.btn_task(self.L_Button.text()))
        self.M_Button.clicked.connect(lambda: self.btn_task(self.M_Button.text()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_to_excel.setText(_translate("MainWindow", "导出模板"))
        self.ABCDC_label.setText(_translate("MainWindow", "中国农业银行北方数据中心应急演练"))
        self.W_Button.setText(_translate("MainWindow", "电气领班W"))
        self.A_Button.setText(_translate("MainWindow", "高配A"))
        self.B_Button.setText(_translate("MainWindow", "高配B"))
        self.C_Button.setText(_translate("MainWindow", "变电站C"))
        self.D_Button.setText(_translate("MainWindow", "变电站D"))
        self.E_Button.setText(_translate("MainWindow", "变电站E"))
        self.G_Button.setText(_translate("MainWindow", "柴发G"))
        self.H_Button.setText(_translate("MainWindow", "柴发H"))
        self.K_Button.setText(_translate("MainWindow", "暖通领班K"))
        self.I_Button.setText(_translate("MainWindow", "冷站I"))
        self.J_Button.setText(_translate("MainWindow", "冷站J"))
        self.L_Button.setText(_translate("MainWindow", "精密空调L"))
        self.M_Button.setText(_translate("MainWindow", "环境处M"))
        self.btn_begin.setText(_translate("MainWindow", "开始演练"))
        self.btn_read_excel.setText(_translate("MainWindow", "导入模板"))

    """
    上方计时器
    """
    def clock(self):
        # LCD计时显示
        if not self.flag_start:
            # 显示当地时间
            # t = time.strftime('%H:%M:%S',time.localtime(time.time()))
            t = '0:00:00'
        else:
            dalte_t = datetime.datetime.now().replace(microsecond=0) - self.start_time
            t = str(dalte_t).split(',')[-1]
        self.lcdNumber.display(t)

    """
    开始演练按钮
    """
    def task_begin(self):

        if self.btn_begin.text() == '开始演练':
            self.flag_start = True
            self.btn_begin.setText('停止演练')
            self.start_time = datetime.datetime.now().replace(microsecond=0)
            self.btn_read_excel.setEnabled(False)
            self.btn_to_excel.setEnabled(False)
            self.enable_btn()
            self.item_alter(0,12)
        else:
            self.flag_start = False
            self.btn_begin.setText('开始演练')
            self.end_time = datetime.datetime.now()
            self.disable_btn()
            self.btn_to_excel.setEnabled(True)
            self.btn_read_excel.setEnabled(True)
            for j in range(self.frame_cols-1):
                self.item_alter(self.frame_rows-1,j)
    """
    按钮可用
    """
    def enable_btn(self):
        self.A_Button.setEnabled(True)
        self.B_Button.setEnabled(True)
        self.C_Button.setEnabled(True)
        self.D_Button.setEnabled(True)
        self.E_Button.setEnabled(True)
        self.G_Button.setEnabled(True)
        self.H_Button.setEnabled(True)
        self.I_Button.setEnabled(True)
        self.J_Button.setEnabled(True)
        self.L_Button.setEnabled(True)
        self.K_Button.setEnabled(True)
        self.M_Button.setEnabled(True)
        self.W_Button.setEnabled(True)
    """
    按钮失效
    """
    def disable_btn(self):
        self.A_Button.setEnabled(False)
        self.B_Button.setEnabled(False)
        self.C_Button.setEnabled(False)
        self.D_Button.setEnabled(False)
        self.E_Button.setEnabled(False)
        self.G_Button.setEnabled(False)
        self.H_Button.setEnabled(False)
        self.I_Button.setEnabled(False)
        self.J_Button.setEnabled(False)
        self.L_Button.setEnabled(False)
        self.K_Button.setEnabled(False)
        self.M_Button.setEnabled(False)
        self.W_Button.setEnabled(False)
        self.btn_begin.setEnabled(False)
        self.btn_to_excel.setEnabled(False)
    """
    打开方案
    """
    def openfile(self):
        # 获取路径
        openfile_name, openfile_type = QFileDialog.getOpenFileName(self, '选择文件', './', 'Excel files(*.xlsx , *.xls);; All files(*);')
        # print(openfile_name,openfile_type)
        self.path_openfile = openfile_name
        file_name = self.path_openfile.split('/')[-1].split('.')[0]
        if len(self.path_openfile) > 0:
            self.btn_begin.setEnabled(True)
            self.load_dict()
            font = QtGui.QFont()
            font.setFamily("Yuanti SC")
            font.setPointSize(60)
            self.tableBack.setFont(font)
            self.tableBack.setText(file_name)
            self.tableBack.setStyleSheet("text-align:center;color:rgb(0,255,127);")#浅绿色
            self.tableBack.setTextFormat(QtCore.Qt.AutoText)
            self.tableBack.setAlignment(Qt.AlignCenter)

    """
    加载物业计时点表
    """
    def load_dict(self):
        try:
            with open('./config.json',encoding='utf-8') as f:
                res = f.read()
                plan_dict = json.loads(res)
                # print(plan_dict)
        except Exception as e:
            self.dialog = QtWidgets.QMessageBox.about(self, '通知', e)

        # 根据方案文件名判断应用场景
        file_name = self.path_openfile.split('/')[-1].split('.')[0]
        # print(file_name)
        if '3#' in file_name and '中断' in file_name:
            self.btn_dict = plan_dict.get('num3_break')
            self.creat_table_show()
            return
        elif '3#' in file_name and '恢复' in file_name:
            self.btn_dict = plan_dict.get('num3_resume')
            self.creat_table_show()
            return
        elif '2#' in file_name and '中断' in file_name:
            self.btn_dict = plan_dict.get('num2_break')
            self.creat_table_show()
            return
        elif '2#' in file_name and '恢复' in file_name:
            self.btn_dict = plan_dict.get('num2_resume')
            self.creat_table_show()
            return
        if '1#' in file_name and '中断' in file_name:
            # print(file_name)
            self.btn_dict = plan_dict.get('num1_break')
            self.creat_table_show()
            return
        elif '1#' in file_name and '恢复' in file_name:
            self.btn_dict = plan_dict.get('num1_resume')
            self.creat_table_show()
            return
        else:
            print('else')
            self.dialog = QtWidgets.QMessageBox.about(self, '通知', '方案不符合要求！')
            return

    """
    table显示功能
    """
    def creat_table_show(self):
        # 读取表格，转换表格，
        if len(self.path_openfile) > 0:
            frame_all = pd.read_excel(self.path_openfile, index_col=0)
            # print(frame_all)
            self.frame_rows = frame_all.shape[0]
            self.frame_cols = frame_all.shape[1]

            # 读取表格行/列表头
            self.frame_h_header = frame_all.columns.values.tolist()
            self.frame_v_header = frame_all.index.values.tolist()
            # 给tablewidget设置行列表头
            self.tableWidget.setColumnCount(self.frame_cols)
            self.tableWidget.setRowCount(self.frame_rows)
            self.tableWidget.setHorizontalHeaderLabels(self.frame_h_header)
            self.tableWidget.horizontalHeader().setStyleSheet("border:2px solid #888; background-color:#AAA; font:14px;")
            self.tableWidget.verticalHeader().setFixedWidth(60)
            self.tableWidget.setVerticalHeaderLabels(self.frame_v_header)
            self.tableWidget.verticalHeader().setStyleSheet("border:2px solid #888; background-color:#AAA;font:14px;")

            # 遍历表格每个元素，同时添加到tablewidget中
            for j in range(self.frame_cols):
                input_table_cols_list = frame_all[frame_all.columns[j]].values.tolist()
                # button_start.setStyleSheet('''text-align:center;background-color:DarkSeaGreen;height:30px;border-style:outset;font:14px''')

                for i in range(0, self.frame_rows):
                    input_table_item = input_table_cols_list[i]
                    # 将遍历的元素添加到tablewidget中并显示
                    input_table_item = str(input_table_item)
                    # print(input_table_item)
                    newItem = QTableWidgetItem(input_table_item)
                    newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                    # newItem.setFont(QtGui.QFont("Yuanti SC",14)) #设置单元格内字体，字号
                    self.tableWidget.setItem(i, j, newItem)
                    self.tableWidget.setRowHeight(i, 200)

        else:
            self.centralWidget.show()

    """
    按键功能
    """
    def btn_task(self, btn_text):
        click_list = self.btn_dict.get(btn_text)
        if len(click_list) != 0:
            i = click_list.pop()
            j = self.colnum_dict.get(btn_text)
            # print(i)
            self.item_alter(i,j)

    """修改单元格内容--添加完成时间，用时"""
    def item_alter(self,i,j):
        time_point = datetime.datetime.now().replace(microsecond=0)
        time_point_str = datetime.datetime.strftime(time_point, '\n完成时间: %H:%M:%S;')
        time_li = str(time_point - self.start_time).split(',')[-1].split(':')
        time_complete = ''.join(['用时:', time_li[-2], '分,', time_li[-1], '秒。'])
        read_item_text = self.tableWidget.item(i, j).text()
        new_item_text = ''.join([read_item_text, time_point_str, time_complete])
        # print(new_item_text)
        self.tableWidget.item(i, j).setText(new_item_text)
        self.tableWidget.item(i,j).setForeground(QBrush(QColor(255,0,0)))
        self.tableWidget.showColumn(j)

    """
    导出功能
    """
    def save_event(self):
        directory1 = QFileDialog.getSaveFileName(None, "文件保存", "C:/", "Excel files(*.xlsx , *.xls);;All files(*);")
        self.path_to_excel = os.path.join(directory1[0])
        if len(self.path_to_excel) != 0:
            self.task_to_excel()

    def task_to_excel(self):
        frame_out = pd.DataFrame(index=self.frame_v_header, columns=self.frame_h_header)
        frame_rows = frame_out.shape[0]
        frame_cols = frame_out.shape[1]
        for j in range(frame_cols):
            col_list = []
            for i in range(frame_rows):
                read_item_text = self.tableWidget.item(i, j).text()
                col_list.append(read_item_text)
            frame_out[self.frame_h_header[j]] = col_list
        # print(frame_out)
        try:
            frame_out.to_excel(self.path_to_excel)
        except Exception as e:
            self.dialog = QtWidgets.QMessageBox.about(self, '警告', e)
            self.dialog.exec_()
        else:
            self.dialog = QtWidgets.QMessageBox.about(self, '通知', ''.join(['成功导出至"', self.path_to_excel, '".']))
