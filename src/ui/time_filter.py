
from PyQt5 import QtWidgets, QtGui, QtCore


class TimeFilterWidget(QtWidgets.QWidget):
    toggledButton = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.is5yrselected = False
        self.is10yrselected = False
        self.isAny = True

        # 3 buttons
        lessThan5Years = QtWidgets.QRadioButton("5 Years")
        lessThan5Years.clicked.connect(lambda: self.years5(True))

        lessThan10Years = QtWidgets.QRadioButton("10 Years")
        lessThan10Years.clicked.connect(lambda: self.years10(True))

        anyYears = QtWidgets.QRadioButton("Any")
        anyYears.clicked.connect(lambda: self.yearsAny(True))
        anyYears.setChecked(True)

        # H Layout
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(lessThan5Years)
        layout.addWidget(lessThan10Years)
        layout.addWidget(anyYears)
        self.setLayout(layout)

    def years5(self, check):
        self.is5yrselected = check
        self.is10yrselected = False
        self.isAny = False

        self.toggledButton.emit("5")

        print("5 yrs selected")

    def years10(self, check):
        self.is10yrselected = check
        self.is5yrselected = False
        self.isAny = False

        self.toggledButton.emit("10")

        print("10yrs selected")

    def yearsAny(self, check):
        self.is10yrselected = False
        self.is5yrselected = False
        self.isAny = check

        self.toggledButton.emit("any")

        print("any selected")
