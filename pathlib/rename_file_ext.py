"""Change all the file extensions"""
from pathlib import Path

def change_extensions(directory):
    "Find files with specific extension and change file ext"
    root_dir = Path(directory)
    # matches files in subdirs with the extension
    for path in root_dir.rglob('*.txt'):
        if path.is_file():
            # change file extension
            path.rename(path.with_suffix('.txt'))
