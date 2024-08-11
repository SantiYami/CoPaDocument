import os
from app.handlers.base.document_handler_factory import DocumentHandlerFactory

def get_file_info(paths, factory=None):
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
            info = handler.get_info(file_path)
            if info:
                document_info.append(info)
                total_size += info["size"]
                file_count += 1
        except ValueError as e:
            print(f"Error: {e}")

    return document_info, total_size, file_count

def _get_files_from_directory(directory):
    """Helper function to retrieve all files in a directory recursively."""
    files = []
    for root, dirs, file_names in os.walk(directory):
        for file_name in file_names:
            files.append(os.path.join(root, file_name))
    return files