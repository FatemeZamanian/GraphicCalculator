# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import math
import sys
from functools import partial

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget


class main(QWidget):
    def __init__(self):
        self.operator = ""
        self.text = ""
        self.text2 = ""
        self.op2 = ""
        self.text3 = ""
        super(main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('GraphicCalculator.ui', None)
        self.ui.show()
        self.ui.label.setText("")
        self.ui.pushButton.clicked.connect(partial(self.method_num, "1"))
        self.ui.pushButton_2.clicked.connect(partial(self.method_num, "2"))
        self.ui.pushButton_3.clicked.connect(partial(self.method_num, "3"))
        self.ui.pushButton_4.clicked.connect(partial(self.method_num, "4"))
        self.ui.pushButton_5.clicked.connect(partial(self.method_num, "5"))
        self.ui.pushButton_6.clicked.connect(partial(self.method_num, "6"))
        self.ui.pushButton_7.clicked.connect(partial(self.method_num, "7"))
        self.ui.pushButton_8.clicked.connect(partial(self.method_num, "8"))
        self.ui.pushButton_9.clicked.connect(partial(self.method_num, "9"))
        self.ui.pushButton_zero.clicked.connect(partial(self.method_num, "0"))
        self.ui.pushButton_dot.clicked.connect(partial(self.method_num, "."))
        self.ui.pushButton_answer.clicked.connect(self.method_answer)
        self.ui.pushButton_pluse.clicked.connect(partial(self.method_op, "+"))
        self.ui.pushButton_minus.clicked.connect(partial(self.method_op, "-"))
        self.ui.pushButton_multiple.clicked.connect(partial(self.method_op, "*"))
        self.ui.pushButton_devide.clicked.connect(partial(self.method_op, "/"))
        self.ui.pushButton_power.clicked.connect(partial(self.method_op, "**"))
        self.ui.pushButton_sin.clicked.connect(self.method_sin)
        self.ui.pushButton_cos.clicked.connect(self.method_cos)
        self.ui.pushButton_tan.clicked.connect(self.method_tan)
        self.ui.pushButton_clear.clicked.connect(self.method_clear)
        self.ui.pushButton_del.clicked.connect(self.method_delete)

    def method_num(self, num):
        text = self.ui.label.text()
        if num == '.':
            for t in text:
                if t == '.':
                    break
            else:
                self.ui.label.setText(text + num)
        else:
            self.ui.label.setText(text + num)

    def method_op(self, op):
        if self.operator != "":
            self.method_answer()
        self.text = self.ui.label.text()
        self.text = float(self.text)
        self.operator = op
        self.ui.label.setText("")

    def method_clear(self):
        self.ui.label.setText("")
        self.operator = ""
        self.text = ""
        self.text2 = ""
        self.text3 = ""
        self.op2 = ""

    def method_delete(self):
        self.text = self.ui.label.text()
        self.ui.label.setText(self.text[:len(self.text) - 1])

    def method_sin(self):
        if self.operator != "":
            self.text3 = self.text
            self.op2 = self.operator
            self.ui.label.setText("")
            self.text = ""
            self.operator = ""
            self.ui.method_sin()

        else:
            self.ui.label.setText("")
            self.operator = "sin"

    def method_cos(self):
        if self.operator != "":
            self.text3 = self.text
            self.op2 = self.operator
            self.ui.label.setText("")
            self.text = ""
            self.operator = ""
            self.ui.method_cos()

        else:
            self.ui.label.setText("")
            self.operator = "cos"

    def method_tan(self):
        if self.operator != "":
            self.text3 = self.text
            self.op2 = self.operator
            self.ui.label.setText("")
            self.text = ""
            self.operator = ""
            self.ui.method_tan()

        else:
            self.ui.label.setText("")
            self.operator = "tan"

    def method_answer(self):
        c = 0
        if self.operator == "+":
            self.text2 = self.ui.label.text()
            self.text2 = float(self.text2)
            self.text = float(self.text)
            self.ui.label.setText("")
            ans = self.text + self.text2
            self.text = ans
            self.ui.label.setText(str(self.text))
            self.operator = ""

        if self.operator == "-":
            self.text2 = self.ui.label.text()
            self.text2 = float(self.text2)
            self.ui.label.setText("")
            self.text = self.text - self.text2
            self.ui.label.setText(str(self.text))
            self.operator = ""

        if self.operator == "*":
            self.text2 = self.ui.label.text()
            self.text2 = float(self.text2)
            self.ui.label.setText("")
            self.text = self.text * self.text2
            self.ui.label.setText(str(self.text))
            self.operator = ""

        if self.operator == "/":
            self.text2 = self.ui.label.text()
            self.text2 = float(self.text2)
            self.ui.label.setText("")
            text = self.text / self.text2
            self.ui.label.setText(str(self.text))
            self.operator = ""

        if self.operator == "**":
            self.text2 = self.ui.label.text()
            self.text2 = float(self.text2)
            self.ui.label.setText("")
            self.text = math.pow(self.text, self.text2)
            self.ui.label.setText(str(self.text))
            self.operator = ""

        if self.operator == "sin":

            if self.text == "":
                self.text2 = self.ui.label.text()
                self.text2 = float(self.text2)
                self.ui.label.setText("")
                self.text2 = math.sin(math.radians(self.text2))
                self.ui.label.setText(str(self.text2))

        if self.operator == "cos":

            if self.text == "":
                self.text2 = self.ui.label.text()
                self.text2 = float(self.text2)
                self.ui.label.setText("")
                self.text2 = math.cos(math.radians(self.text2))
                self.ui.label.setText(str(self.text2))

        if self.operator == "tan":
            if self.text == "":
                self.text2 = self.ui.label.text()
                self.text2 = float(self.text2)
                self.ui.label.setText("")
                self.text2 = math.tan(math.radians(self.text2))
                self.ui.label.setText(str(self.text2))

        if self.text3 != "" and self.op2 != "":
            c = 1
            self.operator = self.op2
            self.text = self.text3
            self.text3 = ""
            self.op2 = ""

        if c == 1:
            c = 0
            self.ui.method_answer()
            self.text = self.ui.label.text()
            self.text = float(self.text)
            self.operator = ""


if __name__ == "__main__":
    app = QApplication([])
    widget = main()
    sys.exit(app.exec_())
