import sys
from math import log


def calcPMI(count1,count2,countJoint,countTotal):
	if count1==0 or count2==0 or countJoint==0 or countTotal==0:
		return -99
	else:
		#print(str(count1)+" "+str(count2)+" "+str(countJoint)+" "+str(countTotal))
		
		# if temp>=1:
		pmi=log((float(countJoint)*countTotal)/(count1*count2))

		# else:
		# 	temp=1/temp
		# 	pmi=-log(temp)	
		return pmi


def calcNormPMI(count1,count2,countJoint,countTotal):
	if count1==0 or count2==0 or countJoint==0 or countTotal==0:
		return -1
	else:
		#print(str(count1)+" "+str(count2)+" "+str(countJoint)+" "+str(countTotal))
		
		# if temp>=1:
		pmi=log((float(countJoint)*countTotal)/(count1*count2))
		normPMI=pmi/log(float(countTotal)/countJoint)
		# else:
		# 	temp=1/temp
		# 	pmi=-log(temp)	
		return normPMI		


def writeDictToFile(dict,countBound,countTotal,outFileName):#,f):
	print(outFileName)
	f=open(outFileName,'w')
	for x in dict:
		f.write(x)
		f.write('\t')
		f.write(str(dict[x][1]))
		f.write('\t')
		f.write(str(countBound))
		f.write('\t')
		f.write(str(dict[x][0]))
		f.write('\t')
		f.write(str(countTotal))
		f.write('\t')
		#f.write(str(calcPMI(dict[x][1],countBound,dict[x][0],countTotal)))
		f.write(dict[x][2])
		f.write('\n')
		
	f.close()


def sortBy():
	if sortby=="countWord":
		return 1
	elif sortby=="countJoint":
		return 0
	elif sortby=="pmi":
		return 2
	elif sortby=="normPMI":
		return 3

# def sortDictAndPrint(diction,outFileName):
# 	print(outFileName)
# 	f=open(outFileName,'w')
# 	for i in sorted(diction,key=diction.__getitem__[1],reverse=True):
# 		f.write(str(i))
# 		f.write('\t')
# 		f.write(str(diction[i][0]))
# 		f.write('\t')
# 		f.write(str(diction[i][1]))
# 		f.write('\t')
# 		f.write(str(diction[i][2]))
# 		f.write('\t')
# 		f.write(str(diction[i][3]))
# 		f.write('\n')
		
# 	f.close()

def sortDictAndPrint(diction,outFileName):
	print(outFileName)
	f=open(outFileName,'w')
	
	s=sortBy()
	for key, value in sorted(diction.iteritems(),key=lambda (k,v):(v[s],k),reverse=True):
		f.write(str(key))
		f.write('\t')
		f.write(str(value[0]))
		f.write('\t')
		f.write(str(value[1]))
		f.write('\t')
		f.write(str(value[2]))
		f.write('\t')
		f.write(str(value[3]))
		f.write('\n')
		
	f.close()	

global sortby
filename=str(sys.argv[1])#input("Enter filename: ")
hist=int(sys.argv[2])#int(input( "Enter number of h:"))
forw=int(sys.argv[3])#int(input("Enter number of j:"))
sortby=sys.argv[4] # options- countWord,countJoint,pmi,normPMI
size=hist+forw


dictList=[dict() for i in range (size)]  # list of dictionaries for different word contexts. Each dictionary has word as key and an array [countJoint count1 pmi normPMI] as value

wordList=[]   #list of all words including boundaries

file=open(filename,"r")
for line in file:
	for word in line.split():
		wordList.append(word)


numWords=len(wordList)
countBound=0

for i in range (numWords):


	if wordList[i]=="." : #sentence boundary. change this acc to data
		countBound+=1
		for k in range(i-1,max(-1,i-hist-1),-1):
			dictList[i-1-k][wordList[k]][0]=dictList[i-1-k].setdefault(wordList[k],[0,0,0,0])[0]+1
			

		for l in range(i+1,min(numWords,i+forw+1),1):
			dictList[l-i-1+hist][wordList[l]][0]=dictList[l-i-1+hist].setdefault(wordList[l],[0,0,0,0])[0]+1
	
	else:
		for m in range(size):
			dictList[m][wordList[i]][1]=dictList[m].setdefault(wordList[i],[0,0,0,0])[1]+1

for i in range(0,hist):
	outFileName="h"+str(i+1)+".txt"
	for x in dictList[i]:
		dictList[i][x][2]=calcPMI(dictList[i][x][1],countBound,dictList[i][x][0],numWords)
		dictList[i][x][3]=calcNormPMI(dictList[i][x][1],countBound,dictList[i][x][0],numWords)
	sortDictAndPrint(dictList[i],outFileName)

for i in range(hist,size):
	outFileName="j"+str(i-hist+1)+".txt"
	for x in dictList[i]:
		dictList[i][x][2]=calcPMI(dictList[i][x][1],countBound,dictList[i][x][0],numWords)
		dictList[i][x][3]=calcNormPMI(dictList[i][x][1],countBound,dictList[i][x][0],numWords)
	sortDictAndPrint(dictList[i],outFileName)
#outputFileList=[]
# for i in range(0,hist):
# 	outFileName="h"+str(i+1)+".txt"
# 	writeDictToFile(dictList[i],countBound,numWords,outFileName)
	
# for i in range(hist,size):
# 	outFileName="j"+str(i-hist+1)+".txt"
# 	writeDictToFile(dictList[i],countBound,numWords,outFileName)

