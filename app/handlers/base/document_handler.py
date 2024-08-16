import os
from typing import Dict, Optional
from abc import ABC, abstractmethod
from ...utils.format_utils import format_size

class DocumentHandler(ABC):
    """
    Abstract base class for handling documents. Defines common functionality 
    for extracting file information.
    """

    @abstractmethod
    def get_info(self, file_path: str, filters: Dict[str, bool]) -> Optional[Dict[str, str]]:
        """
        Abstract method to be implemented by subclasses for extracting 
        specific information from the document.

        Args:
            file_path (str): The path to the document.
            filters (Dict[str, bool]): A dictionary with filters that indicate what information to extract.

        Returns:
            Dict[str, str]: A dictionary containing document-specific information.
        """
        pass

    def extract_file_info(self, file_path: str) -> Dict[str, str]:
        """
        Extracts basic information about a file, including its path, name, 
        directory, size, and extension.

        Args:
            file_path (str): The path to the file.

        Returns:
            Dict[str, str]: A dictionary with file information.
        """
        try:
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
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} was not found.")
        except OSError as e:
            raise RuntimeError(f"Error accessing file {file_path}: {e}")
