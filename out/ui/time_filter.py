
from PyQt5 import QtWidgets, QtGui, QtCore


class TimeFilterWidget(QtWidgets.QWidget):
    toggledButton = QtCore.pyqtSignal(str)
    buttonClicked = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        self.toggleStates = "001"
        self.toggledButton.emit("001")
        # 3 buttons
        lessThan5Years = QtWidgets.QRadioButton("5 Years")
        lessThan5Years.clicked.connect(lambda: self.years(check5=True))

        lessThan10Years = QtWidgets.QRadioButton("10 Years")
        lessThan10Years.clicked.connect(lambda: self.years(check10=True))

        anyYears = QtWidgets.QRadioButton("Any")
        anyYears.clicked.connect(lambda: self.years(checkAny=True))

        anyYears.setChecked(True)

        # H Layout
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(lessThan5Years)
        layout.addWidget(lessThan10Years)
        layout.addWidget(anyYears)
        self.setLayout(layout)

    def years(self, check5=False, check10=False, checkAny=False):
        if check5:
            self.toggledButton.emit("100")
            self.toggleStates = "100"
        if check10:
            self.toggledButton.emit("010")
            self.toggleStates = "010"
        if checkAny:
            self.toggledButton.emit("001")
            self.toggleStates = "001"
        self.buttonClicked.emit()
