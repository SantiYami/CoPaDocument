from PySide6.QtWidgets import QApplication
import sys
from .frontend.main_window import MainWindow

def run_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
