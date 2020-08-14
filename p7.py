import re
import numpy as np 
import pandas as pd 
from apyori import apriori
f=open("Market_Basket_V3.csv","r")
f1=f.readlines()
cartList=[]
itemList=[]
listOfDictionary=[]

finalCartList=[]
#list of list
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
#print(finalCartList)[[,,],[,,],[,,],[,,]]

print("Most frequent items Set")
#for k item set
association_rules=apriori(finalCartList,min_support=0.10)
association_results=list(association_rules)
#print(association_results)

listRules=[list(association_results[i][0]) for i in range(0,len(association_results))]
print(listRules)
fwrite=open("frequentitemlist.txt","a+")
for frqlist in listRules:
	for frqitem in frqlist:
		fwrite.write("%s "%frqitem)
		fwrite.write("\n")
		









	




		





