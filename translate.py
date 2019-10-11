# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'translate.ui',
# licensing of 'translate.ui' applies.
#
# Created: Tue Oct  8 21:16:09 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!


import uuid
import hashlib
import time
import json
import random
from PySide2 import QtCore, QtGui, QtWidgets
import requests
import icon


def baidu_translate(q):
    appid = '20191009000339969'  # 你的appid
    secretKey = 'UxLJEgDMWygKZ_owM8GB'  # 你的密钥
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    q = q
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    b = sign.encode(encoding='utf-8')
    m1.update(b)
    sign = m1.hexdigest()
    data = {
        'appid': appid,
        'q': q.encode('utf-8'),
        'from': fromLang,
        'to': toLang,
        'salt': str(salt),
        'sign': sign
    }
    res = requests.get(myurl, data)
    data = res.json()
    return data


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def youdao_translate(q):
    YOUDAO_URL = 'https://openapi.youdao.com/api'
    APP_KEY = '602fb863aba0d0f5'
    APP_SECRET = '2dP4JOSRH6L3HssfBNJmC4yxzCziWXFP'
    data = {}
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(YOUDAO_URL, data=data, headers=headers)
    contentType = response.headers['Content-Type']
    if contentType == "audio/mp3":
        millis = int(round(time.time() * 1000))
        filePath = "合成的音频存储路径" + str(millis) + ".mp3"
        fo = open(filePath, 'wb')
        fo.write(response.content)
        fo.close()
    else:
        print(response.text)
        data = json.loads(response.text)
        return data


class Ui_Dialog(object):
    def __init__(self):
        self.use = 1  # 1为有道，2为百度

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(533, 551)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 170, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 70, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtCore.Qt.IBeamCursor)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 220, 54, 12))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 170, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(100, 170, 71, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 170, 71, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(360, 510, 161, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(170, 240, 131, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(120, 290, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.retranslateUi(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowIcon(QtGui.QIcon('logo.png'))
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "简易翻译器", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialog", "清空", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "输入要查询的单词", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "查询结果", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Dialog", "查询", None, -1))
        self.radioButton.setText(QtWidgets.QApplication.translate("Dialog", "有道翻译", None, -1))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("Dialog", "百度翻译", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog", "LIBAO 制作简易翻译器 1.0", None, -1))
        self.textBrowser.setHtml(QtWidgets.QApplication.translate("Dialog",
                                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>",
                                                                  None, -1))

        self.pushButton.clicked.connect(self.clear_query)
        self.pushButton_2.clicked.connect(self.query)
        self.radioButton.clicked.connect(self.buttonClicked)
        self.radioButton_2.clicked.connect(self.buttonClicked)
        self.radioButton.click()

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == "有道翻译":
            self.use = 1
        else:
            self.use = 2

        self.statusBar().showMessage(sender.text() + ' 正在使用')

    def clear_query(self):
        self.lineEdit.clear()

    def query(self):
        query_word = self.lineEdit.text()
        if not query_word:
            pass
        else:
            if self.use == 1:
                data = youdao_translate(query_word)
                text = data['translation'][0]+'\n'
                if 'web' in data:
                    value = data['web'][0]['value']
                    for i in value:
                        text += i + '\n'
                self.label_5.setText(query_word)
                self.textBrowser.setText(text)
            elif self.use == 2:
                data = baidu_translate(query_word)
                text = data['trans_result'][0]['dst']
                self.label_5.setText(query_word)
                self.textBrowser.setText(text)
