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
	fileNameParts = fileName.split(".")
	fileRootName = fileNameParts[0]
	sequenceNum = re.search('\.(\d+)', fileName).group(1) #Finds sequence number by '.' and '#{x}' combination
	directory = os.listdir(baseDirectory)
	sequence = []
	compareRegex = buildSequenceMatchRegex(fileNameParts, sequenceNum)

	for file in directory:
		if (re.match(compareRegex, file)):
			sequence.append(file)

	print sequence
	return sequence

#Builds regex based on the individual filename components. Substitutes wildcards for frame numbers so that we can match the entire rest of the file
def buildSequenceMatchRegex(fileNameList, sequenceNum):
	regex = ''
	for part in fileNameList:
		if part != sequenceNum:
			regex += part + '\.'
		else:
			regex += '.' * len(sequenceNum) + '\.'
	regex = regex[:-2]
	return regex


path = getPathFromUser()
getSequence(path)


