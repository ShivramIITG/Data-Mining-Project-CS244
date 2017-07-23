import os
import io
import operator

attackType = raw_input("Enter attack type. ")

filer = open("intermed" + attackType +".txt","r")


N = int(raw_input("Enter gram size(3,5,7): "))

filew = open(str(N) + "-grams" + attackType +".txt","w")

dic = dict()

for line in filer:
	array = []
	array = map(int, line.strip().split(' '))
	#print array

	string = ""
	for i in range(0,N-1):
		string = string + str(array[i]) + " "
	string = string + str(array[N-1])
	#print string

	if string in dic:
		dic[string] = dic[string] + 1
	else:
		dic[string] = 1

	if(array[7] == 1):
		for st in range(1,7-N+1):
			string = ""
			for i in range(st,st+N-1):
				string = string + str(array[i]) + " "
			string = string + str(array[st+N-1])
			#print string

			if string in dic:
				dic[string] = dic[string] + 1
			else:
				dic[string] = 1

ct = 0


sorted_dic = sorted(dic.items(), key=operator.itemgetter(1),reverse = True)

for key,value in sorted_dic:
	wr = key + " count = " + str(value)
	ct = ct + value
	filew.write(wr + "\n")

print "Total = " + str(ct)