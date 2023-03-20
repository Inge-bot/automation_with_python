"""Add prefix to all filenames in folder"""
from pathlib import Path

def add_prefix(file):
    "Add prefix to files"
    # specify route directory as Path object
    root_dir = Path(file)
    file_paths = root_dir.iterdir()

    for path in file_paths:
        # rename files
        new_filename = 'v2_' + path.stem + path.suffix
        new_filepath = path.with_name(new_filename)
        # use existing file path and change file name
        path.rename(new_filepath)

    return file_paths

print(add_prefix('files'))
