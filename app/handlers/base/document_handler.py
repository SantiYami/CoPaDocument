import os
from abc import ABC, abstractmethod
from ...utils.format_utils import format_size

class DocumentHandler(ABC):

    @abstractmethod
    def get_info(self, file_path):
        pass

    def extract_file_info(self, file_path):
        file_name = os.path.basename(file_path)
        dir_path = os.path.dirname(file_path)
        file_size = os.path.getsize(file_path)
        file_extension = os.path.splitext(file_path)[1].lower()

        return {
            "path": file_path,
            "filename": file_name,
            "directory": dir_path,
            "size": file_size,
            "extension": file_extension,
            "format_size": format_size(file_size)
        }
