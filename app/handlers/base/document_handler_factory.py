from ..pdf.pdf_handler import PDFHandler
from ..excel.xlsx_handler import XLSXHandler
from ..excel.xls_handler import XLSHandler
from ..excel.ods_handler import ODSHandler
from ..csv.csv_handler import CSVHandler
from ..img.image_handler import ImageHandler

from typing import Type, Dict, List
from ...constants.file_extensions import PDF_EXTENSION, XLSX_EXTENSION, XLS_EXTENSION, ODS_EXTENSION, CSV_EXTENSION, IMAGE_EXTENSIONS


class HandlerNotFoundError(ValueError):
    """Exception raised when no handler is found for a file extension."""
    pass

class DocumentHandlerFactory:
    """
    Factory class to create and manage document handlers based on file extensions.
    """
    def __init__(self):
        """
        Initializes the factory and registers default handlers.
        """
        self._handlers: Dict[str, Type] = {}
        self._register_default_handlers()

    def _register_default_handlers(self):
        """
        Registers default handlers for common document types.
        """
        self._register_handlers({
            PDF_EXTENSION: PDFHandler,
            XLSX_EXTENSION: XLSXHandler,
            XLS_EXTENSION: XLSHandler,
            ODS_EXTENSION: ODSHandler,
            CSV_EXTENSION: CSVHandler
        })
        
        # Register multiple extensions for images
        self._register_extensions(IMAGE_EXTENSIONS, ImageHandler)

    def _register_extensions(self, extensions: List[str], handler_class: Type):
        """
        Registers handlers for multiple file extensions at once using a single handler class.
        
        Args:
            extensions (List[str]): A list of file extensions to register.
            handler_class (Type): The handler class to register for the provided extensions.
        """
        self._register_handlers({ext: handler_class for ext in extensions})

    def _register_handlers(self, handlers_dict: Dict[str, Type]):
        """
        Registers multiple handlers at once.
        
        Args:
            handlers_dict (Dict[str, Type]): A dictionary mapping file extensions to handler classes.
        """
        self._handlers.update(handlers_dict)

    def register_handler(self, extension: str, handler_class: Type):
        """
        Registers a single handler for a specific file extension.
        
        Args:
            extension (str): The file extension to associate with the handler.
            handler_class (Type): The class of the handler to register.
        """
        self._handlers[extension.lower()] = handler_class

    def get_handler(self, file_extension: str) -> Type:
        """
        Retrieves the handler class for a given file extension.
        
        Args:
            file_extension (str): The file extension to retrieve the handler for.
        
        Returns:
            Type: The handler class associated with the file extension.
        
        Raises:
            HandlerNotFoundError: If no handler is registered for the given file extension.
        """
        handler_class = self._handlers.get(file_extension.lower())
        if not handler_class:
            raise HandlerNotFoundError(f"No handler registered for extension: {file_extension}")
        return handler_class()

    def get_supported_extensions(self) -> List[str]:
        """
        Retrieves a list of all supported file extensions.
        
        Returns:
            List[str]: A list of supported file extensions.
        """
        return list(self._handlers.keys())
