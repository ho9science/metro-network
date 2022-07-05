import os


INSTALLED_PATH = os.path.dirname(os.path.realpath(__file__))

def join(path, *paths):
	return os.path.join(path, paths)

def data_path(filename):
	return os.path.join(INSTALLED_PATH, 'data', filename)
