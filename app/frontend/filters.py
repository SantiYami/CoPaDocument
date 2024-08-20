from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QCheckBox
from collections import defaultdict
from ..constants.file_extensions import PDF_EXTENSION
from ..utils.file_utils import group_by_properties

class FilterPanel(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("Filters", parent)
        layout = QVBoxLayout()

        # Agrupar extensiones por conjunto de propiedades
        self.property_groups = group_by_properties()

        # Crear checkboxes para cada grupo de propiedades
        self.checkboxes = {}
        for properties, extensions in self.property_groups.items():
            checkbox_text = f"{', '.join(properties).capitalize()} ({', '.join(extensions)})"
            checkbox = QCheckBox(checkbox_text, self)
            if PDF_EXTENSION in extensions:
                checkbox.setChecked(True)
            layout.addWidget(checkbox)
            self.checkboxes[checkbox] = properties

        self.setLayout(layout)

    def get_filters(self):
        filters = {}
        for checkbox, properties in self.checkboxes.items():
            is_checked = checkbox.isChecked()
            for prop in properties:
                filters[prop] = is_checked
        return filters
