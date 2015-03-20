import os


def iswritable(directory):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except:
            return False
    return os.access(directory, os.W_OK | os.X_OK | os.R_OK)


def static_file_path(root, filename):
    root = os.path.abspath(root) + os.sep
    return os.path.abspath(os.path.join(root, filename.strip('/\\')))


def static_file_exists(root, filename):
    root = os.path.abspath(root) + os.sep
    filename = os.path.abspath(os.path.join(root, filename.strip('/\\')))

    if not filename.startswith(root):
        return False
    if not os.path.exists(filename) or not os.path.isfile(filename):
        return False
    return True
