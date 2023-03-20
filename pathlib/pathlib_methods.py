from pathlib import Path

# if not using pathlib - file name is in string format
p1 = 'files/abc.txt'

# using pathlib
p2 = Path('files/abc.txt')

p3 = Path('files/ghi.txt')

if p2.exists():
# read file
    with open(p2, 'r') as file:
        file.read()

if not p3.exists():
    with open(p3, 'w') as file:
        file.write('Content 3')

# pathlib methods
filename = p2.name
file_stem = p2.stem
file_suffix = p2.suffix

# iterate over files in directory
p4 = Path('files')
dir_files = p4.iterdir()

# make list of files in dir
list_p4 = list(dir_files)

# iterate over files in directory
for item in p4.iterdir():
    print(item)
