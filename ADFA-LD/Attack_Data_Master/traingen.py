import os
import io

import time
start_time = time.time()

N = int(raw_input("Enter gram size(3,5,7) for test data: "))

filer = []
filer.append(open(str(N) + "-grams" + "Adduser" +".txt","r"))
filer.append(open(str(N) + "-grams" + "Hydra_FTP" +".txt","r"))
filer.append(open(str(N) + "-grams" + "Hydra_SSH" +".txt","r"))
filer.append(open(str(N) + "-grams" + "Java_Meterpreter" +".txt","r"))
filer.append(open(str(N) + "-grams" + "Meterpreter" +".txt","r"))
filer.append(open(str(N) + "-grams" + "Web_Shell" +".txt","r"))
filer.append(open(str(N) + "-grams" + "Normal" +".txt","r"))

inter = []
inter.append(open("intermed" + "Adduser" +".txt","r"))
inter.append(open("intermed" + "Hydra_FTP" +".txt","r"))
inter.append(open("intermed" + "Hydra_SSH" +".txt","r"))
inter.append(open("intermed" + "Java_Meterpreter" +".txt","r"))
inter.append(open("intermed" + "Meterpreter" +".txt","r"))
inter.append(open("intermed" + "Web_Shell" +".txt","r"))
inter.append(open("intermed" + "Normal" +".txt","r"))

inter.append(open("intermed" + "AdduserTest" +".txt","r"))
inter.append(open("intermed" + "Hydra_FTPTest" +".txt","r"))
inter.append(open("intermed" + "Hydra_SSHTest" +".txt","r"))
inter.append(open("intermed" + "Java_MeterpreterTest" +".txt","r"))
inter.append(open("intermed" + "MeterpreterTest" +".txt","r"))
inter.append(open("intermed" + "Web_ShellTest" +".txt","r"))
inter.append(open("intermed" + "NormalTest" +".txt","r"))


lines = []
for i in range(0,7):
	lines.append(filer[i].readlines())


filew = open(str(N) + "-grams-trainfeatures.txt","w")
filewf = open(str(N) + "-grams-traindata.txt","w")
filewf2 = open(str(N) + "-grams-testdata.txt","w")

dic =  dict()

tot = 1

for j in range(0,7):

	for i in range(0,len(lines[j])):
		if(float(i)/len(lines[j]) > 0.30):
			break

		curLine = lines[j][i].rstrip()
		st = 0
		while(st<len(curLine)):
			if(curLine[st] == 'c'):
				break;
			else:
				st=st+1
		st = st-2

		curCount = int(curLine[st+10:])
		curLine = curLine[0:st+1]
		#print(curLine,curCount)

		if curLine in dic:
			pass
		else:
			filew.write("F"+str(tot)+" "+curLine+"\n")
			dic[curLine]=tot
			tot=tot+1

dic1 = dict()

for j in range(0,14):
	for line in inter[j]:
		array = []
		array = map(int, line.strip().split(' '))
		#print array

		string = ""
		for i in range(0,N-1):
			string = string + str(array[i]) + " "
		string = string + str(array[N-1])
		#print (str(j)+ " " +string)

		if string in dic1:
			dic1[string] = dic1[string] + 1
		else:
			dic1[string] = 1


		if(array[7] == 1):
			for st in range(1,7-N+1):
				string = ""
				for i in range(st,st+N-1):
					string = string + str(array[i]) + " "
				string = string + str(array[st+N-1])

				#print (str(j)+ " " +string)

				if string in dic1:
					dic1[string] = dic1[string] + 1
				else:
					dic1[string] = 1

			fVec = []
			for l in range(0,tot-1):
				fVec.append(0)

			for key,value in dic1.items():
				if key in dic:
					fVec[dic[key]-1] = value

			str1 = ' '.join(str(e) for e in fVec)
			if(j==0):
				filewf.write("Adduser: "+str1+"\n")
			if(j==1):
				filewf.write("Hydra FTP: "+str1+"\n")
			if(j==2):
				filewf.write("Hydra SSH: "+str1+"\n")
			if(j==3):
				filewf.write("Java Meterpreter: "+str1+"\n")
			if(j==4):
				filewf.write("Meterpreter: "+str1+"\n")
			if(j==5):
				filewf.write("Web Shell: "+str1+"\n")
			if(j==6):
				filewf.write("Normal: "+str1+"\n")
			if(j>6):
				filewf2.write("Test: "+str1+"\n")

			dic1.clear()

print("--- %s seconds ---" % (time.time() - start_time))