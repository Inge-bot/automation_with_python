"""Add date file was created to file name"""
from pathlib import Path
from datetime import datetime

def add_date_filename(directory):
    "add date and time to file names"

    root_dir = Path(directory)
    file_paths = root_dir.glob('**/*')

    for path in file_paths:
        if path.is_file():
            # create date based on timestamp (st_ctime in path stats)
            date_created = datetime.fromtimestamp(path.stat().st_ctime)
            # change into string
            date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")
            # create new file_name
            file_name = date_created_str + '_' + path.name
            # create new path object and rename
            new_filepath = path.with_name(file_name)
            path.rename(new_filepath)

add_date_filename('files')
