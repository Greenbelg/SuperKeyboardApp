from os import walk
import pathlib
import os

f = []
for (dirpath, dirnames, filenames) in walk(pathlib.Path().resolve()):
    f.extend(filenames)
    break

for filename in f:
    if filename == "levelsChange.ui":
        os.system("pyuic5 {0}.ui -o {0}.py".format(filename.split(".")[0]))