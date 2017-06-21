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
		f.write(str(calcPMI(dict[x][1],countBound,dict[x][0],countTotal)))
		f.write('\n')
		
	f.close()


filename=str(sys.argv[1])#input("Enter filename: ")
hist=int(sys.argv[2])#int(input( "Enter number of h:"))
forw=int(sys.argv[3])#int(input("Enter number of j:"))
sortby=sys.argv[4] # options- count1,countJoint,pmi
size=hist+forw


dictList=[dict() for i in range (size)]

wordList=[]

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
			dictList[i-1-k][wordList[k]][0]=dictList[i-1-k].setdefault(wordList[k],[0,0])[0]+1
			

		for l in range(i+1,min(numWords,i+forw+1),1):
			dictList[l-i-1+hist][wordList[l]][0]=dictList[l-i-1+hist].setdefault(wordList[l],[0,0])[0]+1
	
	else:
		for m in range(size):
			dictList[m][wordList[i]][1]=dictList[m].setdefault(wordList[i],[0,0])[1]+1

#outputFileList=[]
for i in range(0,hist):
	outFileName="h"+str(i+1)+".txt"
	writeDictToFile(dictList[i],countBound,numWords,outFileName)
	
for i in range(hist,size):
	outFileName="j"+str(i-hist+1)+".txt"
	writeDictToFile(dictList[i],countBound,numWords,outFileName)

