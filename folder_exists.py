# added because the script would fail to recognize a bad
# path before attempting to use it

import os

def folder_exists(path):
    if os.path.isdir(path) == False:
        return False
    if path[-1] != "/" and path[-1] != "\\":
        return False
    return True
