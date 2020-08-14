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
for element in uniqueset:
	if frequentList.count(element)>=freqvalue:
		print(element)





	




		





