from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from ..utils.file_utils import get_file_info

class DragAndDropWidget(QLabel):
    def __init__(self, parent, drop_callback, filter_panel):
        super().__init__(parent)
        self.setText("Drag and Drop Folder or File Here")
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("padding: 8px 0 8px 0;")
        self.drop_callback = drop_callback
        self.filter_panel = filter_panel
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            path = urls[0].toLocalFile()
            filters = self.filter_panel.get_filters()
            files_info = get_file_info(path, filters=filters)
            self.drop_callback(files_info)
