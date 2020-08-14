import re
f=open("Market_Basket_V3.csv","r")
f1=f.readlines()
cartList=[]
itemList=[]
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
	modifiedItemList=[]
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
#print(finalCartList)
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
#print(frequentList)
freqvalue=noe*10/100
print(freqvalue)
uniqueset=set(frequentList)
freqvalue=freqvalue+1

########################################################frequent item in a list filist
filist=[]
for element in uniqueset:
	if frequentList.count(element)>=freqvalue:
		filist.append(element)
print("Most Frequent Items")
print(filist)
print("Most Frequent Items bought together")

f2list=[]
nof=len(filist)
for felement in range(0,nof):
	counter=0
	for selement in range(felement+1,nof):
		
		for sublist in finalCartList:
			if filist[felement] in sublist and filist[selement] in sublist:
				counter=counter+1
		if counter>freqvalue:
			fsublist=[]
			fsublist.append(filist[felement])
			fsublist.append(filist[selement])
			f2list.append(fsublist)
print(f2list)
print(len(f2list))
#def intersect(list1,list2):
#	return(len(set(list1) & set(list2)))

#f3list=[]
#set1={}
#itemset2=len(f2list)
#for var1 in range(0,itemset2):
#	for var2 in range(var1+1,itemset2):
#		if intersect(f2list[var1],f2list[var2]) 
#			#print("true")
#			set1=set(f2list[var1]).union(set(f2list[var2]))
#			f3list.append(set1)
#print("3 Items bought together")
#print(f3list)


	




		





