import os
from typing import List, Tuple, Optional, Union
from ..handlers.base.document_handler_factory import DocumentHandlerFactory

def get_file_info(paths: Union[str, List[str]], factory: Optional[DocumentHandlerFactory] = None) -> Tuple[List[dict], int, int]:
    """
    Retrieves information about files, including their size and count.

    Args:
        paths (Union[str, List[str]]): A directory path or a list of file paths.
        factory (Optional[DocumentHandlerFactory]): An instance of DocumentHandlerFactory. If None, a new instance is created.

    Returns:
        Tuple[List[dict], int, int]: A tuple containing a list of file information dictionaries, total size of files, and count of files processed.
    """
    if factory is None:
        factory = DocumentHandlerFactory()

    document_info = []
    total_size = 0
    file_count = 0

    if isinstance(paths, str):
        files = _get_files_from_directory(paths)
    elif isinstance(paths, list):
        files = paths
    else:
        raise ValueError("Invalid type for paths. Expected str or list.")

    for file_path in files:
        file_extension = os.path.splitext(file_path)[1].lower()
        try:
            handler = factory.get_handler(file_extension)
            info = handler.get_info(str(file_path))
            if info:
                document_info.append(info)
                total_size += info["size"]
                file_count += 1
        except ValueError as e:
            print(f"Error: {e}")

    return document_info, total_size, file_count

def _get_files_from_directory(directory: str) -> List[str]:
    """
    Helper function to retrieve all files in a directory recursively.

    Args:
        directory (str): The directory path.

    Returns:
        List[str]: A list of file paths.
    """
    if not os.path.isdir(directory):
        raise ValueError(f"The path {directory} is not a valid directory.")
    
    return [
        os.path.join(root, file_name)
        for root, _, file_names in os.walk(directory)
        for file_name in file_names
    ]
