import os

def tryExcept(success, failure, *exceptions):
    try:
        return success()
    except exceptions: 
        return failure() if callable(failure) else failure 

def ensureDir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return file_path