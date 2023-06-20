# File: Main.py
# Description: CellProfiler user-friendly software for .csv data analysis, manipulation, and visualization.
# Authors: Anush Varma, Juned Miah
# Created: June 20, 2023 (Today's Date)
# Last Modified: June 20, 2023 (Anush Varma - Initial commit)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Cell Profiler")
        MainWindow.resize(760, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.modules_label = QtWidgets.QLabel(self.centralwidget)
        self.modules_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modules_label.sizePolicy().hasHeightForWidth())
        self.modules_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        self.modules_label.setFont(font)
        self.modules_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.modules_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.modules_label.setLineWidth(2)
        self.modules_label.setMidLineWidth(0)
        self.modules_label.setScaledContents(True)
        self.modules_label.setAlignment(QtCore.Qt.AlignCenter)
        self.modules_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.modules_label.setObjectName("modules_label")
        self.verticalLayout_2.addWidget(self.modules_label, 0, QtCore.Qt.AlignTop)
        self.types_button = QtWidgets.QPushButton(self.centralwidget)
        self.types_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.types_button.sizePolicy().hasHeightForWidth())
        self.types_button.setSizePolicy(sizePolicy)
        self.types_button.setSizeIncrement(QtCore.QSize(3, 3))
        self.types_button.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.types_button.setFont(font)
        self.types_button.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.types_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.types_button.setAutoFillBackground(False)
        self.types_button.setObjectName("types_button")
        self.verticalLayout_2.addWidget(self.types_button)
        self.graph_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_button.sizePolicy().hasHeightForWidth())
        self.graph_button.setSizePolicy(sizePolicy)
        self.graph_button.setSizeIncrement(QtCore.QSize(3, 3))
        self.graph_button.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.graph_button.setFont(font)
        self.graph_button.setObjectName("graph_button")
        self.verticalLayout_2.addWidget(self.graph_button)
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        self.settings_button.setSizeIncrement(QtCore.QSize(3, 3))
        self.settings_button.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout_2.addWidget(self.settings_button)
        spacerItem = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.file_loaded_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.file_loaded_label.setFont(font)
        self.file_loaded_label.setAlignment(QtCore.Qt.AlignCenter)
        self.file_loaded_label.setObjectName("file_loaded_label")
        self.verticalLayout_3.addWidget(self.file_loaded_label, 0, QtCore.Qt.AlignTop)
        self.Check_all_box = QtWidgets.QCheckBox(self.centralwidget)
        self.Check_all_box.setSizeIncrement(QtCore.QSize(0, 0))
        self.Check_all_box.setObjectName("Check_all_box")
        self.verticalLayout_3.addWidget(self.Check_all_box)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -83, 600, 173))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 5, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 6, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 3, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 4, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_CSV = QtWidgets.QAction(MainWindow)
        self.actionLoad_CSV.setObjectName("actionLoad_CSV")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionLoad_CSV)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.settings_button, self.graph_button)
        MainWindow.setTabOrder(self.graph_button, self.types_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cell Profiler"))
        self.modules_label.setText(_translate("MainWindow", "Modules"))
        self.types_button.setText(_translate("MainWindow", "Names / Types"))
        self.graph_button.setText(_translate("MainWindow", "Graph"))
        self.settings_button.setText(_translate("MainWindow", "Settings"))
        self.file_loaded_label.setText(_translate("MainWindow", "No File Loaded"))
        self.Check_all_box.setText(_translate("MainWindow", "Check All"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_7.setText(_translate("MainWindow", "CheckBox"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionLoad_CSV.setText(_translate("MainWindow", "Load CSV"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
