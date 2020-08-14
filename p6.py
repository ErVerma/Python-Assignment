import re
f=open("Market_Basket_V3.csv","r")
fwrite=open("frequentlist.txt","a+")
f1=f.readlines()
cartList=[] #list of cartitem's string['a b:b c:d:',':::','::']

itemList=[]#['a b','b c','d']
listOfDictionary=[]

finalCartList=[]
finalDict={}

for fstring in f1:
     sList=fstring.split(",")
     Tid=sList[0]
     cartItem=sList[1]
     cartList.append(cartItem[1:-1])
     #print(Tid)
     Dict={}
      
     Dict[Tid]=cartItem[1:-1]
     listOfDictionary.append(Dict)

for item in cartList:
	modifiedItemList=[]#['b','c','d']
	itemList=item.split(':')
	for items in itemList:

		if re.match(r'.*\w+ \w+',items):
			transformation=re.findall("\w+$",items)[0]
			
			modifiedItemList.append(transformation)
			#print(items)
			#print(transformation)
		else:
			transformation=items
			modifiedItemList.append(transformation)
		#print(modifiedItemList)
	modifiedItemList.sort()	
	finalCartList.append(modifiedItemList)
#print(finalCartList) list of list[[],[],[]]
noe=len(listOfDictionary)
finalDict["Tid"]="cartItem"
##FINAL DICTIONARY
x=1
while x<noe:

	finalDict[x]=finalCartList[x]
	x=x+1
#print(finalDict)
frequentList=[]
for ll in finalCartList:
	frequentList=frequentList+ll
#print(frequentList) list of all cartitems
freqvalue=noe*10/100
print(freqvalue)
uniqueset=set(frequentList)
freqvalue=freqvalue+1

########################################################frequent item in a list filist
fwrite.write("Most Frequent Items Bought")
filist=[]
for element in uniqueset:
	if frequentList.count(element)>=freqvalue:
		filist.append(element)
		fwrite.write("\n%s "%element)
print("Most Frequent Items")
print(filist)
print("Most Frequent Items bought together")

f2list=[]
nof=len(filist)

def exists(felement,flist):
	for item in flist:
		if(item==felement):
			return 1
		else:
			return 0
#for 2 item set
for felement in range(0,nof):
	counter=0
	for selement in range(felement+1,nof):
		
		for sublist in finalCartList:
			
			if exists(filist[felement],sublist) and exists(filist[selement],sublist):
				counter=counter+1
		if counter>freqvalue:
			fsublist=[]
			fsublist.append(filist[felement])
			fsublist.append(filist[selement])
			f2list.append(fsublist)
			print(filist[felement],filist[selement])
			print(sublist)
			print(counter)
print(f2list)
print(len(f2list))




	




		





