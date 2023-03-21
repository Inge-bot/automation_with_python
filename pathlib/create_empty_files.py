"""Create empty files in directory"""
from pathlib import Path

def create_files(directory):
    "Create files in specific directory"
    root_dir = Path(directory)

    for i in range(1,5):
        filename = f'{str(i)}.txt'
        filepath = root_dir/Path(filename)
        filepath.touch()
        print(filepath)

create_files('files')
