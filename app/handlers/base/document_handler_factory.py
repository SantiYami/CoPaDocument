from ..pdf.pdf_handler import PDFHandler
from ..excel.xlsx_handler import XLSXHandler
from ..excel.xls_handler import XLSHandler
from ..excel.ods_handler import ODSHandler
from ..csv.csv_handler import CSVHandler

class DocumentHandlerFactory:
    def __init__(self):
        self._handlers = {}
        self._register_default_handlers()

    def _register_default_handlers(self):
        self.register_handler('.pdf', PDFHandler)
        self.register_handler('.xlsx', XLSXHandler)
        self.register_handler('.xls', XLSHandler)
        self.register_handler('.ods', ODSHandler)
        self.register_handler('.csv', CSVHandler)

    def register_handler(self, extension, handler_class):
        self._handlers[extension.lower()] = handler_class

    def get_handler(self, file_extension):
        handler_class = self._handlers.get(file_extension.lower())
        if not handler_class:
            raise ValueError(f"No handler registered for extension: {file_extension}")
        return handler_class()

    def get_supported_extensions(self):
        return list(self._handlers.keys())
