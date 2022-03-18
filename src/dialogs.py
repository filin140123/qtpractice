import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Third GUI')
        self.resize(200, 200)

        self.btn_info = QPushButton('Show Info Message', self)
        self.btn_info.move(20, 30)

        self.btn_warn = QPushButton('Show Warning Message', self)
        self.btn_warn.move(20, 70)

        self.btn_q = QPushButton('Show Question Message', self)
        self.btn_q.move(20, 110)

        self.btn_info.clicked.connect(self.evt_btn_info_clicked)
        self.btn_warn.clicked.connect(self.evt_btn_warn_clicked)
        self.btn_q.clicked.connect(self.evt_btn_q_clicked)

    def evt_btn_info_clicked(self):
        result = QMessageBox.information(self, 'msg', 'Hi there')
        print(result)

    def evt_btn_warn_clicked(self):
        result = QMessageBox.warning(self, 'msg', 'Hi there')
        print(result)

    def evt_btn_q_clicked(self):
        result = QMessageBox.question(self, 'msg', 'Hi there')
        if result == QMessageBox.Yes:
            QMessageBox.information(self, '', '"Yes" button clicked')
        elif result == QMessageBox.No:
            QMessageBox.information(self, '', '"No" Button clicked')
        print(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
