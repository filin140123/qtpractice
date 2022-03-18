import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Third GUI')
        self.resize(200, 200)

        self.btn_name = QPushButton('Name Input', self)
        self.btn_name.move(20, 30)
        self.btn_name.clicked.connect(self.evt_btn_name_clicked)

        self.btn_age = QPushButton('Age Input', self)
        self.btn_age.move(20, 60)
        self.btn_age.clicked.connect(self.evt_btn_age_clicked)

        self.btn_height = QPushButton('Height Input', self)
        self.btn_height.move(20, 90)
        self.btn_height.clicked.connect(self.evt_btn_height_clicked)

        self.btn_color = QPushButton('Color Input', self)
        self.btn_color.move(20, 120)
        self.btn_color.clicked.connect(self.evt_btn_color_clicked)

    def evt_btn_name_clicked(self):
        user_name, btn_is_ok = QInputDialog.getText(self, 'Name', 'Enter your name:')
        if btn_is_ok:
            QMessageBox.information(self, 'Name', f'Your name is {user_name}')
        else:
            QMessageBox.critical(self, 'Canceled', 'Operation cancelled')

    def evt_btn_age_clicked(self):
        user_age, btn_is_ok = QInputDialog.getInt(self, 'Age', 'Enter your age:', 18, 18, 65, 1)
        if btn_is_ok:
            QMessageBox.information(self, 'Age', f'Your age is {user_age}')
        else:
            QMessageBox.critical(self, 'Canceled', 'Operation cancelled')

    def evt_btn_height_clicked(self):
        user_height, btn_is_ok = QInputDialog.getDouble(self, 'Height', 'Enter your height:', 1.70, .50, 2.50, 2)
        if btn_is_ok:
            QMessageBox.information(self, 'Height', f'Your height is {user_height}')
        else:
            QMessageBox.critical(self, 'Canceled', 'Operation cancelled')

    def evt_btn_color_clicked(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        user_color, btn_is_ok = QInputDialog.getItem(self, 'Color', 'Choose your color:', colors)
        if btn_is_ok:
            QMessageBox.information(self, 'Color', f'Your favorite color is {user_color}')
        else:
            QMessageBox.critical(self, 'Canceled', 'Operation cancelled')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
