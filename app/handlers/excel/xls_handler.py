import xlrd
from typing import Dict, Optional
from ..base.document_handler import DocumentHandler

class XLSHandler(DocumentHandler):
    """
    Handler for XLS (Excel 97-2003) files. Extracts information including the number of 
    sheets in the XLS workbook.
    """

    def get_info(self, file_path: str, filters: Optional[Dict[str, bool]] = None) -> Optional[Dict[str, str]]:
        """
        Extracts information from an XLS file, including file details and the number of 
        sheets in the workbook.

        Args:
            file_path (str): The path to the XLS file.
            filters (Optional[Dict[str, bool]]): Optional dictionary specifying which details to extract.

        Returns:
            Optional[Dict[str, str]]: A dictionary with file information including the 
            number of sheets, or None if an error occurs.
        """
        # Set default filters if not provided
        if filters is None:
            filters = {"sheets": False}

        try:
            file_info = self.extract_file_info(file_path)
            
            if filters.get('sheets', False):
                # Abrir el libro de trabajo XLS
                workbook = xlrd.open_workbook(file_path)
                num_sheets = len(workbook.sheets())
                file_info.update({"sheets": num_sheets})

            return file_info
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except PermissionError:
            print(f"Permission denied: {file_path}")
            return None
        except xlrd.XLRDError as e:
            print(f"Error reading XLS file: {e}")
            return None
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
