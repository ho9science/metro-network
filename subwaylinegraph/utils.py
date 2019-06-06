import os

installpath = os.path.dirname(os.path.realpath(__file__))

def join(path, *paths):
	return os.path.join(path, paths)
