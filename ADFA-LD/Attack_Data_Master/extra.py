
import os
import io

N = int(raw_input("Enter gram size(3,5,7) for test data: "))

filer1 = open(str(N) + "-grams" + "Adduser" +".txt","r")
filer2 = open(str(N) + "-grams" + "Hydra_FTP" +".txt","r")
filer3 = open(str(N) + "-grams" + "Hydra_SSH" +".txt","r")
filer4 = open(str(N) + "-grams" + "Java_Meterpreter" +".txt","r")
filer5 = open(str(N) + "-grams" + "Meterpreter" +".txt","r")
filer6 = open(str(N) + "-grams" + "Web_Shell" +".txt","r")

lines1 = filer1.readlines()
lines2 = filer2.readlines()
lines3 = filer3.readlines()
lines4 = filer4.readlines()
lines5 = filer5.readlines()
lines6 = filer6.readlines()

filew = open(str(N) + "-grams-trainfeatures.txt","w")
filewf = open(str(N) + "-grams-traindata.txt","w")

dict1 = dict()
for i in range(0,len(lines1)):
	curLine = lines1[i].rstrip()
	st = 0
	while(st<len(curLine)):
		if(curLine[st] == 'c'):
			break;
		else:
			st=st+1
	st = st-2

	curCount = int(curLine[st+10:])
	curLine = curLine[0:st+1]

	dict1[curLine] = curCount

dict2 = dict()
for i in range(0,len(lines2)):
	curLine = lines2[i].rstrip()
	st = 0
	while(st<len(curLine)):
		if(curLine[st] == 'c'):
			break;
		else:
			st=st+1
	st = st-2

	curCount = int(curLine[st+10:])
	curLine = curLine[0:st+1]

	dict2[curLine] = curCount

dict3 = dict()
for i in range(0,len(lines3)):
	curLine = lines3[i].rstrip()
	st = 0
	while(st<len(curLine)):
		if(curLine[st] == 'c'):
			break;
		else:
			st=st+1
	st = st-2

	curCount = int(curLine[st+10:])
	curLine = curLine[0:st+1]

	dict3[curLine] = curCount

dict4 = dict()
for i in range(0,len(lines4)):
	curLine = lines4[i].rstrip()
	st = 0
	while(st<len(curLine)):
		if(curLine[st] == 'c'):
			break;
		else:
			st=st+1
	st = st-2

	curCount = int(curLine[st+10:])
	curLine = curLine[0:st+1]

	dict4[curLine] = curCount

dict5 = dict()
for i in range(0,len(lines5)):
	curLine = lines5[i].rstrip()
	st = 0
	while(st<len(curLine)):
		if(curLine[st] == 'c'):
			break;
		else:
			st=st+1
	st = st-2

	curCount = int(curLine[st+10:])
	curLine = curLine[0:st+1]

	dict5[curLine] = curCount

dict6 = dict()
for i in range(0,len(lines6)):
	curLine = lines6[i].rstrip()
	st = 0
	while(st<len(curLine)):
		if(curLine[st] == 'c'):
			break;
		else:
			st=st+1
	st = st-2

	curCount = int(curLine[st+10:])
	curLine = curLine[0:st+1]

	dict6[curLine] = curCount

tot = 1

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []

""" For Adduser """
for i in range(0,len(lines1)):
	if(float(i)/len(lines1) > 0.30):
		break

	curLine = lines1[i].rstrip()
	st = 0
	while(st<len(curLine)):
		if(curLine[st] == 'c'):
			break;
		else:
			st=st+1
	st = st-2

	curCount = int(curLine[st+10:])
	curLine = curLine[0:st+1]
	print(curLine,curCount)

	list1.append(curCount)

	if curLine in dict2:
		list2.append(dict2[curLine])
	else:
		list2.append(0)

	if curLine in dict3:
		list3.append(dict3[curLine])
	else:
		list3.append(0)

	if curLine in dict4:
		list4.append(dict4[curLine])
	else:
		list4.append(0)

	if curLine in dict5:
		list5.append(dict5[curLine])
	else:
		list5.append(0)

	if curLine in dict6:
		list6.append(dict6[curLine])
	else:
		list6.append(0)


	filew.write("F"+str(tot)+" "+curLine+"\n")
	tot=tot+1

""" For Hydra FTP """
for i in range(0,len(lines2)):
	if(float(i)/len(lines2) > 0.30):
		break

	curLine = lines2[i].rstrip()
	st = 0
	while(st<len(curLine)):
		if(curLine[st] == 'c'):
			break;
		else:
			st=st+1
	st = st-2

	curCount = int(curLine[st+10:])
	curLine = curLine[0:st+1]
	print(curLine,curCount)

	list2.append(curCount)

	if curLine in dict1:
		list1.append(dict1[curLine])
	else:
		list1.append(0)

	if curLine in dict3:
		list3.append(dict3[curLine])
	else:
		list3.append(0)

	if curLine in dict4:
		list4.append(dict4[curLine])
	else:
		list4.append(0)

	if curLine in dict5:
		list5.append(dict5[curLine])
	else:
		list5.append(0)

	if curLine in dict6:
		list6.append(dict6[curLine])
	else:
		list6.append(0)


	filew.write("F"+str(tot)+" "+curLine+"\n")
	tot=tot+1

""" For Hydra SSH """
for i in range(0,len(lines3)):
	if(float(i)/len(lines3) > 0.30):
		break

	curLine = lines3[i].rstrip()
	st = 0
	while(st<len(curLine)):
		if(curLine[st] == 'c'):
			break;
		else:
			st=st+1
	st = st-2

	curCount = int(curLine[st+10:])
	curLine = curLine[0:st+1]
	print(curLine,curCount)

	list3.append(curCount)

	if curLine in dict1:
		list1.append(dict1[curLine])
	else:
		list1.append(0)

	if curLine in dict2:
		list2.append(dict2[curLine])
	else:
		list2.append(0)

	if curLine in dict4:
		list4.append(dict4[curLine])
	else:
		list4.append(0)

	if curLine in dict5:
		list5.append(dict5[curLine])
	else:
		list5.append(0)

	if curLine in dict6:
		list6.append(dict6[curLine])
	else:
		list6.append(0)


	filew.write("F"+str(tot)+" "+curLine+"\n")
	tot=tot+1

""" For Java meterpreter """
for i in range(0,len(lines4)):
	if(float(i)/len(lines4) > 0.30):
		break

	curLine = lines4[i].rstrip()
	st = 0
	while(st<len(curLine)):
		if(curLine[st] == 'c'):
			break;
		else:
			st=st+1
	st = st-2

	curCount = int(curLine[st+10:])
	curLine = curLine[0:st+1]
	print(curLine,curCount)

	list4.append(curCount)

	if curLine in dict1:
		list1.append(dict1[curLine])
	else:
		list1.append(0)

	if curLine in dict2:
		list2.append(dict2[curLine])
	else:
		list2.append(0)

	if curLine in dict3:
		list3.append(dict3[curLine])
	else:
		list3.append(0)

	if curLine in dict5:
		list5.append(dict5[curLine])
	else:
		list5.append(0)

	if curLine in dict6:
		list6.append(dict6[curLine])
	else:
		list6.append(0)


	filew.write("F"+str(tot)+" "+curLine+"\n")
	tot=tot+1

""" For Meterpreter """
for i in range(0,len(lines5)):
	if(float(i)/len(lines5) > 0.30):
		break

	curLine = lines5[i].rstrip()
	st = 0
	while(st<len(curLine)):
		if(curLine[st] == 'c'):
			break;
		else:
			st=st+1
	st = st-2

	curCount = int(curLine[st+10:])
	curLine = curLine[0:st+1]
	print(curLine,curCount)

	list5.append(curCount)

	if curLine in dict1:
		list1.append(dict1[curLine])
	else:
		list1.append(0)

	if curLine in dict2:
		list2.append(dict2[curLine])
	else:
		list2.append(0)

	if curLine in dict3:
		list3.append(dict3[curLine])
	else:
		list3.append(0)

	if curLine in dict4:
		list4.append(dict4[curLine])
	else:
		list4.append(0)

	if curLine in dict6:
		list6.append(dict6[curLine])
	else:
		list6.append(0)


	filew.write("F"+str(tot)+" "+curLine+"\n")
	tot=tot+1


""" For Webshell """
for i in range(0,len(lines6)):
	if(float(i)/len(lines6) > 0.30):
		break

	curLine = lines6[i].rstrip()
	st = 0
	while(st<len(curLine)):
		if(curLine[st] == 'c'):
			break;
		else:
			st=st+1
	st = st-2

	curCount = int(curLine[st+10:])
	curLine = curLine[0:st+1]
	print(curLine,curCount)

	list6.append(curCount)

	if curLine in dict1:
		list1.append(dict1[curLine])
	else:
		list1.append(0)

	if curLine in dict2:
		list2.append(dict2[curLine])
	else:
		list2.append(0)

	if curLine in dict3:
		list3.append(dict3[curLine])
	else:
		list3.append(0)

	if curLine in dict4:
		list4.append(dict4[curLine])
	else:
		list4.append(0)

	if curLine in dict5:
		list5.append(dict5[curLine])
	else:
		list5.append(0)


	filew.write("F"+str(tot)+" "+curLine+"\n")
	tot=tot+1

str1 = ' '.join(str(e) for e in list1)
filewf.write("Adduser: "+str1+"\n")

str2 = ' '.join(str(e) for e in list2)
filewf.write("Hydra FTP: "+str2+"\n")

str3 = ' '.join(str(e) for e in list3)
filewf.write("Hydra SSH: "+str3+"\n")

str4 = ' '.join(str(e) for e in list4)
filewf.write("Java Meterpreter: "+str4+"\n")

str5 = ' '.join(str(e) for e in list5)
filewf.write("Meterpreter: "+str5+"\n")

str6 = ' '.join(str(e) for e in list6)
filewf.write("Web Shell: "+str6+"\n")