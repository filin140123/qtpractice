import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Fourth GUI')
        self.resize(200, 300)

        self.btn_color = QPushButton('Choose Color', self)
        self.btn_color.setIcon(QIcon(QPixmap('pics/pallete.png')))
        self.btn_color.move(20, 30)
        self.btn_color.clicked.connect(self.evt_btn_color_clicked)

        self.lbl_msg = 'Result: '
        self.lbl_rslt = QLabel(self.lbl_msg, self)
        self.lbl_rslt.move(20, 60)

        self.btn_font = QPushButton('Choose Font', self)
        self.btn_font.setIcon(QIcon(QPixmap('pics/fonts.png')))
        self.btn_font.move(20, 100)
        self.btn_font.clicked.connect(self.evt_btn_font_clicked)

        font = QFont('Arial', 10, 81, True)
        self.btn_color.setFont(font)
        self.btn_font.setFont(font)
        self.lbl_rslt.setFont(font)

    def evt_btn_color_clicked(self):
        color = QColorDialog.getColor(QColor('#ffffff'), self, 'Choose Color')
        hex_ = color.name()
        rgb_ = f'{color.red()}, {color.blue()}, {color.green()}'
        msg = f'Hex: {hex_}\nRGB: {rgb_}'
        self.lbl_rslt.resize(120, 30)
        self.lbl_rslt.setText(msg)

    def evt_btn_font_clicked(self):
        font, btn_is_ok = QFontDialog.getFont()
        if btn_is_ok:
            self.btn_font.setFont(font)
            self.btn_color.setFont(font)
            self.lbl_rslt.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
