from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QMessageBox
from FCFS import *
from SRTF import *
from SJF import *
from RR import *

class Ui_MainWindow(object):

    def __init__(self):
        self.X = 0
        self.availableProcesses = []
        self.processes = {}

    def sortDict(self):
        temp = sorted(self.processes.items(), key=lambda x: x[1]['arrival'])
        for i in temp:
            self.processes[i[0]] = i[1]


    def add(self):
        name = self.processNameText.text()
        arrival, burst = self.arrivalTimeText.text(), self.BurstTimeText.text()
        if name == "" or arrival == "" or burst == "":
            self.show_popup("Enter full data for the process first")
            return
        if name in self.processes:
            self.show_popup("Process already exist")
            return
        else:
            self.processesTable.setItem(self.X, 0, QTableWidgetItem(name))
            self.processesTable.setItem(self.X, 1, QTableWidgetItem(arrival))
            self.processesTable.setItem(self.X, 2, QTableWidgetItem(burst))
            self.availableProcesses.append(name)
            self.processes[name] = {'arrival' : int(arrival), 'brust': int(burst)}
            self.X += 1

    def remove(self):
        if len(self.processes) == 0:
            self.show_popup("No processes to delete")
            return
        row = self.processesTable.currentRow()
        del self.processes[self.processesTable.item(row, 0).text()]
        print(self.processes)
        self.processesTable.removeRow(row)
        self.X = max(self.X - 1, 0)
        self.processesTable.setRowCount(20)


    def calculate(self):

        if  not(self.SJF_btn.isChecked() or  self.FCFS_btn.isChecked() or self.RR_btn.isChecked() or self.SRTF_btn.isChecked()):
            self.show_popup("Enter algorithm to execute")
            return
        if len(self.processes) == 0:
            self.show_popup("There must be at least one process to execute this algorithm")
            return
        self.sortDict()
        if self.SJF_btn.isChecked():
             res = SJF(self.processes)
        elif self.FCFS_btn.isChecked():
             res = FCFS(self.processes)
        elif self.RR_btn.isChecked():
            if self.quantum_time.text() == "":
                self.show_popup("Enter value for Quantum time first")
                return
            else:
                res = RR(self.processes, int(self.quantum_time.text()))
        else:
            res = SRTF(self.processes)
        self.lcdNumber.display(res[0])
        self.lcdNumber_2.display(res[1])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(670, 430, 101, 51))
        self.lcdNumber.setObjectName("lcdNumber")

        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(670, 360, 101, 51))
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 430, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 370, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 40, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 160, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 100, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(490, 260, 111, 51))
        self.addBtn.setObjectName("addBtn")

        self.removeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.removeBtn.setGeometry(QtCore.QRect(640, 260, 111, 51))
        self.removeBtn.setObjectName("removeBtn")

        self.processNameText = QtWidgets.QLineEdit(self.centralwidget)
        self.processNameText.setGeometry(QtCore.QRect(650, 50, 131, 31))
        self.processNameText.setObjectName("processNameText")

        self.arrivalTimeText = QtWidgets.QLineEdit(self.centralwidget)
        self.arrivalTimeText.setGeometry(QtCore.QRect(650, 110, 131, 31))
        self.arrivalTimeText.setObjectName("arrivalTimeText")

        self.BurstTimeText = QtWidgets.QLineEdit(self.centralwidget)
        self.BurstTimeText.setGeometry(QtCore.QRect(650, 170, 131, 31))
        self.BurstTimeText.setObjectName("BurstTimeText")

        self.quantum_time = QtWidgets.QLineEdit(self.centralwidget)
        self.quantum_time.setGeometry(QtCore.QRect(260, 450, 131, 31))
        self.quantum_time.setObjectName("quantum_time")

        self.calculateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calculateBtn.setGeometry(QtCore.QRect(340, 510, 111, 51))
        self.calculateBtn.setObjectName("calculateBtn")

        self.FCFS_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.FCFS_btn.setGeometry(QtCore.QRect(30, 380, 161, 20))
        self.FCFS_btn.setObjectName("FCFS_btn")

        self.SJF_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.SJF_btn.setGeometry(QtCore.QRect(220, 380, 161, 20))
        self.SJF_btn.setObjectName("SJF_btn")

        self.SRTF_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.SRTF_btn.setGeometry(QtCore.QRect(30, 410, 211, 20))
        self.SRTF_btn.setObjectName("SRTF_btn")

        self.RR_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.RR_btn.setGeometry(QtCore.QRect(30, 450, 211, 20))
        self.RR_btn.setObjectName("RR_btn")

        self.QT_text = QtWidgets.QLabel(self.centralwidget)
        self.QT_text.setGeometry(QtCore.QRect(160, 440, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.QT_text.setFont(font)
        self.QT_text.setObjectName("QT_text")

        self.processesTable = QtWidgets.QTableWidget(self.centralwidget)
        self.processesTable.setGeometry(QtCore.QRect(20, 10, 441, 351))
        self.processesTable.setRowCount(20)
        self.processesTable.setColumnCount(3)
        self.processesTable.setObjectName("processesTable")

        item = QtWidgets.QTableWidgetItem()
        self.processesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.processesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.processesTable.setHorizontalHeaderItem(2, item)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.addBtn.clicked.connect(self.add)
        self.calculateBtn.clicked.connect(self.calculate)
        self.removeBtn.clicked.connect(self.remove)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_popup(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText(text)
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setStandardButtons(QtWidgets.QMessageBox.Close)
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label.setText(_translate("MainWindow", "Average Turnaround "))
        self.label_2.setText(_translate("MainWindow", "Average Waiting"))
        self.label_3.setText(_translate("MainWindow", "Process Name"))
        self.label_4.setText(_translate("MainWindow", "Process Burst Time"))
        self.label_5.setText(_translate("MainWindow", "Process Arrival Time"))

        self.addBtn.setText(_translate("MainWindow", "Add process"))
        self.removeBtn.setText(_translate("MainWindow", "Remove Process"))
        self.calculateBtn.setText(_translate("MainWindow", "Calculate"))
        self.FCFS_btn.setText(_translate("MainWindow", "First Come First Served"))
        self.SJF_btn.setText(_translate("MainWindow", "Shortest Job First"))
        self.SRTF_btn.setText(_translate("MainWindow", "Shortest Remaining Time First"))
        self.RR_btn.setText(_translate("MainWindow", "Round Robin"))

        self.QT_text.setText(_translate("MainWindow", "Quantum Time"))
        item = self.processesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.processesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Arrival Time"))
        item = self.processesTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Burst Time"))
