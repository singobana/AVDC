# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\win\PycharmProjects\AVDC\AVDC.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AVDV(object):
    def setupUi(self, AVDV):
        AVDV.setObjectName("AVDV")
        AVDV.resize(1250, 870)
        self.centralwidget = QtWidgets.QWidget(AVDV)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_setting = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_setting.sizePolicy().hasHeightForWidth())
        self.widget_setting.setSizePolicy(sizePolicy)
        self.widget_setting.setMinimumSize(QtCore.QSize(221, 721))
        self.widget_setting.setObjectName("widget_setting")
        self.label_ico = QtWidgets.QLabel(self.widget_setting)
        self.label_ico.setGeometry(QtCore.QRect(10, 380, 201, 321))
        self.label_ico.setObjectName("label_ico")
        self.layoutWidget = QtWidgets.QWidget(self.widget_setting)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 360))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_close = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.pushButton_min = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_min.setObjectName("pushButton_min")
        self.horizontalLayout.addWidget(self.pushButton_min)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_main = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_main.setObjectName("pushButton_main")
        self.verticalLayout.addWidget(self.pushButton_main)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_log = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_log.setObjectName("pushButton_log")
        self.verticalLayout.addWidget(self.pushButton_log)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_tool = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_tool.setObjectName("pushButton_tool")
        self.verticalLayout.addWidget(self.pushButton_tool)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButton_setting = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_setting.setObjectName("pushButton_setting")
        self.verticalLayout.addWidget(self.pushButton_setting)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.pushButton_about = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_about.setObjectName("pushButton_about")
        self.verticalLayout.addWidget(self.pushButton_about)
        self.horizontalLayout_3.addWidget(self.widget_setting)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(1013, 860))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_avdc = QtWidgets.QWidget()
        self.page_avdc.setObjectName("page_avdc")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_avdc)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeWidget_number = QtWidgets.QTreeWidget(self.page_avdc)
        self.treeWidget_number.setObjectName("treeWidget_number")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_number)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_number)
        self.horizontalLayout_2.addWidget(self.treeWidget_number)
        self.main_right = QtWidgets.QWidget(self.page_avdc)
        self.main_right.setMinimumSize(QtCore.QSize(600, 0))
        self.main_right.setObjectName("main_right")
        self.pushButton_start_cap = QtWidgets.QPushButton(self.main_right)
        self.pushButton_start_cap.setGeometry(QtCore.QRect(380, 0, 191, 50))
        self.pushButton_start_cap.setObjectName("pushButton_start_cap")
        self.textBrowser_warning = QtWidgets.QTextBrowser(self.main_right)
        self.textBrowser_warning.setGeometry(QtCore.QRect(0, 0, 370, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.textBrowser_warning.setFont(font)
        self.textBrowser_warning.setObjectName("textBrowser_warning")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.main_right)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 800, 571, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.progressBar_avdc = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.progressBar_avdc.setProperty("value", 24)
        self.progressBar_avdc.setObjectName("progressBar_avdc")
        self.horizontalLayout_21.addWidget(self.progressBar_avdc)
        self.label_percent = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_percent.setObjectName("label_percent")
        self.horizontalLayout_21.addWidget(self.label_percent)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.main_right)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 560, 161, 221))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_poster = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_poster.setFrameShape(QtWidgets.QFrame.Box)
        self.label_poster.setAlignment(QtCore.Qt.AlignCenter)
        self.label_poster.setObjectName("label_poster")
        self.gridLayout_2.addWidget(self.label_poster, 0, 0, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.main_right)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(240, 560, 331, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.label_fanart = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_fanart.setEnabled(True)
        self.label_fanart.setFrameShape(QtWidgets.QFrame.Box)
        self.label_fanart.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fanart.setObjectName("label_fanart")
        self.gridLayout.addWidget(self.label_fanart, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.main_right)
        self.line.setGeometry(QtCore.QRect(0, 50, 571, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_11 = QtWidgets.QLabel(self.main_right)
        self.label_11.setGeometry(QtCore.QRect(0, 70, 81, 39))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_number = QtWidgets.QLabel(self.main_right)
        self.label_number.setGeometry(QtCore.QRect(80, 70, 201, 39))
        self.label_number.setFrameShape(QtWidgets.QFrame.Box)
        self.label_number.setLineWidth(1)
        self.label_number.setText("")
        self.label_number.setObjectName("label_number")
        self.label_13 = QtWidgets.QLabel(self.main_right)
        self.label_13.setGeometry(QtCore.QRect(290, 70, 81, 39))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_release = QtWidgets.QLabel(self.main_right)
        self.label_release.setGeometry(QtCore.QRect(370, 70, 201, 39))
        self.label_release.setFrameShape(QtWidgets.QFrame.Box)
        self.label_release.setText("")
        self.label_release.setObjectName("label_release")
        self.label_15 = QtWidgets.QLabel(self.main_right)
        self.label_15.setGeometry(QtCore.QRect(0, 270, 81, 39))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_actor = QtWidgets.QLabel(self.main_right)
        self.label_actor.setGeometry(QtCore.QRect(80, 270, 491, 39))
        self.label_actor.setFrameShape(QtWidgets.QFrame.Box)
        self.label_actor.setLineWidth(1)
        self.label_actor.setText("")
        self.label_actor.setObjectName("label_actor")
        self.label_outline = QtWidgets.QLabel(self.main_right)
        self.label_outline.setGeometry(QtCore.QRect(80, 320, 491, 39))
        self.label_outline.setFrameShape(QtWidgets.QFrame.Box)
        self.label_outline.setLineWidth(1)
        self.label_outline.setText("")
        self.label_outline.setObjectName("label_outline")
        self.label_18 = QtWidgets.QLabel(self.main_right)
        self.label_18.setGeometry(QtCore.QRect(0, 320, 81, 39))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_title = QtWidgets.QLabel(self.main_right)
        self.label_title.setGeometry(QtCore.QRect(80, 220, 491, 39))
        self.label_title.setFrameShape(QtWidgets.QFrame.Box)
        self.label_title.setLineWidth(1)
        self.label_title.setText("")
        self.label_title.setObjectName("label_title")
        self.label_20 = QtWidgets.QLabel(self.main_right)
        self.label_20.setGeometry(QtCore.QRect(0, 220, 81, 39))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_director = QtWidgets.QLabel(self.main_right)
        self.label_director.setGeometry(QtCore.QRect(80, 120, 201, 39))
        self.label_director.setFrameShape(QtWidgets.QFrame.Box)
        self.label_director.setLineWidth(1)
        self.label_director.setText("")
        self.label_director.setObjectName("label_director")
        self.label_publish = QtWidgets.QLabel(self.main_right)
        self.label_publish.setGeometry(QtCore.QRect(370, 170, 201, 39))
        self.label_publish.setFrameShape(QtWidgets.QFrame.Box)
        self.label_publish.setText("")
        self.label_publish.setObjectName("label_publish")
        self.label_23 = QtWidgets.QLabel(self.main_right)
        self.label_23.setGeometry(QtCore.QRect(0, 120, 81, 39))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.main_right)
        self.label_24.setGeometry(QtCore.QRect(290, 170, 81, 39))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_studio = QtWidgets.QLabel(self.main_right)
        self.label_studio.setGeometry(QtCore.QRect(80, 170, 201, 39))
        self.label_studio.setFrameShape(QtWidgets.QFrame.Box)
        self.label_studio.setLineWidth(1)
        self.label_studio.setText("")
        self.label_studio.setObjectName("label_studio")
        self.label_label = QtWidgets.QLabel(self.main_right)
        self.label_label.setGeometry(QtCore.QRect(370, 120, 201, 39))
        self.label_label.setFrameShape(QtWidgets.QFrame.Box)
        self.label_label.setText("")
        self.label_label.setObjectName("label_label")
        self.label_30 = QtWidgets.QLabel(self.main_right)
        self.label_30.setGeometry(QtCore.QRect(0, 170, 81, 39))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.main_right)
        self.label_31.setGeometry(QtCore.QRect(290, 120, 81, 39))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_tag = QtWidgets.QLabel(self.main_right)
        self.label_tag.setGeometry(QtCore.QRect(80, 370, 491, 39))
        self.label_tag.setFrameShape(QtWidgets.QFrame.Box)
        self.label_tag.setLineWidth(1)
        self.label_tag.setText("")
        self.label_tag.setObjectName("label_tag")
        self.label_33 = QtWidgets.QLabel(self.main_right)
        self.label_33.setGeometry(QtCore.QRect(0, 370, 81, 39))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.checkBox_cover = QtWidgets.QCheckBox(self.main_right)
        self.checkBox_cover.setGeometry(QtCore.QRect(0, 520, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_cover.setFont(font)
        self.checkBox_cover.setObjectName("checkBox_cover")
        self.label_progress = QtWidgets.QLabel(self.main_right)
        self.label_progress.setGeometry(QtCore.QRect(480, 520, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_progress.setFont(font)
        self.label_progress.setObjectName("label_progress")
        self.horizontalLayout_2.addWidget(self.main_right)
        self.stackedWidget.addWidget(self.page_avdc)
        self.page_tool = QtWidgets.QWidget()
        self.page_tool.setObjectName("page_tool")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_tool)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.page_tool)
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setGeometry(QtCore.QRect(230, 60, 511, 41))
        self.label_8.setObjectName("label_8")
        self.pushButton_move_mp4 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_move_mp4.setGeometry(QtCore.QRect(10, 30, 201, 71))
        self.pushButton_move_mp4.setObjectName("pushButton_move_mp4")
        self.label_41 = QtWidgets.QLabel(self.groupBox_6)
        self.label_41.setGeometry(QtCore.QRect(230, 30, 81, 24))
        self.label_41.setObjectName("label_41")
        self.lineEdit_escape_dir_move = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_escape_dir_move.setGeometry(QtCore.QRect(310, 30, 431, 24))
        self.lineEdit_escape_dir_move.setObjectName("lineEdit_escape_dir_move")
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.page_tool)
        self.groupBox_7.setObjectName("groupBox_7")
        self.label = QtWidgets.QLabel(self.groupBox_7)
        self.label.setGeometry(QtCore.QRect(230, 60, 511, 41))
        self.label.setObjectName("label")
        self.pushButton_select_file = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_select_file.setGeometry(QtCore.QRect(10, 30, 201, 71))
        self.pushButton_select_file.setObjectName("pushButton_select_file")
        self.comboBox_website = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_website.setGeometry(QtCore.QRect(310, 30, 431, 22))
        self.comboBox_website.setObjectName("comboBox_website")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.comboBox_website.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox_7)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 72, 21))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.groupBox_7)
        self.groupBox_12 = QtWidgets.QGroupBox(self.page_tool)
        self.groupBox_12.setObjectName("groupBox_12")
        self.pushButton_add_actor_pic = QtWidgets.QPushButton(self.groupBox_12)
        self.pushButton_add_actor_pic.setGeometry(QtCore.QRect(10, 30, 201, 71))
        self.pushButton_add_actor_pic.setObjectName("pushButton_add_actor_pic")
        self.lineEdit_emby_url = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_emby_url.setGeometry(QtCore.QRect(310, 30, 431, 21))
        self.lineEdit_emby_url.setObjectName("lineEdit_emby_url")
        self.label_3 = QtWidgets.QLabel(self.groupBox_12)
        self.label_3.setGeometry(QtCore.QRect(230, 30, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_12)
        self.label_4.setGeometry(QtCore.QRect(230, 74, 72, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_api_key = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_api_key.setGeometry(QtCore.QRect(310, 70, 431, 21))
        self.lineEdit_api_key.setObjectName("lineEdit_api_key")
        self.label_5 = QtWidgets.QLabel(self.groupBox_12)
        self.label_5.setGeometry(QtCore.QRect(230, 110, 511, 71))
        self.label_5.setObjectName("label_5")
        self.pushButton_show_pic_actor = QtWidgets.QPushButton(self.groupBox_12)
        self.pushButton_show_pic_actor.setGeometry(QtCore.QRect(10, 140, 201, 31))
        self.pushButton_show_pic_actor.setObjectName("pushButton_show_pic_actor")
        self.comboBox_pic_actor = QtWidgets.QComboBox(self.groupBox_12)
        self.comboBox_pic_actor.setGeometry(QtCore.QRect(10, 110, 201, 21))
        self.comboBox_pic_actor.setObjectName("comboBox_pic_actor")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.comboBox_pic_actor.addItem("")
        self.verticalLayout_2.addWidget(self.groupBox_12)
        self.groupBox_13 = QtWidgets.QGroupBox(self.page_tool)
        self.groupBox_13.setObjectName("groupBox_13")
        self.pushButton_select_fanart = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_select_fanart.setGeometry(QtCore.QRect(10, 20, 201, 71))
        self.pushButton_select_fanart.setObjectName("pushButton_select_fanart")
        self.label_6 = QtWidgets.QLabel(self.groupBox_13)
        self.label_6.setGeometry(QtCore.QRect(230, 20, 511, 71))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.groupBox_13)
        self.stackedWidget.addWidget(self.page_tool)
        self.page_setting = QtWidgets.QWidget()
        self.page_setting.setObjectName("page_setting")
        self.pushButton_save_config = QtWidgets.QPushButton(self.page_setting)
        self.pushButton_save_config.setGeometry(QtCore.QRect(210, 660, 361, 28))
        self.pushButton_save_config.setObjectName("pushButton_save_config")
        self.groupBox_8 = QtWidgets.QGroupBox(self.page_setting)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 530, 761, 121))
        self.groupBox_8.setObjectName("groupBox_8")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_8)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(0, 20, 751, 110))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_43 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_43.setObjectName("label_43")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.lineEdit_dir_name = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_dir_name.setObjectName("lineEdit_dir_name")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dir_name)
        self.label_44 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_44.setObjectName("label_44")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_44)
        self.lineEdit_media_name = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_media_name.setObjectName("lineEdit_media_name")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_media_name)
        self.label_45 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_45.setObjectName("label_45")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_45)
        self.lineEdit_local_name = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_local_name.setObjectName("lineEdit_local_name")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_local_name)
        self.groupBox_9 = QtWidgets.QGroupBox(self.page_setting)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 400, 751, 121))
        self.groupBox_9.setObjectName("groupBox_9")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_9)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 751, 91))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_25 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_25.setObjectName("label_25")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.lineEdit_proxy = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_proxy.setObjectName("lineEdit_proxy")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_proxy)
        self.label_26 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_26.setObjectName("label_26")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.lineEdit_timeout = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_timeout.setObjectName("lineEdit_timeout")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_timeout)
        self.label_27 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_27.setObjectName("label_27")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.lineEdit_retry = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_retry.setObjectName("lineEdit_retry")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_retry)
        self.groupBox_10 = QtWidgets.QGroupBox(self.page_setting)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 10, 751, 381))
        self.groupBox_10.setObjectName("groupBox_10")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_10)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(0, 250, 751, 121))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_37 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_37.setObjectName("label_37")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_37)
        self.lineEdit_fail = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_fail.setObjectName("lineEdit_fail")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fail)
        self.label_39 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_39.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_39.setObjectName("label_39")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_39)
        self.lineEdit_success = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_success.setObjectName("lineEdit_success")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_success)
        self.label_40 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_40.setObjectName("label_40")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.lineEdit_escape_dir = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_escape_dir.setObjectName("lineEdit_escape_dir")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_escape_dir)
        self.label_38 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_38.setObjectName("label_38")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.lineEdit_escape_char = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_escape_char.setObjectName("lineEdit_escape_char")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_escape_char)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_10)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 731, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName("groupBox")
        self.radioButton_common = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_common.setGeometry(QtCore.QRect(190, 10, 181, 19))
        self.radioButton_common.setObjectName("radioButton_common")
        self.radioButton_sort = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_sort.setGeometry(QtCore.QRect(490, 10, 181, 19))
        self.radioButton_sort.setObjectName("radioButton_sort")
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_soft_on = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_soft_on.setGeometry(QtCore.QRect(190, 10, 181, 19))
        self.radioButton_soft_on.setObjectName("radioButton_soft_on")
        self.radioButton_soft_off = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_soft_off.setGeometry(QtCore.QRect(490, 10, 181, 19))
        self.radioButton_soft_off.setObjectName("radioButton_soft_off")
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_debug_on = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_debug_on.setGeometry(QtCore.QRect(190, 10, 181, 19))
        self.radioButton_debug_on.setObjectName("radioButton_debug_on")
        self.radioButton_debug_off = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_debug_off.setGeometry(QtCore.QRect(490, 10, 181, 19))
        self.radioButton_debug_off.setObjectName("radioButton_debug_off")
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton_update_on = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_update_on.setGeometry(QtCore.QRect(190, 10, 181, 19))
        self.radioButton_update_on.setObjectName("radioButton_update_on")
        self.radioButton_update_off = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_update_off.setGeometry(QtCore.QRect(490, 10, 181, 19))
        self.radioButton_update_off.setObjectName("radioButton_update_off")
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton_emby = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_emby.setGeometry(QtCore.QRect(190, 10, 181, 19))
        self.radioButton_emby.setObjectName("radioButton_emby")
        self.radioButton_plex = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_plex.setGeometry(QtCore.QRect(420, 10, 181, 19))
        self.radioButton_plex.setObjectName("radioButton_plex")
        self.radioButton_kodi = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_kodi.setGeometry(QtCore.QRect(600, 10, 115, 19))
        self.radioButton_kodi.setObjectName("radioButton_kodi")
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.groupBox_11 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_11.setObjectName("groupBox_11")
        self.radioButton_all = QtWidgets.QRadioButton(self.groupBox_11)
        self.radioButton_all.setGeometry(QtCore.QRect(190, 10, 291, 19))
        self.radioButton_all.setObjectName("radioButton_all")
        self.radioButton_javdb = QtWidgets.QRadioButton(self.groupBox_11)
        self.radioButton_javdb.setGeometry(QtCore.QRect(490, 10, 115, 19))
        self.radioButton_javdb.setObjectName("radioButton_javdb")
        self.verticalLayout_3.addWidget(self.groupBox_11)
        self.stackedWidget.addWidget(self.page_setting)
        self.page_about = QtWidgets.QWidget()
        self.page_about.setObjectName("page_about")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_about)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_about = QtWidgets.QTextBrowser(self.page_about)
        self.textBrowser_about.setObjectName("textBrowser_about")
        self.verticalLayout_4.addWidget(self.textBrowser_about)
        self.stackedWidget.addWidget(self.page_about)
        self.page_log = QtWidgets.QWidget()
        self.page_log.setObjectName("page_log")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_log)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowser_log_main = QtWidgets.QTextBrowser(self.page_log)
        self.textBrowser_log_main.setObjectName("textBrowser_log_main")
        self.verticalLayout_5.addWidget(self.textBrowser_log_main)
        self.stackedWidget.addWidget(self.page_log)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        AVDV.setCentralWidget(self.centralwidget)

        self.retranslateUi(AVDV)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AVDV)

    def retranslateUi(self, AVDV):
        _translate = QtCore.QCoreApplication.translate
        AVDV.setWindowTitle(_translate("AVDV", "AVDC-3.73"))
        self.label_ico.setText(_translate("AVDV", "图标"))
        self.pushButton_close.setText(_translate("AVDV", "X"))
        self.pushButton_min.setText(_translate("AVDV", "-"))
        self.pushButton_main.setText(_translate("AVDV", "主界面"))
        self.pushButton_log.setText(_translate("AVDV", "日志"))
        self.pushButton_tool.setText(_translate("AVDV", "工具"))
        self.pushButton_setting.setText(_translate("AVDV", "设置"))
        self.pushButton_about.setText(_translate("AVDV", "关于"))
        self.treeWidget_number.headerItem().setText(0, _translate("AVDV", "番号"))
        __sortingEnabled = self.treeWidget_number.isSortingEnabled()
        self.treeWidget_number.setSortingEnabled(False)
        self.treeWidget_number.topLevelItem(0).setText(0, _translate("AVDV", "成功"))
        self.treeWidget_number.topLevelItem(1).setText(0, _translate("AVDV", "失败"))
        self.treeWidget_number.setSortingEnabled(__sortingEnabled)
        self.pushButton_start_cap.setText(_translate("AVDV", "开始"))
        self.textBrowser_warning.setHtml(_translate("AVDV", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:10.5pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:600; color:#000000;\">反馈BUG，请：开调试模式后截图日志。</span></p></body></html>"))
        self.label_percent.setText(_translate("AVDV", "0%"))
        self.label_poster.setText(_translate("AVDV", "封面图"))
        self.label_fanart.setText(_translate("AVDV", "缩略图"))
        self.label_11.setText(_translate("AVDV", "番号："))
        self.label_13.setText(_translate("AVDV", "发行日期："))
        self.label_15.setText(_translate("AVDV", "演员："))
        self.label_18.setText(_translate("AVDV", "简介："))
        self.label_20.setText(_translate("AVDV", "标题："))
        self.label_23.setText(_translate("AVDV", "导演："))
        self.label_24.setText(_translate("AVDV", "发行："))
        self.label_30.setText(_translate("AVDV", "制作："))
        self.label_31.setText(_translate("AVDV", "系列："))
        self.label_33.setText(_translate("AVDV", "类别："))
        self.checkBox_cover.setText(_translate("AVDV", "显示封面(取消勾选后，立即关闭封面显示)"))
        self.label_progress.setText(_translate("AVDV", "0/0"))
        self.groupBox_6.setTitle(_translate("AVDV", "视频、字幕移动"))
        self.label_8.setText(_translate("AVDV", "程序所在目录的所有子目录(不包括排除目录)下的视频及同名字幕， 移动到当前目录下。"))
        self.pushButton_move_mp4.setText(_translate("AVDV", "开始移动"))
        self.label_41.setText(_translate("AVDV", "排除目录："))
        self.groupBox_7.setTitle(_translate("AVDV", "单文件刮削"))
        self.label.setText(_translate("AVDV", "选择单个文件(程序目录下或者子目录下)，使用文件名做为番号进行刮削。"))
        self.pushButton_select_file.setText(_translate("AVDV", "选择文件"))
        self.comboBox_website.setItemText(0, _translate("AVDV", "All websites"))
        self.comboBox_website.setItemText(1, _translate("AVDV", "javdb"))
        self.comboBox_website.setItemText(2, _translate("AVDV", "javbus"))
        self.comboBox_website.setItemText(3, _translate("AVDV", "avsox"))
        self.comboBox_website.setItemText(4, _translate("AVDV", "fc2club"))
        self.comboBox_website.setItemText(5, _translate("AVDV", "fanza"))
        self.comboBox_website.setItemText(6, _translate("AVDV", "siro(mgstage)"))
        self.comboBox_website.setItemText(7, _translate("AVDV", "javlibrary"))
        self.label_2.setText(_translate("AVDV", "刮削网站:"))
        self.groupBox_12.setTitle(_translate("AVDV", "Emby-女优头像"))
        self.pushButton_add_actor_pic.setText(_translate("AVDV", "添加头像"))
        self.label_3.setText(_translate("AVDV", "Emby地址："))
        self.label_4.setText(_translate("AVDV", "API密钥："))
        self.label_5.setText(_translate("AVDV", "说明: 1、头像请放在程序目录(AVDC目录)下的Actor目录中。 2、密钥创建方法：Emby控制台->高级->API密钥->添加(APP名称任意)。"))
        self.pushButton_show_pic_actor.setText(_translate("AVDV", "查看"))
        self.comboBox_pic_actor.setItemText(0, _translate("AVDV", "可添加头像的女优"))
        self.comboBox_pic_actor.setItemText(1, _translate("AVDV", "没有头像的女优"))
        self.comboBox_pic_actor.setItemText(2, _translate("AVDV", "已有头像的女优"))
        self.comboBox_pic_actor.setItemText(3, _translate("AVDV", "所有女优"))
        self.groupBox_13.setTitle(_translate("AVDV", "裁剪封面图"))
        self.pushButton_select_fanart.setText(_translate("AVDV", "选择缩略图"))
        self.label_6.setText(_translate("AVDV", "说明: 1、对有些封面图(.png)不满意,比例不对或者分辨率太低,可使用此工具。 2、此工具通过判断人脸位置，可以将缩略图(.jpg)裁剪为封面图。 3、不要选择Backdrop.jpg。"))
        self.pushButton_save_config.setText(_translate("AVDV", "保存"))
        self.groupBox_8.setTitle(_translate("AVDV", "命名规则"))
        self.label_43.setText(_translate("AVDV", "目录命名："))
        self.label_44.setText(_translate("AVDV", "视频标题(媒体库中)："))
        self.label_45.setText(_translate("AVDV", "视频标题(本地文件)："))
        self.groupBox_9.setTitle(_translate("AVDV", "代理设置"))
        self.label_25.setText(_translate("AVDV", "代理:"))
        self.label_26.setText(_translate("AVDV", "超时重试时间："))
        self.label_27.setText(_translate("AVDV", "重试次数："))
        self.groupBox_10.setTitle(_translate("AVDV", "普通设置"))
        self.label_37.setText(_translate("AVDV", "失败输出目录："))
        self.label_39.setText(_translate("AVDV", "成功输出目录："))
        self.label_40.setText(_translate("AVDV", "排除目录："))
        self.label_38.setText(_translate("AVDV", "异常字符："))
        self.groupBox.setTitle(_translate("AVDV", "模式："))
        self.radioButton_common.setText(_translate("AVDV", "普通模式"))
        self.radioButton_sort.setText(_translate("AVDV", "整理模式"))
        self.groupBox_2.setTitle(_translate("AVDV", "软链接模式："))
        self.radioButton_soft_on.setText(_translate("AVDV", "开"))
        self.radioButton_soft_off.setText(_translate("AVDV", "关"))
        self.groupBox_3.setTitle(_translate("AVDV", "调试模式："))
        self.radioButton_debug_on.setText(_translate("AVDV", "开"))
        self.radioButton_debug_off.setText(_translate("AVDV", "关"))
        self.groupBox_4.setTitle(_translate("AVDV", "检测更新："))
        self.radioButton_update_on.setText(_translate("AVDV", "开"))
        self.radioButton_update_off.setText(_translate("AVDV", "关"))
        self.groupBox_5.setTitle(_translate("AVDV", "媒体库："))
        self.radioButton_emby.setText(_translate("AVDV", "emby/jellyfin"))
        self.radioButton_plex.setText(_translate("AVDV", "plex"))
        self.radioButton_kodi.setText(_translate("AVDV", "kodi"))
        self.groupBox_11.setTitle(_translate("AVDV", "网站选择："))
        self.radioButton_all.setText(_translate("AVDV", "All websites"))
        self.radioButton_javdb.setText(_translate("AVDV", "Only javdb"))
        self.textBrowser_about.setHtml(_translate("AVDV", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:10.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:20pt; font-weight:600;\">AVDC</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:14pt; font-weight:600;\">目录</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#_一、功能简介\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\"> 一、功能简介</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#_二、项目简介\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\"> 二、项目简介</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#_设置说明\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\"> 三、设置说明</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"#_四、更新日志\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\"> 四、更新日志</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-weight:600;\"> </span></p>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_一、功能简介\"></a><span style=\" font-family:\'宋体\'; font-size:22pt; font-weight:600;\">一</span><span style=\" font-family:\'宋体\'; font-size:22pt; font-weight:600;\">、功能简介</span></h1>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 日本电影</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">元数据抓取工具</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">/刮削器，配合本地影片管理软件</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">EMBY,KODI，PLEX</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">等管理本地影片，该软件起到分类与元数据抓取作用，利用元数据信息来分类，供本地影片</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">分类整理</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">使用。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> </span></p>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_二、项目简介\"></a><span style=\" font-family:\'宋体\'; font-size:22pt; font-weight:600;\">二</span><span style=\" font-family:\'宋体\'; font-size:22pt; font-weight:600;\">、项目简介</span></h1>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\"> G</span><span style=\" font-family:\'Calibri\'; font-size:12pt;\">ui made by </span><span style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:600; color:#ff0000;\">moy</span><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600; color:#ff0000;\">y</span><span style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:600; color:#ff0000;\">996</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，C</span><span style=\" font-family:\'Calibri\'; font-size:12pt;\">ore made by </span><span style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:600; color:#ff0000;\">yoshiko2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt;\"> tg</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">官方电报群</span><span style=\" font-family:\'Calibri\'; font-size:12pt;\">:</span><a href=\"https://t.me/joinchat/J54y1g3-a7nxJ_-WS4-KFQ\"><span style=\" font-family:\'Calibri\'; font-size:12pt; text-decoration: underline; color:#0000ff;\"> </span></a><a href=\"https://t.me/joinchat/J54y1g3-a7nxJ_-WS4-KFQ\"><span style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://t.me/joinchat/J54y1g3-a7nxJ_-WS4-KFQ</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\"> 命令行版项目地址：</span><a href=\"https://github.com/yoshiko2/AV_Data_Capture\"><span style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://github.com/yoshiko2/AV_Data_Capture</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\"> GUI版项目地址：</span><a href=\"https://github.com/moyy996/AVDC\"><span style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://github.com/moyy996/AVDC</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\"> GUI版</span><span style=\" font-family:\'Calibri\'; font-size:12pt;\">EXE</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">下载地址：</span><a href=\"https://github.com/moyy996/AVDC/releases\"><span style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://github.com/moyy996/AVDC/releases</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\"> </span></p>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"_设置说明\"></a><span style=\" font-family:\'宋体\'; font-size:22pt; font-weight:600;\">三</span><span style=\" font-family:\'宋体\'; font-size:22pt; font-weight:600;\">、设置说明</span></h1>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 更详细的说明： </span><a href=\"https://github.com/moyy996/AVDC/blob/master/README.md\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; text-decoration: underline; color:#24292e; background-color:#ffffff;\">https://github.com/moyy996/AVDC/blob/master/README.md</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; text-decoration: underline; color:#24292e;\"> </span></p>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600;\">1、普通模式/整理模式</span></h4>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; font-weight:600; color:#000000; background-color:#ffffff;\"> </span><span style=\" font-family:\'宋体\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">普通模式</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">：通过番号刮削数据，包括元数据、封面图、缩略图、背景图。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; font-weight:600; color:#000000; background-color:#ffffff;\"> </span><span style=\" font-family:\'宋体\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">整理模式</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">：仅根据女优把电影命名为番号并分类到女优名称的文件夹下</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e;\"> </span></p>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600;\">2、软链接模式：使用此模式，要以</span><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600; text-decoration: underline; color:#ff0000;\">管理员身份</span><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600;\">运行。</span></h4>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 刮削完</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">不移动视频</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">，而是在相应目录创建软链接（类似于快捷方式），</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">方便PT下载完既想刮削又想继续上传的仓鼠党同志</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e;\"> </span></p>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600;\">3、调试模式</span></h4>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 输出番号的元数据，包括封面，导演，演员，简介等。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e;\"> </span></p>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600;\">4、排除目录</span></h4>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 在多层目录刮削时排除所填目录。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e;\"> </span></p>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600;\">5、异常字符</span></h4>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 在创建文件夹时，删除指定的字符。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'宋体\'; font-size:9.5pt; color:#24292e;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600;\">6、命名规则</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; font-weight:600; background-color:#ffffff;\"> 1、</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">目录命名</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">：存放视频数据的目录名，支持</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">多层目录</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">，支持</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">自定义符号</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">，例：[actor]/studio/number-【title】。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; font-weight:600; background-color:#ffffff;\"> 2、</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">视频标题</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">：nfo中的标题命名。例：</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">number-</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">[</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">title</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">]。可以自定义符号。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> </span><span style=\" font-family:\'宋体\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">3、</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">可选项为</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">title（片名）、actor（演员）、studio（制作商）、director（导演）、release（发售日）、year（发行年份）、number（番号）、runtime（时长）、</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">series（系列）、publisher（发行商）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e;\"> </span></p>\n"
"<h4 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt; font-weight:600;\">7、网站选择</span></h4>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">、</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">All website</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">: </span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">使用</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">avsox,javbus,fanza,javdb,fc2club</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">进行刮削。</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"><br /> 2</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">、</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">Only javdb</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">: </span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">仅使用</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">javdb</span><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">进行刮削。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:9.5pt; color:#24292e;\"> </span></p>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:22pt; font-weight:600;\">四、更新日志</span></h1>\n"
"<h1 style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'宋体\'; font-size:22pt; font-weight:600;\"><br /></h1>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:18pt; font-weight:600; color:#ff0000;\">3.7</span></h1>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-02-15 19:30更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">可选项变更：</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">title（片名）、actor（演员）、studio（制作商）、director（导演）、release（发售日）、year（发行年份）、number（番号）、runtime（时长）、</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">series（系列）、publisher（发行商）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">修复：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、修改javbus的抓取逻辑，成功率提高。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 2、更新</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">进度条</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">改为刮削完之后。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 3、不再强制替换‘_’为‘-’。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 4、EMBY添加头像时，演员有别名，</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">中文符号</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">导致添加失败。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 5、修复字幕移动，与视频文件同名的</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">字幕</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">，刮削完后会随视频一起移动。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">新增：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">自定义本地文件名</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 2、获取</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">制作商，发行商</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 3、标签加入</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">系列、发行商、制作商</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">(太多标签EMBY只显示一部分)。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 4、小工具-</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">视频移动</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">，会移动与视频文件同名的</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">字幕</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:18pt; font-weight:600; color:#ff0000;\">3.61</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-02-12-15:40更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">修复：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">演员过多</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">导致文件夹创建失败。(只取</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">前三个</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">)<br /> 2、avsox有多个封面图时导致失败。<br /> 3、主页面-</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">封面开关</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">不管用。<br /> 4、</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">制作商、导演</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">抓取错误。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e;\"><br /></p>\n"
"<h1 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:18pt; font-weight:600; color:#ff0000;\">3.6</span></h1>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-02-11 晚23点更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">新增：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、修改</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">主界面UI</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">，显示</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">封面，番号、标题</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">等数据。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 2、刮削完的番号会添加到</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">主界面左侧</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 3、刮削</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">成功</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">的可以</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">点选</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">，查看刮削到的</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">数据、封面</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">等。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 4、</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">失败</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">的可以根据对应</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">序号</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">，去日志页查看具体</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">报错信息</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:18pt; font-weight:600; color:#ff0000;\">3.5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-02-11 凌晨更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">新增：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、小工具-</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">裁剪封面图</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">： 裁剪</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">缩略图</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">为</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">封面图</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。，针对比例错误，分辨率低的情况。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 2、更改</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">命名规则</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">，支持</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">自定义符号</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">，例如:[actor]/number-【title】-（release）。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">修复：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、avsox封面存在下载失败情况，修改无码片首先到javbus查找。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 2、封面图下载失败后，将缩略图裁剪为封面图。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 3、Fc2、javdb无码封面图比例不对，会进行裁剪。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:18pt; font-weight:600; color:#ff0000;\">3.41</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-02-09-15点更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">新增:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、小工具-</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">单个</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">抓取的文件名</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">去掉-CD、-C</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。<br /> 2、tag,genre添加</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">系列</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。<br /> 3、Actor中上传成功的头像复制到</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">Success</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">目录。</span></p>\n"
"<h1 style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'宋体\'; font-size:22pt; font-weight:600;\"><br /></h1>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:18pt; font-weight:600; color:#ff0000;\">3.4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-02-07-晚20点 更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">新增:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">批量添加</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">emby</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">演员头像</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 2、查看</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">可添加头像</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">的演员，</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">有头像、无头像、所有</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">演员。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:18pt; font-weight:600; color:#ff0000;\">3.32</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-02-06-19:10更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">修复:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、无法识别</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">111111-MMMM</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">这种番号。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">新增:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、小工具-</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">单个抓取</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">,支持选择</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#24292e; background-color:#ffffff;\">刮削网站</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:18pt; font-weight:600; color:#ff0000;\">3.31</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-02-05-21:42更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">修复:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、仅JAVDB时，番号跟封面图不匹配的BUG。<br /> 2、优化报错信息的输出。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:18pt; font-weight:600; color:#ff0000;\">3.3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-02-05 凌晨更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">修复:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、分集刮削时文件命名出错。<br /> 2、javdb中演员有多曾用名时出错。<br /> 3、文件的命名都采用网站刮削到的番号命名</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:18pt; font-weight:600; color:#ff0000;\">3.22</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-02-04 更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">修复：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、javdb,avsox抓取到但是显示抓取失败。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">新增：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、文件夹命名支持</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">多级目录</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">，例：actor/studio/number-release。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:18pt; font-weight:600; color:#ff0000;\">3.21</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-02-03-20:24更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">新增：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">刮削网站</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">可选，</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">全部网站</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">(avsox,javbus,fanza,javdb,fc2club)，或者</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">仅JAVDB</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。<br /> 2、改进javdb刮削逻辑。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:18pt; font-weight:600; color:#ff0000;\">3.2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-02-03 更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">修复：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、找不到影片信息时依然创建目录、下载空图片的问题。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 2、界面微调。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 3、修复</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">MIDE139</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">抓取不到的情况。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">新增：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">进度条</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">显示。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 2、一次刮削任务未结束，</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">开始按钮</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">不可用。结束后才可用。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:18pt; font-weight:600; color:#ff0000;\">3.1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-02-02更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">修复：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、修复文件夹自定义命名规则时，使用studio、release等刮削失败的bug。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 2、去掉背景透明。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 3、去掉javdb爬虫工具。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:11pt; font-weight:600; color:#24292e; background-color:#ffffff;\">新增： </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、工具新增</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">单个文件刮削</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。针对个别刮削失败的情况，使用文件名做番号。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 2、</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">更改</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">自定义文件夹命名、媒体库标题</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">命名规则</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\';\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/moyy996/AVDC/releases/tag/3.0\"><span style=\" font-family:\'Calibri\'; font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">3.0-GUI</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:11pt; font-weight:600;\">2020-01-31 更新</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> 1、第一个GUI版本。<br /> 2、两个工具-javdb爬虫、视频移动。<br /> 3、可视化编辑config.ini。<br /> 4、多层目录刮削，增加</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; font-weight:600; color:#ff0000; background-color:#ffffff;\">排除目录</span><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\">选项。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:9.5pt; color:#24292e; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\';\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\';\"> </span></p></body></html>"))
