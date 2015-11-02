import math
import time

def getFileLen(dir):
	o = sum(1 for _ in dir)
	if(str(o).endswith("0", 0, 0)):
		return o[1:] # Don't even know why this works but it works so...
	else:
		return o

path = input("Specify the location of the file you want to compile: ")
useDebug = input("Print debug messages? (Yes / No)\n").upper()
print("Preparing...")
if(len(path) < 1):
	print("ERROR #0: Invalid file location. Seriosly, you can't just write nothing -.-")
elif(not(path.endswith(".pbtl"))):
	print("ERROR #1: Invalid file extension. Must be '.pbtl'.")
else:
	with open(path) as f:
		fileLi = f.read()
		fileLi = fileLi.splitlines()
	if(useDebug == "YES"):
		print("[DEBUG]: {}".format(fileLi))
	lineNo = 0
	charNo = 0
	lineLi = []
	tmpLi = []
	fileLength = getFileLen(open(path, "r"))
	dest = open(path[:-4] + "py", "w")
	foundPrint = False
	foundWait = False
	foundComment = False
	foundIgnore = False
	errorType2 = 0
	
	# Prepare
	for line in fileLi:
		for char in line:
			lineLi.append(char)
			if((("".join(lineLi)).endswith("wait ")) and (not foundWait)):
				dest.write("import time\n")
				if(useDebug == "YES"):
					print("[DEBUG]: Found need of import.")
				foundWait = True
		lineLi = []
		lineNo += 1
		print("%.2f%s" % (round((lineNo / fileLength)*100, 2), "%"), end = "\r")
	lineNo = 0
	lineLi = []
	foundWait = False
	print("Preparations done.")
	print("Compiling...")
	
	# Write main stuff
	for line in fileLi:
		for char in line:
			lineLi.append(char)
			if(foundComment):
				if(("".join(lineLi)).endswith("\"")):
					foundComment = False
					print("[DEBUG]: Found end of comment.")
					break
				else:
					break
			elif(foundIgnore):
				foundIgnore = False
				tmpLi.append(char)
				print("[DEBUG]: Found end of ignore.")
				charNo += 1
				continue
			elif(("".join(lineLi)).endswith("\\")):
				foundIgnore = True
				print("[DEBUG]: Found ignore.")
				charNo += 1
				continue
			elif(("".join(lineLi)).endswith("print ") or foundPrint):
				if(not foundPrint):
					if(useDebug == "YES"):
						print("[DEBUG]: Found print.")
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
					if(useDebug == "YES"):
						print("[DEBUG]: Found wait.")
					foundWait = True
				else:
					if(char.isdigit()):
						tmpLi.append(char)
					else:
						print("[ERROR] {} is not a digit, ignoring.".format(char))
						errorType2 += 1
						foundError = True
					if(charNo+1 == len(line)):
						dest.write("time.sleep({})".format("".join(tmpLi)))
						tmpLi = []
						foundWait = False
			elif(("".join(lineLi)).endswith("//")):
				if(useDebug == "YES"):
					print("[DEBUG]: Found one-line comment.")
				break
			elif(("".join(lineLi)).endswith("\"")):
				foundComment = True
				if(useDebug == "YES"):
					print("[DEBUG]: Found multi-line comment.")
				break
			if(foundIgnore):
				foundIgnore = False
			charNo += 1
		if((lineNo+1 != fileLength) and (charNo == len(line)) and (not foundComment) and (len(line) != 0)):
			dest.write("".join(tmpLi))
			dest.write("\n")
		lineLi = []
		charNo = 0
		lineNo += 1
		print("%.2f%s" % (round((lineNo / fileLength)*100, 2), "%"), end = "\r")
	print("\n")
	print("------------------------------------------------------------")
	if(foundError):
		if(errorType2 > 0):
			print("[!] Found {} errors of type 2 ('NaN').".format(errorType2))
		else:
			print("[?] Something is wrong with the error system.")
			time.sleep(3)
			print("Please make sure you haven't removed/edited any necessary files.")
		time.sleep(3)
		print("------------------------------------------------------------")
	print("\nCompilation done.")
		