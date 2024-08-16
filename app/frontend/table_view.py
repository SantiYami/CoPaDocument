from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from ..utils.format_utils import format_size

class TableView(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(0, 3, parent)
        self.setHorizontalHeaderLabels(["Path", "Pages", "Size"])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.horizontalHeader().setStretchLastSection(True)

    def update_table(self, files_info):
        document_info, total_size, file_count = files_info

        self.setRowCount(0)  # Clear the table

        for info in document_info:
            row_position = self.rowCount()
            self.insertRow(row_position)
            self.setItem(row_position, 0, QTableWidgetItem(info["path"]))
            self.setItem(row_position, 1, QTableWidgetItem(str(info.get("pages", "-"))))
            self.setItem(row_position, 2, QTableWidgetItem(info["format_size"]))

        # Display totals
        row_position = self.rowCount()
        self.insertRow(row_position)
        self.setItem(row_position, 0, QTableWidgetItem("Total"))
        self.setItem(row_position, 1, QTableWidgetItem(str(file_count)))
        self.setItem(row_position, 2, QTableWidgetItem(f"{format_size(total_size)}"))

        # Ajustar tamaño de las columnas
        self.resizeColumnsToContents()
