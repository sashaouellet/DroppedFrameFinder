import os
from os.path import isfile
import re

def getPathFromUser():
	path = ""
	while not isPathFormat(path):
		path = raw_input("File path: ")
		if not os.path.isfile(path):
			print "File doesn't exist at the specified path"
			return getPathFromUser()
	return path

def isPathFormat(path):
	regex = '(\w+\\\\{1})+(\w+\.{1})+\w+'
	regex2 = '\/(\w+\/{1})+(\w+\.{1})+\w+'
	if re.match(regex2, path):
		return True
	else:
		return False

def getSequence(entirePath):
	directoryFileList = re.split('(\/(\w+\/{1})+)', entirePath)
	baseDirectory = directoryFileList[1]
	fileName = directoryFileList[3]
	print re.split('(\.\d+)', fileName)
	fileRootName = re.split('(\.\d+)', fileName)[0]
	sequenceNum = re.search('(\.\d+)', fileName).group(0).replace(".", "") #Finds sequence number by '.' and '#{x}' combination, strip the '.'
	directory = os.listdir(baseDirectory)
	sequence = []

	for file in directory:
		if (file.startswith(fileRootName)):
			sequence.append(file)

	print sequence
	return sequence

path = getPathFromUser()
getSequence(path)


