import os

dirs = ["my_project", "settings", "mainapp", "adminapp", "authapp", "authapp"]

i = 1

for iter in range(len(dirs) - 1):
    new_tree = os.path.join(dirs[0], dirs[i])
    if not os.path.exists(new_tree):
        os.makedirs(new_tree)
    i += 1