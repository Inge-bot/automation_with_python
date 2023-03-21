"Extract files archive in zip folder"
from pathlib import Path
import zipfile

def extract_files(directory):
    "extract files from zip file to specified path"
    root_dir = Path(directory)

    # check for zip file one level deep in directory (use rglob for more levels)
    for path in root_dir.glob('*.zip'):
        # read zip file and create path name for extracted files
        with zipfile.ZipFile(path, 'r') as zf:
            final_path = root_dir/ Path(path.stem)
            zf.extractall(path=final_path)
