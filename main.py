import sys, os

from PySide2.QtWidgets import QMainWindow, QFileDialog, QApplication
from translate import Ui_Dialog


# 创建APP类，并继承UI的类
class TranslateApp(QMainWindow, Ui_Dialog):
    # 初始化构造函数
    def __init__(self):
        # 继承： super指父类（子类，实例）.构造函数
        super(TranslateApp, self).__init__()
        self.setupUi(self)
        # 把UI中的控件连接函数功能（事件）

    # 功能函数

# 创建实例
def main():
    # 创建新的实例应用
    app = QApplication(sys.argv)
    # 我们将表单设置为WoHeYunApp
    widgets = TranslateApp()
    # 显示我们的表单
    widgets.show()
    # 退出程序
    app.exec_()


# 如果我们直接运行文件而不是导入它，则执行
if __name__ == '__main__':
    main()
