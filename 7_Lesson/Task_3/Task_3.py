from os import walk
from os.path import join
from shutil import copytree

path = join(".", "some_dir", "my_project")
my_path = join(".", "my_project")

for name, dirs, files in walk(path):
    for temp in dirs:
        if dirs[0] == 'templates':
            copytree(join(name, 'templates'), join(my_path, 'templates'), dirs_exist_ok=True)
