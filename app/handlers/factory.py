from .pdf_handler import PDFHandler
from .excel_handler import ExcelHandler

class DocumentHandlerFactory:

    @staticmethod
    def get_handler(file_extension):
        if file_extension in ['.pdf']:
            return PDFHandler()
        elif file_extension in ['.xls', '.xlsx']:
            return ExcelHandler()
        else:
            return None
