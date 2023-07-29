import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        try:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename): #recursion
                search(full_filename)
            else: #base case
                ext = os.path.splitext(full_filename)[-1]
            if ext == ".py" or ".txt":
                print(full_filename)
        except PermissionError:
            pass

search(os.getcwd())

