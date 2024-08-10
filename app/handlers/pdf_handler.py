import os
from PyPDF2 import PdfReader
from .document_handler import DocumentHandler
from ..utils.format_utils import format_size

class PDFHandler(DocumentHandler):

    def get_info(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                reader = PdfReader(f)
                num_pages = len(reader.pages)
                size = os.path.getsize(file_path)
                return {
                    "path": file_path,
                    "pages": num_pages,
                    "size": format_size(size)
                }
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
