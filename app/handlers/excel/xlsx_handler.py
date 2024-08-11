from openpyxl import load_workbook
from ..base.document_handler import DocumentHandler

class XLSXHandler(DocumentHandler):
    def get_info(self, file_path):
        try:
            file_info = self.extract_file_info(file_path)
            workbook = load_workbook(file_path, read_only=True)
            num_sheets = len(workbook.sheetnames)
            
            file_info.update({
                "sheets": num_sheets
            })
            return file_info
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
