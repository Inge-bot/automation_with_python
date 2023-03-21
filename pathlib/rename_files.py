"""Rename files based on directory"""
from pathlib import Path
def rename_files(directory):
    "add directory name as prefix to filenames"
    root_dir = Path(directory)

    # glob matches pathname pattern
    file_paths = root_dir.glob('**/*')

    # Iterate through the root dir
    for path in file_paths:
        # only return files
        if path.is_file():
            # break up the pathname into parts
            parent_folder = path.parts[-2]
            # create new filename
            new_filename = f'{parent_folder}_{path.name}'
            # create new path object and rename
            new_filepath = path.with_name(new_filename)
            path.rename(new_filepath)
