"""Archive files into a zip file"""
from pathlib import Path
import zipfile

def archive_files(directory):
    "zip files and delete the original file objects"
    root_dir = Path(directory)
    archive_path = root_dir/Path('archive.zip')

    # use Zipfile class from zipfile library to write file
    with zipfile.ZipFile(archive_path, 'w') as zf:
        # rewrite all directory filenames
        for path in root_dir.rglob("*.txt"):
            # write zipfile
            zf.write(path)
            # delete original files
            path.unlink()

# archive_files('files/2022')