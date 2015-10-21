import time

def getFileLen(dir):
	o = sum(1 for _ in dir)
	if(str(o).endswith("0", 0, 0)):
		return o[1:] # Don't even know why this works but it works so...
	else:
		return o

path = input("Specify the location of the file you want to compile: ")
print("Compiling...")
if(len(path) < 1):
	print("ERROR #0: Invalid file location. Seriosly, you can't just write nothing -.-")
elif(not(path.endswith(".pbtl"))):
	print("ERROR #1: Invalid file extension. Must be '.pbtl'.")
else:
	destination = open(path[:-4] + "py", "w")
	source = open(path, "r")
	fileLength = getFileLen(source)
	source.close()
	source = open(path, "r") # Yes this is necessary because of the garbage collector...
	lineNumber = 0
	charNumber = 0
	foundPrint = False
	foundWait = False
	lineLi = []
	tmpLi = []
	liValue = 0
	for line in source:
		for char in line:
			lineLi.append(char)
			if(("".join(lineLi)).endswith("print ") or foundPrint):
				if(not foundPrint):
					liValue += 1
					foundPrint = True
				else:
					tmpLi.append(char)
					if(("".join(lineLi)).endswith("; as list")):
						tmpLi = tmpLi[:-9]
						destination.write("print(\", \".join({}))".format(tmpLi))
						tmpLi = []
						foundPrint = False
					elif(("".join(lineLi)).endswith("; as nlist")):
						tmpLi = tmpLi[:-11]
						destination.write("print(\"\\n\".join({}))".format(tmpLi))
						tmpLi = []
						foundPrint = False
					elif(charNumber+1 == len(line)):
						tmpLi = tmpLi[:-1]
						destination.write("print(\"{}\")".format("".join(tmpLi)))
						tmpLi = []
						foundPrint = False
			elif(("".join(lineLi)).endswith("wait ") or foundWait):
				if(not foundWait):
					liValue += 1
					foundWait = True
				else:
					tmpLi.append(char)
					if((("".join(lineLi)).endswith(" secs")) or (("".join(lineLi)).endswith(" seconds"))):
						if(("".join(lineLi)).endswith(" secs")):
							tmpLi = tmpLi[:-5]
						else:
							tmpLi = tmpLi[:-8]
						destination.write("time.sleep({})".format("".join(tmpLi)))
						tmpLi = []
						foundWait = False
			charNumber += 1
		if(lineNumber+1 != fileLength):
			destination.write("\n")
		charNumber = 0
		lineLi = []
		lineNumber += 1
		print("%.2f%s" % (round((lineNumber / fileLength)*100, 2), "%"))
	source.close()
	destination.close()
	print("Compilation done.")