import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Second GUI')
        self.resize(300, 160)

        self.ledText = QLineEdit('Sample Text', self)
        self.ledText.move(86, 40)

        self.btnUpdate = QPushButton('Update Window Title', self)
        self.btnUpdate.move(98, 65)
        self.btnUpdate.clicked.connect(self.evt_btn_update_clicked)

    def evt_btn_update_clicked(self):
        self.setWindowTitle(self.ledText.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
