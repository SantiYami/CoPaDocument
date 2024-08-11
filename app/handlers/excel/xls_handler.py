import xlrd
from ..base.document_handler import DocumentHandler

class XLSHandler(DocumentHandler):
    def get_info(self, file_path):
        try:
            file_info = self.extract_file_info(file_path)
            workbook = xlrd.open_workbook(file_path)
            num_sheets = len(workbook.sheets())
            
            file_info.update({
                "sheets": num_sheets
            })
            return file_info
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
