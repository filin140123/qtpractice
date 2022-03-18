import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Fourth GUI')
        self.resize(200, 200)

        self.btn_info = QPushButton('Open file', self)
        self.btn_info.move(20, 30)

        self.btn_info.clicked.connect(self.evt_btn_info_clicked)

    def evt_btn_info_clicked(self):
        res = QFileDialog.getOpenFileName(self, 'Open File', '/', 'PNG File (*.png);; JPG File (*.jpg)')
        print(res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
