def validate_file(file):
    if file.size > 5 * 1024 * 1024:
        raise ValueError("File too large")
