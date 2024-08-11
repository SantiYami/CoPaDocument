import csv
import chardet
from ..base.document_handler import DocumentHandler

class CSVHandler(DocumentHandler):
    def get_info(self, file_path):
        try:
            file_info = self.extract_file_info(file_path)
            
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
                num_columns = len(next(reader, []))  # Leer el encabezado
                num_rows = sum(1 for _ in reader)    # Contar filas
            
            file_info.update({
                "rows": num_rows,
                "columns": num_columns
            })
            return file_info
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
