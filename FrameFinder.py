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

def getFileSequenceAsNumbers(files):
	sequence = []
	for file in files:
		sequenceNum = re.search('\.(\d+)', file).group(1)
		sequence.append(int(sequenceNum.lstrip('0'))) #Remove leading 0's and append to the list

	return sequence

def getDroppedFrameNumbers(numberSequence):
	firstFrame = min(numberSequence)
	lastFrame = max(numberSequence)

	firstConsecutive = firstFrame
	consecutiveCount = 0;
	
	output = ""

	for i in range(firstFrame, lastFrame + 1):
		if i not in numberSequence:
			if (consecutiveCount == 0): #If we haven't started a streak yet, set the start point to the current iteration
				firstConsecutive = i
				#Also append the beginning portion to our output string
				output += ", " + str(i)
			consecutiveCount += 1 #Add 1 to our streak
		else:
			if (consecutiveCount > 0):
				#End consecutive streak
				consecutiveCount = 0
				#Reset starting point to current iteration
				firstConsecutive = i
				#Append end of range to output
				output += "-" + str(i-1)

	print output[2:]


path = getPathFromUser()
getDroppedFrameNumbers(getFileSequenceAsNumbers(getSequence(path)))


