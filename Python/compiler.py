def getFileLen(dir):
	i = 0
	for l in dir:
		i += 1
	return i

path = input("Specify the location of the file you want to compile:")
print("Compiling...")
if(len(path) < 1):
	print("ERROR #0: Invalid file location. Seriosly, you can't just write nothing -.-")
elif(not(path.endswith(".pbtl"))):
	print("ERROR #1: Invalid file extension. Must be '.pbtl'.")
else:
	destination = open(path[:-4] + "py", "w")
	source = open(path, "r")
	lineNumber = 0
	for line in source:
		if(line.endswith("2")):
			destination.write("here")
		else:
			destination.write(line)
		lineNumber += 1
		print("%.2f%s" % (round((lineNumber / getFileLen(source))*100, 2), "%"))
	source.close()
	destination.close()
	print("Compilation done.")