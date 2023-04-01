
from PyQt5 import QtWidgets, QtGui, QtCore


genres = ['Select genre', 'Game-Show', 'Adventure', 'Reality-TV', 'Comedy', 'Fantasy', 'Sport', 'Animation', 'Mystery', 'Drama', 'Horror', 'Crime', 'Romance', 'Sci-Fi', 'Film-Noir', 'Adult', 'Biography', 'War', 'Western', 'Music', 'Thriller', 'History', 'Family', 'Action', 'Musical']



class SeachPanel(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()

        self.name_edit = QtWidgets.QLineEdit()
        self.genre_input = QtWidgets.QComboBox()
        self.shuffle_btn = QtWidgets.QPushButton('SHUFFLE')

        self.genre_input.addItems(genres)
        self.name_edit.setPlaceholderText('Search')
        self.name_edit.returnPressed.connect(self.name_filter)
        self.name_edit.returnPressed.connect(self.name_filter)
        self.shuffle_btn.clicked.connect(self.shuffle)

        search_layout = QtWidgets.QHBoxLayout()
        search_layout.addWidget(self.name_edit)
        search_layout.addWidget(self.genre_input)

        sub_layout = QtWidgets.QVBoxLayout()
        sub_layout.addWidget(self.shuffle_btn)
        sub_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(search_layout)
        main_layout.addLayout(sub_layout)

        self.setLayout(main_layout)

    def genre_filter(self, new_genre: str) -> None:
        print('[NOT IMPLEMENTED]', new_genre)

    def name_filter(self) -> None:
        name = self.name_edit.text()
        print('[NOT IMPLEMENTED]', name)

    def shuffle(self) -> None:
        print('[NOT IMPLEMENTED]', 'shuffle')


app = QtWidgets.QApplication([])

win = SeachPanel()
win.show()

app.exec()