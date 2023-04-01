
from PyQt5 import QtWidgets, QtGui, QtCore
from ui.overview_ui import MovieOverviewWidget, Movie


app = QtWidgets.QApplication([])

item = Movie(
    'Top Gun: Maverick',
    "After more than thirty years of service as one of the Navy's top aviators, Pete Mitchell is where he belongs, pushing the envelope as a courageous test pilot and dodging the advancement in rank that would ground",
    '8.6',
    '/title/tt98492',
    ['action', 'suspense', 'more-shit', 'rom'],
    'Mr Director',
    ['NAME-1', 'name-2', 'name-3'],
    '2014'
)

win = MovieOverviewWidget(item)
win.show()

app.exec()
