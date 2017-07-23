import os
import io

attackType = raw_input("Enter attack type. ")

filer = open("concat" + attackType +".txt","r")
filew = open("intermed" + attackType +".txt","w")


for line in filer:
	array = []
	array = map(int, line.strip().split(' '))
	

	string = ""
	for y in range(0,6):

		string = string + str(array[y])
		string = string + " "

	for x in range(0,len(array)):
		#print (string)
		if(x+6 >= len(array)):
			break
		string = string + str(array[x+6])
		string = string + " "	

		wrString = string
		if(x+6 == len(array)-1):
			wrString = wrString + "1"
		else:
			wrString = wrString + "0"

		st=0
		while(1):
			if(string[st]==' '):
				break
			st=st+1

		string = string[st+1:]	

		filew.write(wrString + "\n")



filer1 = open("concat" + attackType +"Test.txt","r")
filew1 = open("intermed" + attackType +"Test.txt","w")


for line in filer1:
	array = []
	array = map(int, line.strip().split(' '))
	

	string = ""
	for y in range(0,6):

		string = string + str(array[y])
		string = string + " "

	for x in range(0,len(array)):
		#print (string)
		if(x+6 >= len(array)):
			break
		string = string + str(array[x+6])
		string = string + " "	

		wrString = string
		if(x+6 == len(array)-1):
			wrString = wrString + "1"
		else:
			wrString = wrString + "0"

		st=0
		while(1):
			if(string[st]==' '):
				break
			st=st+1

		string = string[st+1:]	

		filew1.write(wrString + "\n")