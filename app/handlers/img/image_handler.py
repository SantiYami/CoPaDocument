import cv2
from typing import Dict, Optional
from ..base.document_handler import DocumentHandler

class ImageHandler(DocumentHandler):
    """
    Handler for image files. Extracts information including width, height, and 
    number of channels.
    """

    def get_info(self, file_path: str, filters: Dict[str, bool]) -> Optional[Dict[str, str]]:
        """
        Extracts information from an image file, including file details, width, height, 
        and number of channels.

        Args:
            file_path (str): The path to the image file.
            filters (Dict[str, bool]): A dictionary with filters that indicate what information to extract.

        Returns:
            Optional[Dict[str, str]]: A dictionary with file information including width, 
            height, and number of channels, or None if an error occurs.
        """
        try:
            file_info = self.extract_file_info(file_path)
            
            if any(filters.get(key, False) for key in ['width', 'height', 'channels']):
                image = cv2.imread(file_path)
                height, width, channels = image.shape

                if filters.get('width', False):
                    file_info.update({"width": width})
                if filters.get('height', False):
                    file_info.update({"height": height})
                if filters.get('channels', False):
                    file_info.update({"channels": channels})

            return file_info
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except PermissionError:
            print(f"Permission denied: {file_path}")
            return None
        except ValueError as ve:
            print(f"Value error: {ve}")
            return None
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
