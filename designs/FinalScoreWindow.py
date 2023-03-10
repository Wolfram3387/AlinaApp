# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Wolfram_3387/Downloads/FinalScoreWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(585, 720)
        Dialog.setStyleSheet("background-color:#B0C4DE")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 120, 531, 580))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Vuz = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Vuz.setFont(font)
        self.label_Vuz.setStyleSheet("color:#3E5F8A")
        self.label_Vuz.setObjectName("label_Vuz")
        self.verticalLayout.addWidget(self.label_Vuz)
        self.textEdit_Vuz = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_Vuz.setStyleSheet("background-color:white;color:black")
        self.textEdit_Vuz.setReadOnly(True)
        self.textEdit_Vuz.setObjectName("textEdit_Vuz")
        self.verticalLayout.addWidget(self.textEdit_Vuz)
        self.label_Site = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Site.setFont(font)
        self.label_Site.setStyleSheet("color:#3E5F8A")
        self.label_Site.setObjectName("label_Site")
        self.verticalLayout.addWidget(self.label_Site)
        self.textBrowser_Site = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_Site.setStyleSheet("background-color:white;color:black")
        self.textBrowser_Site.setReadOnly(True)
        self.textBrowser_Site.setObjectName("textBrowser_Site")
        self.verticalLayout.addWidget(self.textBrowser_Site)
        self.label_Direction = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Direction.setFont(font)
        self.label_Direction.setStyleSheet("color:#3E5F8A")
        self.label_Direction.setObjectName("label_Direction")
        self.verticalLayout.addWidget(self.label_Direction)
        self.textEdit_Direction = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_Direction.setStyleSheet("background-color:white;color:black")
        self.textEdit_Direction.setReadOnly(True)
        self.textEdit_Direction.setObjectName("textEdit_Direction")
        self.verticalLayout.addWidget(self.textEdit_Direction)
        self.label_Score = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Score.setFont(font)
        self.label_Score.setStyleSheet("color:#3E5F8A")
        self.label_Score.setObjectName("label_Score")
        self.verticalLayout.addWidget(self.label_Score)
        self.textEdit_Score = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_Score.setStyleSheet("background-color:white;color:black")
        self.textEdit_Score.setReadOnly(True)
        self.textEdit_Score.setObjectName("textEdit_Score")
        self.verticalLayout.addWidget(self.textEdit_Score)
        self.label_Chances = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Chances.setFont(font)
        self.label_Chances.setStyleSheet("color:#3E5F8A")
        self.label_Chances.setObjectName("label_Chances")
        self.verticalLayout.addWidget(self.label_Chances)
        self.textEdit_Chances = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_Chances.setStyleSheet("background-color:white;color:black")
        self.textEdit_Chances.setReadOnly(True)
        self.textEdit_Chances.setObjectName("textEdit_Chances")
        self.verticalLayout.addWidget(self.textEdit_Chances)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 585, 111))
        self.frame.setStyleSheet("background-color:#6C92AF")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(440, 210, 585, 211))
        self.frame_2.setStyleSheet("background-color:#6C92AF")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(200, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:#3E5F8A")
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setObjectName("label_6")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 70, 491, 131))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("color:#434B4D\n"
"")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(460, 200, 585, 211))
        self.frame_3.setStyleSheet("background-color:#6C92AF")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(200, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#3E5F8A")
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setObjectName("label_7")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(50, 70, 491, 131))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("color:#434B4D\n"
"")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(440, 210, 585, 211))
        self.frame_4.setStyleSheet("background-color:#6C92AF")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(200, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#3E5F8A")
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.frame_4)
        self.textBrowser_4.setGeometry(QtCore.QRect(50, 70, 491, 131))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setStyleSheet("color:#434B4D\n"
"")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(140, 20, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:#F5FFFA")
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_Vuz.setText(_translate("Dialog", "???????????????? ??????????????????:"))
        self.label_Site.setText(_translate("Dialog", "???????? ??????????????????:"))
        self.label_Direction.setText(_translate("Dialog", "?????????????????????? ???? ???????????? ??????????????????:"))
        self.label_Score.setText(_translate("Dialog", "?????????? ???? ???????????? ???????????????? ????????:"))
        self.label_Chances.setText(_translate("Dialog", "?????????? ?????????????????? (?? ???????????? ????????????????):"))
        self.label_6.setText(_translate("Dialog", "COSMOS APP"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sitka\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; color:#ffffff;\">????????????! ???????????????????? ???????? ???????????? ??????????????????, ???????????????????? ???????????????????????? ?? ???????????????????? ?????????????????????? ???? ???????????????????? ?????????????????????? ????????????????. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; color:#ffffff;\">???? ?????????? ?? ????????? </span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "COSMOS APP"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sitka\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; color:#ffffff;\">????????????! ???????????????????? ???????? ???????????? ??????????????????, ???????????????????? ???????????????????????? ?? ???????????????????? ?????????????????????? ???? ???????????????????? ?????????????????????? ????????????????. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; color:#ffffff;\">???? ?????????? ?? ????????? </span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "COSMOS APP"))
        self.textBrowser_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sitka\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; color:#ffffff;\">????????????! ???????????????????? ???????? ???????????? ??????????????????, ???????????????????? ???????????????????????? ?? ???????????????????? ?????????????????????? ???? ???????????????????? ?????????????????????? ????????????????. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; color:#ffffff;\">???? ?????????? ?? ????????? </span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "?????? ???????? ????????????????????:"))
