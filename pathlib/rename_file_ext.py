"""Change all the file extensions"""
from pathlib import Path

def change_extensions(directory):
    root_dir = Path(directory)
    
    # matches files in subdirs with the extension
    for path in root_dir.rglob('*.csv'):
        if path.is_file():
            print(path)
            # change file extension
            path.rename(path.with_suffix('.txt'))

change_extensions('files')