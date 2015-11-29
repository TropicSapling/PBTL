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
	print("ERROR #1: Invalid file extension. Must be '.pbtl' or '.pseudo'.")
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
	foundPrint2 = False
	foundPrint3 = False
	foundComment = False
	foundIgnore = False
	foundError = False
	foundWait = False
	errorType2 = 0
	
	# Prepare
	for line in fileLi:
		for char in line:
			lineLi.append(char)
			if((("".join(lineLi)).endswith("wait ")) and (not foundWait)):
				dest.write("import time\n")
				if(useDebug == "YES"):
					print("[DEBUG]: Imported 'time'.")
				foundWait = True
			elif(("".join(lineLi)).endswith("; as signal ") and (not foundPrint2)):
				dest.write("import socket\n")
				if(useDebug == "YES"):
					print("[DEBUG]: Imported 'socket'.")
				foundPrint2 = True
		lineLi = []
		lineNo += 1
		print("%.2f%s" % (round((lineNo / fileLength)*100, 2), "%"), end = "\r")
	lineNo = 0
	lineLi = []
	if(foundWait or foundPrint2):
		dest.write("\n")
	foundWait = False
	foundPrint2 = False
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
					elif((("".join(lineLi)).endswith("; as signal to ")) or foundPrint2):
						if(foundPrint2):
							if(char == ":"):
								start2 = end1+1
								end2 = start2
								end1 -= 1
								if(useDebug == "YES"):
									print("[DEBUG]: Found port.")
							elif(charNo+1 == len(line)):
								dest.write("s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n")
								dest.write("s.connect(('{}', {}))\n".format("".join(tmpLi[start1:end1+1]), "".join(tmpLi[start2:end2+1])))
								dest.write("s.send(\"{}\")\n".format("".join(tmpLi[:start1])))
								dest.write("data = s.recv(1024)\n")
								dest.write("s.close\n")
								dest.write("print(\"[{}] \", data)".format("".join(tmpLi[start1:end1+1])))
								tmpLi = []
								foundPrint2 = False
								foundPrint = False
							if(start2 == -1):
								end1 += 1
							else:
								end2 += 1
						else:
							tmpLi = tmpLi[:-15]
							start1 = charNo-20
							end1 = start1
							start2 = -1
							foundPrint2 = True
							if(useDebug == "YES"):
									print("[DEBUG]: Found IP.")
					elif((("".join(lineLi)).endswith("; as signal from ")) or foundPrint3):
						if(foundPrint3):
							if(char == ":"):
								start2 = end1+1
								end2 = start2
								if(useDebug == "YES"):
									print("[DEBUG]: Found port.")
							elif(charNo+1 == len(line)):
								dest.write("s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n")
								dest.write("s.bind(('{}', {}))\n".format("".join(tmpLi[start1:end1]), "".join(tmpLi[start2:end2])))
								dest.write("s.listen(1)\n")
								dest.write("conn, addr = s.accept()\n")
								dest.write("while 1:\n")
								dest.write("	if not conn.recv(BUFFER_SIZE): break\n")
								dest.write("	print(\"[{}] \", data)".format("".join(tmpLi[start1:end1])))
								dest.write("\n	conn.send(data)\n")
								dest.write("conn.close()")
								tmpLi = []
								foundPrint3 = False
								foundPrint = False
							if(start2 == -1):
								end1 += 1
							else:
								end2 += 1
						else:
							tmpLi = tmpLi[:-17]
							start1 = charNo+1
							end1 = start1
							start2 = -1
							foundPrint3 = True
							if(useDebug == "YES"):
									print("[DEBUG]: Found IP.")
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
		
