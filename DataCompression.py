from decimal import *
import sys
import os

print("============Program to demonstrate Arthmetic coding for Data Compression===========")
filename=input('Enter the file name to be compressed\n')
fileobj=open(filename,"r")
text1=fileobj.read()
fileobj.close()
textlen=len(text1)

statinfo = os.stat(filename)
print("\nThe size of input file is "+str(statinfo.st_size)+" bytes\n")

Dict={}
for i in text1:     
    Dict.setdefault(i,0)
    Dict[str(i)]= Dict[str(i)] +1
n=sum(Dict.values())
#print("The dictionary created is "+str(Dict)+"\n")
DictLen=len(Dict)

getcontext().prec=DictLen*2
for i in Dict.keys():    
    Dict[str(i)]= Decimal(Dict[str(i)]/n)
Cumprob=Dict
temp=0
for i in Cumprob.keys():
    Cumprob[str(i)]=Cumprob[str(i)]+temp
    temp=Cumprob[str(i)]
#print("Cumulative Probability for char:"+str(Cumprob))

List=list(Cumprob.values())
Diff=[Decimal(0)]
for i in List:
    Diff.append(i)

Ind=list(Cumprob.keys())
lookup=dict(zip(Ind,Diff))
#print(lookup)
precvalue=(statinfo.st_size)
#print(precvalue)
factor=1.2
while(True):
	factor=factor+0.05
	print("For precision value ="+str(int(precvalue*factor))+" ")
	getcontext().prec=int(precvalue*factor)
	encode=Decimal(1)
	Min=Decimal(1)
	Max=Decimal(1)
	bound=Decimal(1)
	x=Decimal(0)

	for i in text1:
    		Min=x+(Decimal(lookup[i])* bound)
    		Max=x+(Decimal(Cumprob[i])* bound)
    		bound=Max-Min
    		x=Min
	encode=(Min+Max)/2
	


	comp=Diff
	for i in range(len(Diff)):
    		comp[i]=Decimal(Diff[i])

	output=""
	for j in range(textlen):
    		for i in range(DictLen,-1,-1):
        		if encode<comp[i]:
            			continue 
        		else:
            			output+=str(Ind[i])            
	    			#print(Ind[i])
            			break
    		q=Decimal(comp[i+1]-comp[i])
    		comp=[(z*q)+comp[i] for z in Diff]
	

	if(output==text1):
		print(" Lossless compression\n")
		break
	else:
		print(" Error in decompresssion\n")
#print("===================================================================================")
print("The encoded data is "+str(encode))
#print(Min,Max)
print("===================================================================================\n")
print("The size of input file is "+str(statinfo.st_size)+" bytes\n")
print("The size of encoded data is "+str(sys.getsizeof(encode))+" bytes\n")
#print(output)
print("The compression ratio is "+str((statinfo.st_size)/sys.getsizeof(encode))+"\n")
print("The space saved during the compression is "+str((statinfo.st_size-sys.getsizeof(encode))/(statinfo.st_size)*100)+"%\n")
print("===================================================================================\n")
