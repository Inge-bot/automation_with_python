"""Delete files"""
from pathlib import Path

def delete_files(directory):
    "write empty bytes to directory and delete"
    root_dir = Path(directory)

    for path in root_dir.glob("*.txt"):
        if path.is_file():
        # write bytes to file
            with open(path, 'wb') as file:
                file.write(b'')
            path.unlink()
