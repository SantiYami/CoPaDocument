import os
from app.handlers.factory import DocumentHandlerFactory

def get_file_info(directory):
    document_info = []
    total_size = 0
    file_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lower()
            handler = DocumentHandlerFactory.get_handler(file_extension)

            if handler:
                info = handler.get_info(file_path)
                if info:
                    document_info.append(info)
                    total_size += os.path.getsize(file_path)
                    file_count += 1

    return document_info, total_size, file_count
