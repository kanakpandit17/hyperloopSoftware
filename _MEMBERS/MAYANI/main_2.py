class TstWidget(QtGui.QWidget):
    def __init__(self):
        super(type(self), self).__init__()

        self.bar = QRoundProgressBar()
        self.bar.setFixedSize(300, 300)

        self.bar.setDataPenWidth(3)
        self.bar.setOutlinePenWidth(3)
        self.bar.setDonutThicknessRatio(0.85)
        self.bar.setDecimals(1)
        self.bar.setFormat('%v | %p %')
        # self.bar.resetFormat()
        self.bar.setNullPosition(90)
        self.bar.setBarStyle(QRoundProgressBar.StyleDonut)
        self.bar.setDataColors([(0., QtGui.QColor.fromRgb(255,0,0)), (0.5, QtGui.QColor.fromRgb(255,255,0)), (1., QtGui.QColor.fromRgb(0,255,0))])

        self.bar.setRange(0, 300)
        self.bar.setValue(260)

        lay = QtGui.QVBoxLayout()
        lay.addWidget(self.bar)
        self.setLayout(lay)