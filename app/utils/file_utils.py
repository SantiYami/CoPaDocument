import os
from collections import defaultdict
from typing import List, Dict, Tuple, Optional, Union
from ..constants.file_extensions import FILE_PROPERTIES
from ..handlers.base.document_handler_factory import DocumentHandlerFactory

def get_file_info(paths: Union[str, List[str]], filters: Optional[Dict[str, bool]] = None, factory: Optional[DocumentHandlerFactory] = None) -> Tuple[List[dict], int, int]:
    """
    Retrieves information about files, including their size and count.

    Args:
        paths (Union[str, List[str]]): A directory path or a list of file paths.
        filters (Optional[Dict[str, bool]]): Filters to apply when extracting information.
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
            info = handler.get_info(str(file_path), filters=filters)
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

def process_files_info(files_info):
    document_info, total_size, file_count = files_info
    aggregated_info = {}
    for info in document_info:
        file_type = info['extension']
        properties = FILE_PROPERTIES.get(file_type, [])
        
        key = 'directory' if not any(prop in info for prop in properties) else 'path'
        identifier = info[key]
        
        if identifier not in aggregated_info:
            aggregated_info[identifier] = {
                'directory': info['directory'],
                'type': file_type,
                'count': 0,
                'total_size': 0
            }
            aggregated_info[identifier].update({prop: info.get(prop) for prop in properties})
        
        aggregated_info[identifier]['count'] += 1
        aggregated_info[identifier]['total_size'] += info['size']

    return list(aggregated_info.values()), total_size, file_count

def group_by_properties():
    """
    Agrupa extensiones por conjunto de propiedades.

    Returns:
        dict: Diccionario de conjuntos de propiedades a extensiones.
    """
    properties_to_extensions = defaultdict(list)

    # Llenar el defaultdict usando una comprensión de lista
    _ = [properties_to_extensions[tuple(sorted(props))].append(ext) for ext, props in FILE_PROPERTIES.items()]

    return dict(properties_to_extensions)