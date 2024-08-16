import csv
import chardet
from typing import Dict, Optional
from ..base.document_handler import DocumentHandler

class CSVHandler(DocumentHandler):
    """
    Handler for CSV documents. Extracts information including the number of rows 
    and columns in the CSV file.
    """

    def get_info(self, file_path: str, filters: Dict[str, bool]) -> Optional[Dict[str, str]]:
        """
        Extracts information from a CSV file, including file details, number of rows, 
        and number of columns.

        Args:
            file_path (str): The path to the CSV file.
            filters (Dict[str, bool]): A dictionary with filters that indicate what information to extract.

        Returns:
            Optional[Dict[str, str]]: A dictionary with file information including 
            number of rows and columns, or None if an error occurs.
        """
        try:
            file_info = self.extract_file_info(file_path)

            if filters.get('rows', False) or filters.get('columns', False):
                # Detectar el encoding del archivo
                with open(file_path, 'rb') as file:
                    raw_data = file.read()
                    result = chardet.detect(raw_data)
                    encoding = result['encoding']
                
                num_rows = 0
                num_columns = 0
            
                # Leer el archivo con el encoding detectado
                with open(file_path, 'r', newline='', encoding=encoding) as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                    if filters.get('rows', False):
                        num_rows = len(rows)
                        file_info.update({"rows": num_rows})
                    if filters.get('columns', False) and rows:
                        num_columns = len(rows[0])
                        file_info.update({"columns": num_columns})
            
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
