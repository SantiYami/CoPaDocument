from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QCheckBox

class FilterPanel(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("Filters", parent)
        layout = QVBoxLayout()

        self.pdf_pages_checkbox = QCheckBox("PDF Pages", self)
        self.pdf_pages_checkbox.setChecked(True)
        layout.addWidget(self.pdf_pages_checkbox)

        self.xls_sheets_checkbox = QCheckBox("Excel Sheets", self)
        layout.addWidget(self.xls_sheets_checkbox)

        self.csv_rows_cols_checkbox = QCheckBox("CSV Rows and Columns", self)
        layout.addWidget(self.csv_rows_cols_checkbox)

        self.image_info_checkbox = QCheckBox("Image Info (Width, Height, Channels)", self)
        layout.addWidget(self.image_info_checkbox)

        self.setLayout(layout)

    def get_filters(self):
        return {
            "pages": self.pdf_pages_checkbox.isChecked(),
            "sheets": self.xls_sheets_checkbox.isChecked(),
            "rows": self.csv_rows_cols_checkbox.isChecked(),
            "cols": self.csv_rows_cols_checkbox.isChecked(),
            "width": self.image_info_checkbox.isChecked(),
            "height": self.image_info_checkbox.isChecked(),
            "channels": self.image_info_checkbox.isChecked(),
        }
