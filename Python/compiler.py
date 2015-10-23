import math

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
	with open(path) as f:
		fileLi = f.read()
		fileLi = fileLi.splitlines()
	print("[DEBUG] {}".format(fileLi))
	lineNo = 0
	charNo = 0
	lineLi = []
	tmpLi = []
	fileLength = getFileLen(open(path, "r"))
	dest = open(path[:-4] + "py", "w")
	foundPrint = False
	foundWait = False
	for line in fileLi:
		for char in line:
			lineLi.append(char)
			if(("".join(lineLi)).endswith("print ") or foundPrint):
				if(not foundPrint):
					foundPrint = True
				else:
					tmpLi.append(char)
					if(("".join(lineLi)).endswith("; as bubbletopsnow")):
						tmpLi = tmpLi[:-18]
						dest.write("print(\"PRINT WHATEVERTHEFUDGINGTHINGYOUWANT\")\nprint(\"{}\")".format("".join(tmpLi)))
						tmpLi = []
						foundPrint = False
					elif(("".join(lineLi)).endswith("; as list")):
						tmpLi = tmpLi[:-9]
						dest.write("print(\", \".join({}))".format(tmpLi))
						tmpLi = []
						foundPrint = False
					elif(("".join(lineLi)).endswith("; as nlist")):
						tmpLi = tmpLi[:-10]
						dest.write("print(\"\\n\".join({}))".format(tmpLi))
						tmpLi = []
						foundPrint = False
					elif(("".join(lineLi)).endswith("; as TropicSapling")):
						tmpLi = tmpLi[:-18]
						dest.write("print(\"WUT how did you know my username O_O\")\nprint(\"{}\")".format("".join(tmpLi)))
						tmpLi = []
						foundPrint = False
					elif(("".join(lineLi)).endswith("; as an-OK-squirrel")):
						tmpLi = tmpLi[:-19]
						dest.write("print(\"So, what is this?\")\nprint(\"{}\")".format("".join(tmpLi)))
						tmpLi = []
						foundPrint = False
					elif(("".join(lineLi)).endswith("; as Zaidhaan")):
						tmpLi = tmpLi[:-13]
						dest.write("print(\"O hello!\")\nprint(\"{}\")".format("".join(tmpLi)))
						tmpLi = []
						foundPrint = False
					elif(("".join(lineLi)).endswith("; as ev3commander")):
						tmpLi = tmpLi[:-17]
						dest.write("print(\"Markdown is pretty cool\")\nprint(\"{}\")".format("".join(tmpLi)))
						tmpLi = []
						foundPrint = False
					elif(charNo+1 == len(line)):
						dest.write("print(\"{}\")".format("".join(tmpLi)))
						tmpLi = []
						foundPrint = False
			elif(("".join(lineLi)).endswith("wait ") or foundWait):
				if(not foundWait):
					foundWait = True
				else:
					if(char.isdigit()):
						tmpLi.append(char)
					else:
						print("[ERROR] {} is not a digit, ignoring.".format(char))
					if(charNo+1 == len(line)):
						dest.write("# Coming soon!")
						tmpLi = []
						foundWait = False
			charNo += 1
		if(lineNo+1 != fileLength):
			dest.write("\n")
		charNo = 0
		lineNo += 1
		print("%.2f%s" % (round((lineNo / fileLength)*100, 2), "%"))
	print("Compilation done.")