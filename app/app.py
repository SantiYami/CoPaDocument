import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QWidget, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFileDialog
from .utils.file_utils import get_file_info
from .utils.format_utils import format_size

class CoPaDocumentApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CoPaDocument - Document Info Viewer")
        self.setGeometry(100, 100, 800, 400)

        # Crear el widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QVBoxLayout(central_widget)

        # Label para Drag and Drop
        self.drop_label = QLabel("Drag and Drop Folder or File Here", self)
        self.drop_label.setStyleSheet("background-color: lightgray; padding: 10px;")
        layout.addWidget(self.drop_label)

        # Tabla
        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        # Configuración de la tabla
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Path", "Pages", "Size"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.setShowGrid(True)
        self.table.setStyleSheet("QTableWidget::item:selected { background-color: lightblue; }")

        # Habilitar drag and drop
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            directory = urls[0].toLocalFile()
            files_info = get_file_info(directory)
            self.update_table(files_info)

    def update_table(self, files_info):
        document_info, total_size, file_count = files_info

        self.table.setRowCount(0)  # Clear the table

        for info in document_info:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(info["path"]))
            self.table.setItem(row_position, 1, QTableWidgetItem(str(info.get("pages", "-"))))
            self.table.setItem(row_position, 2, QTableWidgetItem(info["format_size"]))

        # Display totals
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem("Total"))
        self.table.setItem(row_position, 1, QTableWidgetItem(str(file_count)))
        self.table.setItem(row_position, 2, QTableWidgetItem(f"{format_size(total_size)}"))

def run_app():
    app = QApplication(sys.argv)
    ex = CoPaDocumentApp()
    ex.show()
    sys.exit(app.exec_())
