from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from ..utils.format_utils import format_size

class TableView(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(0, 3, parent)
        self.setHorizontalHeaderLabels(["Path", "Pages", "Size"])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.horizontalHeader().setStretchLastSection(True)

    def update_table(self, files_info):
        document_info, total_size, file_count = files_info

        self.setRowCount(0)  # Limpiar la tabla

        for info in document_info:
            if info['count'] > 1:
                # Mostrar un resumen del directorio
                row_position = self.rowCount()
                self.insertRow(row_position)
                self.setItem(row_position, 0, QTableWidgetItem(info['directory']))
                self.setItem(row_position, 1, QTableWidgetItem(f"{info['count']} files"))
                self.setItem(row_position, 2, QTableWidgetItem(format_size(info['total_size'])))
            else:
                # Mostrar detalles de cada archivo en el directorio
                for file_info in info['files']:
                    row_position = self.rowCount()
                    self.insertRow(row_position)
                    self.setItem(row_position, 0, QTableWidgetItem(file_info['path']))
                    # Mostrar solo las propiedades relevantes
                    pages = file_info.get('pages', '-')
                    size = file_info['size']  # Ahora usamos el tamaño del archivo individual
                    self.setItem(row_position, 1, QTableWidgetItem(str(pages)))
                    self.setItem(row_position, 2, QTableWidgetItem(format_size(size)))

        # Mostrar totales
        row_position = self.rowCount()
        self.insertRow(row_position)
        self.setItem(row_position, 0, QTableWidgetItem("Total"))
        self.setItem(row_position, 1, QTableWidgetItem(str(file_count)))
        self.setItem(row_position, 2, QTableWidgetItem(f"{format_size(total_size)}"))

        # Ajustar tamaño de las columnas
        self.resizeColumnsToContents()

