import sys
from PyQt5.QtWidgets import QApplication

from widget.main_widget import MainWin_Ui

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = MainWin_Ui()
    ui.show()

    sys.exit(app.exec_())
