from odf.opendocument import load
from odf.table import Table
from ..base.document_handler import DocumentHandler

class ODSHandler(DocumentHandler):
    def get_info(self, file_path):
        try:
            file_info = self.extract_file_info(file_path)
            document = load(file_path)
            num_sheets = len(document.spreadsheet.getElementsByType(Table))
            
            file_info.update({
                "sheets": num_sheets
            })
            return file_info
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
