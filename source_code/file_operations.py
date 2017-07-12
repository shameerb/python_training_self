# Problem 2: Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.

# Problem 3: Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.

# Problem 4: Write a function to compute the number of python files (.py extension) in a specified directory recursively.

# Problem 5: Write a function to compute the total number of lines of code in all python files in the specified directory recursively.

# Problem 6: Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.

# Problem 7: Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines

import os
import sys
from glob import glob


# Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.
# Steps:
# 1. Read the list of directories
# 2. Fetch the files in each directory
# 3. Run the function on each file
# 
def fetchLines(file):
	with open(file) as f:
		yield f.readline()

def fetchFiles(directories):
	for directory in directories:
		if os.path.isfile(directory):
			yield file
		else:
			for curD, nextD, files in os.walk(directory):
				for file in glob(os.path.join(curD,"*")):
					if os.path.isfile(file):
						yield file

def runFunctionFiles(files, fnc):
	result = []
	for file in files:
		output = fnc(file)
		if output:
			result.append(output)
	return result
	

def runFunctionLines(files, fnc):
	result = []
	for file in files:
		for line in fetchLines(file):
			output = fnc(line)
			if output:
				result.append(line)
	return result


def extension(ext):
	def extensionInternal(file):
		print "file" ,file, ext
		if ext in file:
			return file
		else:
			return None
	return extensionInternal

def greaterThan40(line):
	if len(line) > 2:
		return line
	else:
		return None


def checkCount(line):
	return len(line)

def checkCodeCount(file):
	print "checkCodeCount"
	count = 0
	for line in open(file):
		print "line", line
		li = line.strip()
		print "li", li
		if not li.startswith('#'):
			count+=1
	return count

def split(n):
	def splitter(file):
		count = 0
		index = 0
		f = open(file+str(index),'w')
		for line in open(file):
			count+=1
			index+=1
			if count <= n:
				f.write(line)
			else:
				f.close()
				count = 0
				f = open(file+str(index), 'w')
				f.write(line)
	return splitter


directories = sys.argv[1:]
files = fetchFiles(directories)
result = runFunctionLines(files, greaterThan40)
print result


files2 = fetchFiles(directories)
result2 = runFunctionFiles(files2, extension('txt'))


files3 = fetchFiles(directories)
result3 = runFunctionFiles(files3, checkCodeCount)
# list(lines)
# a = runFunction(lines, checkCount)
# print a
# 
# 
# # Problem 7: Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines

files4 = fetchFiles(directories)
result4 = runFunctionFiles(files4, split(1))
print "result4", result4
