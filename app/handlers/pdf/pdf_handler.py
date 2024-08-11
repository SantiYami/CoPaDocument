from PyPDF2 import PdfReader
from ..base.document_handler import DocumentHandler

class PDFHandler(DocumentHandler):

    def get_info(self, file_path):
        try:
            file_info = self.extract_file_info(file_path)
            with open(file_path, 'rb') as f:
                reader = PdfReader(f)
                num_pages = len(reader.pages)
            
            file_info.update({
                "pages": num_pages
            })
            return file_info
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
