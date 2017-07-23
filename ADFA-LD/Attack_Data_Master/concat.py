import os
import io

attackType = raw_input("Enter attack type. ")

filew = open("concat" + attackType +".txt", "w")

var = 1
for x in range(1,8):
	
	if(attackType == "Normal"):
		directory = "../Training_Data_Master/"
		print "CHECK " + directory
	else:
		directory = "./"+attackType+"_" + str(x) + "/"
		print "CHECK " + directory

	if(attackType == "Normal" and x==2):
		break
	
	for filename in os.listdir(directory):
		print "File is " + filename

		
		filer = open(directory + filename,"r")
		for line in filer:
			
			if(var == 1 and attackType == "Adduser"):
				filew.write(line)
			else:
				filew.write(line + "\n")

		var = var + 1


filew2= open("concat" + attackType +"Test.txt", "w")
var = 1
for x in range(8,11):
	
	if(attackType == "Normal"):
		directory = "../Validation_Data_Master/"
		print "CHECK " + directory
	else:
		directory = "./"+attackType+"_" + str(x) + "/"
		print "CHECK " + directory

	if(attackType == "Normal" and x==9):
		break
	
	for filename in os.listdir(directory):
		print "File is " + filename + " " + str(var)
		if(filename == ".DS_Store"):
			print("Skip")
			continue

		filer = open(directory + filename,"r")
		for line in filer:	
			filew2.write(line + "\n")

		var = var + 1
