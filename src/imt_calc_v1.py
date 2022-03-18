import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    m = 0
    h = 0

    def __init__(self):
        super().__init__()
        self.setWindowTitle('IMT Calculator')
        self.resize(200, 180)

        self.btn_mass = QPushButton('Mass Input', self)
        self.btn_mass.move(20, 30)
        self.btn_mass.clicked.connect(self.evt_btn_mass_clicked)

        self.btn_height = QPushButton('Height Input', self)
        self.btn_height.move(20, 60)
        self.btn_height.clicked.connect(self.evt_btn_height_clicked)

        self.btn_imt = QPushButton('Show IMT', self)
        self.btn_imt.move(20, 90)
        self.btn_imt.clicked.connect(self.get_imt)

        self.lbl = QLabel('', self)
        self.lbl.move(110, 20)
        pxm = QPixmap('pics/man.jpg').scaled(70, 106)
        self.lbl.setPixmap(pxm)

    def evt_btn_mass_clicked(self):
        user_mass, btn_is_ok = QInputDialog.getInt(self, 'Mass', 'Enter your mass:', 10, 65, 500, 1)
        if btn_is_ok:
            self.m = user_mass
        else:
            QMessageBox.critical(self, 'Canceled', 'Operation cancelled')

    def evt_btn_height_clicked(self):
        user_height, btn_is_ok = QInputDialog.getDouble(self, 'Height', 'Enter your height:', 1.70, .50, 2.50, 2)
        if btn_is_ok:
            self.h = user_height
        else:
            QMessageBox.critical(self, 'Canceled', 'Operation cancelled')

    def get_imt(self):
        imt = round(self.m / (self.h**2), 2)

        if imt <= 16:
            addmsg = 'Выраженный дефицит массы тела'
        elif imt <= 18.5:
            addmsg = 'Недостаточная масса тела (дефицит)'
        elif imt <= 25:
            addmsg = 'Норма'
        elif imt <= 30:
            addmsg = 'Избыточная масса тела'
        elif imt <= 35:
            addmsg = 'Ожирение 1-й степени'
        elif imt <= 40:
            addmsg = 'Ожирение 2-й степени'
        else:
            addmsg = 'Ожирение 3-й степени'

        msg = f'Your IMT is {imt}\n{addmsg}'
        QMessageBox.information(self, 'IMT', msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
