from PyQt5 import QtCore, QtGui, QtWidgets
import time
from firstversion import *

class mainProgram(Ui_MainWindow):
    def __init__(self, parent=None):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        self.start_b.clicked.connect(self.start)
        self.stop_b.clicked.connect(self.stop)
        self.estop_b.clicked.connect(self.estop)

    def start(self):
        self.state_t.setText("ACTIVE")
        self.state_t.setAlignment(QtCore.Qt.AlignCenter)

    def stop(self):
        self.state_t.setText("STOPPING")
        self.state_t.setAlignment(QtCore.Qt.AlignCenter)
        time.sleep(2)
        self.state_t.setText("GROUND")
        self.state_t.setAlignment(QtCore.Qt.AlignCenter)

    def estop(self):
        self.state_t.setText("GROUND")
        self.state_t.setAlignment(QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    m1= mainProgram()
    MainWindow.show()
    sys.exit(app.exec_())