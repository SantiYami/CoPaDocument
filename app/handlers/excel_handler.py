import os
from .document_handler import DocumentHandler
from ..utils.format_utils import format_size

class ExcelHandler(DocumentHandler):

    def get_info(self, file_path):
        try:
            size = os.path.getsize(file_path)
            return {
                "path": file_path,
                "size": format_size(size)
            }
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
