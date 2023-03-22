"""
Search for file using a searchterm in directories/sub-directories 
and get absolute path
"""
from pathlib import Path

def find_file(search_term, directory):
    "search for file in directories and print absolute path"
    root_dir = Path(directory)

    # solution one
    for path in root_dir.rglob(f'{search_term}*'):
        if path.is_file():
            absolute_path = path.absolute()
            print(absolute_path)

    # solution two
    for path in root_dir.rglob('*'):
        if search_term in path.stem:
            print(path.absolute())
