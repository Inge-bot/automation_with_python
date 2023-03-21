"""Rename files in sub sub directories"""
from pathlib import Path

def rename_files_subdirectory(directory):
    "Iterate throught sub folders and rename files"
    root_dir = Path(directory)
    file_paths = root_dir.glob('**/*')

    # walk operation through the directories
    for path in file_paths:
        if path.is_file():

            # find all subfolders in root dir
            subfolders = path.parts[1:-1]

            # create new filename
            new_filename = '_'.join(subfolders) + '_' + path.name

            # create new path object and rename
            new_filepath = path.with_name(new_filename)
            path.rename(new_filepath)

rename_files_subdirectory('files')
