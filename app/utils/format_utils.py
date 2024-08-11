from numpy import log2, floor

LOG2_1024 = 10

def format_size(size_bytes: int) -> str:
    """
    Formats the size in bytes into a human-readable string with appropriate units.

    Args:
        size_bytes (int): The size in bytes to format.

    Returns:
        str: A formatted string representing the size in human-readable units.
    """
    if size_bytes < 0:
        raise ValueError("Size cannot be negative.")
    if size_bytes == 0:
        return "0B"
    
    size_units = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    
    # Calculate the index of the size unit
    i = int(floor(log2(size_bytes) / LOG2_1024))
    p = 1024**i
    
    # Calculate the size and unit
    return f"{size_bytes / p:.2f} {size_units[i]}"
