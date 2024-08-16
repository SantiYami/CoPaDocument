from odf.opendocument import load
from odf.table import Table
from typing import Dict, Optional
from ..base.document_handler import DocumentHandler

class ODSHandler(DocumentHandler):
    """
    Handler for ODS (OpenDocument Spreadsheet) files. Extracts information including 
    the number of sheets in the ODS document.
    """

    def get_info(self, file_path: str, filters: Dict[str, bool]) -> Optional[Dict[str, str]]:
        """
        Extracts information from an ODS file, including file details and the number of 
        sheets in the document.

        Args:
            file_path (str): The path to the ODS file.
            filters (Dict[str, bool]): A dictionary with filters that indicate what information to extract.

        Returns:
            Optional[Dict[str, str]]: A dictionary with file information including the 
            number of sheets, or None if an error occurs.
        """
        try:
            file_info = self.extract_file_info(file_path)
            
            if filters.get('sheets', False):
                document = load(file_path)
                num_sheets = len(document.spreadsheet.getElementsByType(Table))
                file_info.update({"sheets": num_sheets})
            
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
