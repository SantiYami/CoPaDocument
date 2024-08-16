from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from ..utils.file_utils import get_file_info

class DragAndDropWidget(QLabel):
    def __init__(self, parent, drop_callback):
        super().__init__(parent)
        self.setText("Drag and Drop Folder or File Here")
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color: lightgray;")
        self.drop_callback = drop_callback
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            path = urls[0].toLocalFile()
            files_info = get_file_info(path)
            self.drop_callback(files_info)
