from repository.dictionary.repo_person import *
from os.path import *
from os import curdir

class FileRepoEvent():

    def __init__(self):
        pass

    def savetofile(self):
        path = abspath(join(curdir, "..", "events.txt"))
        f = open(path, "w")
        try:
           pass
        finally:
            f.close()