"""Create empty files in directory"""
from pathlib import Path

def create_files(directory):
    root_dir = Path('files')

    for i in range(1,5):
        filename = f'{str(i)}.txt'
        filepath = root_dir/Path(filename)
        filepath.touch()
        print(filepath)

create_files('file')
