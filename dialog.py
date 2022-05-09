import convexhull
import sys

import numpy as np
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLabel


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("dialog.ui", self)

        # define widgets
        self.filesearch = self.findChild(QPushButton, "pushButton")
        self.coords = self.findChild(QLabel, "label")
        # click dropdown box
        self.filesearch.clicked.connect(self.fileclicker)
        # show app
        self.show()

    def fileclicker(self) -> str:
        fname = QFileDialog.getOpenFileName(self, "Open CSV File", "~", "CSV Files(*.csv);;TXT Files(*.txt)")
        coordinates = np.genfromtxt(fname[0], delimiter=",")
        if fname:
            self.coords.setText(str(coordinates))
        convexhull.load_data(fname[0])
        return fname[0]


app = QApplication(sys.argv)
UIWindow = UI()
app.exec()