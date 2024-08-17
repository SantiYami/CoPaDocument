from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from .table_view import TableView
from .filters import FilterPanel
from .drag_and_drop import DragAndDropWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CoPaDocument - Document Info Viewer")
        self.setGeometry(100, 100, 800, 600)
        
        self.init_ui()

    def init_ui(self):
        # Configurar el layout principal
        main_layout = QVBoxLayout()

        # Crear y agregar los componentes principales
        self.table_view = TableView(self)
        self.filter_panel = FilterPanel(self)
        self.drag_and_drop = DragAndDropWidget(self, self.update_table, self.filter_panel)

        main_layout.addWidget(self.filter_panel)
        main_layout.addWidget(self.drag_and_drop)
        main_layout.addWidget(self.table_view)

        # Configurar el widget central
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def update_table(self, files_info):
        self.table_view.update_table(files_info)
