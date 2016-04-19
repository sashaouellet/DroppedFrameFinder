import os
import re

def getPathFromUser():
	path = ""
	while not isPathFormat(path):
		path = raw_input("File path: ")
	return path

def isPathFormat(path):
	if re.match('(\w+\\\\{1})+\w+\.{1}\w+', path):
		return True
	else:
		return False

path = getPathFromUser()
#file = os.open(path)
