from numpy.lib.scimath import logn

def format_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_units = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    i = int(logn(1024, size_bytes))
    p = 1024**i
    return f"{size_bytes / p:.2f} {size_units[i]}"
