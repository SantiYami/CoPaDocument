from PyPDF2 import PdfReader
from typing import Dict, Optional
from ..base.document_handler import DocumentHandler

class PDFHandler(DocumentHandler):
    """
    Handler for PDF documents. Extracts information including the number of pages.
    """

    def get_info(self, file_path: str) -> Optional[Dict[str, str]]:
        """
        Extracts information from a PDF file, including file details and number of pages.

        Args:
            file_path (str): The path to the PDF file.

        Returns:
            Optional[Dict[str, str]]: A dictionary with file information including the number of pages,
            or None if an error occurs.
        """
        try:
            file_info = self.extract_file_info(file_path)
            
            with open(file_path, 'rb') as f:
                reader = PdfReader(f)
                num_pages = len(reader.pages)
            
            file_info.update({
                "pages": num_pages
            })
            return file_info
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except PermissionError:
            print(f"Permission denied: {file_path}")
            return None
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
