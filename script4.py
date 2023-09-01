from sys import *
import os
import hashlib

def calculatechecksum(path,blocksize=1024):
	fd=open(path,'rb')
	hobj=hashlib.md5()
	
	buffer=fd.read(blocksize)
	while len(buffer)>0:
		hobj.update(buffer)
		buffer=fd.read(blocksize)
		
	fd.close()
	return hobj.hexdigest()
	
def directorytraversal(path):
	#print("contents of directory are")
	scanned=0
	duplicate={}
	
	for folder,subfolder,filename in os.walk(path):
		#print("directory name is : "+folder)
		
		#for sub in subfolder:
			#print("subfolder in " + folder + " is/are "+sub)
		for f in filename:
			scanned+=1
			#print("file name is : "+f)
			actualpath=os.path.join(folder,f)
			hash=calculatechecksum(actualpath)
			#print(actualpath,hash)
			
			if hash in duplicate:
				duplicate[hash].append(actualpath)
			else:
				duplicate[hash]=[actualpath]
				
	return duplicate,scanned
	
def displayduplicate(duplicate):
	output=filter(lambda x : len(x) > 1,duplicate.values())
	
	# filter doees not need loop 
	# in every iteration x contains list of each kkeey from dicttionary
	print("output variable is ",output)
	if(len(output) >0): #how many list are there inn output in lae man's languauge
		print("there are duplicate files")
	else:
		print("there are no duplicate files")
		return
	
	icnt=0
	for result in output:
		print("result variable is",result)
		for path in result:
			print("path variable is ",path)
			icnt+=1
			if icnt>=2:
				print("%s"%path)
				os.remove(path)
		icnt=0
#total files sccanned
#duplictae file
#file deleted

def main():
	print("Marvellous system")
	print("Directory traversal script")
	
	if(len(argv)!=2):
		print("error : invalid number of argument")
		exit()
		
	if(argv[1]=="-h") or (argv[1]=="-H"):
		print("it is a directory cleaner script")
		exit()
		
	if(argv[1]=="-u") or (argv[1]=="-U"):
		print("Usage provide absolute path of target directory")
		exit()
	
	arr={}
	
	arr,scanned=directorytraversal(argv[1])
	print("the total no of files scanned are",scanned)
	print("do you want to delete files?y/n")
	b=input()
	print(b)
	yes='y'
	if b==yes:
		#delete duplicate
		displayduplicate(arr)
	elif b=='n':
		exit()
	
if __name__=="__main__":
	main()
	

