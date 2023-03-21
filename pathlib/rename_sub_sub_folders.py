"""Rename files in sub sub directories"""
from pathlib import Path

def rename_files_subdirectory(directory):
    root_dir = Path(directory)
    file_paths = root_dir.glob('**/*')

    for path in file_paths:
        if path.is_file():
            # create new filename
            new_filename = f"{path.parts[-3]}_{path.parts[-2]}_{path.name}"
            # create new path object and rename
            new_filepath = path.with_name(new_filename)
            path.rename(new_filepath)

rename_files_subdirectory('files')
