"""
https://littlealchemy.com/
# Get example
bases.names[bases.base[1].parents[0][0]]+"+"+bases.names[bases.base[1].parents[0][1]]+"="+bases.names[1]
ice+fire=water
# Get dat (python)
for x in bases.base:
	for y in bases.base[x].parents: 
		bases.names[bases.base[x].parents[y][0]]+"+"+bases.names[bases.base[x].parents[y][1]]+"="+base.names[x]
# Dat fmt
bases={
	names:{
		1:"water"
	},
	base:{
		1:{
			parents:[
				[148, 2]
			],
			tags: ["water"]
		}
	}
}
# Get dat (Console JS)
a=""
for (x in bases.base){
	for (y in bases.base[x].parents){
		a+=bases.names[bases.base[x].parents[y][0]]+"+"+bases.names[bases.base[x].parents[y][1]]+"="+bases.names[x]+"\n"
	}
}
"""

import os

os.system("cls")

print("""
AlchemPy - Little Alchemy in Python!
       (c) James C. Wise 2020
  Released under the DBaD license.
       github.com/Scripter17/

Left/Right -> Move through element list pages
Type a combination of known elements like 'elem1+elem2',
then press enter to submit. If it's a valid combination,
it'll show up in the element list!"""[1:]) # It just looks good

os.system("pause >nul && cls")

data=open("Recipes.dat", "r").read()
elements, recipes=tuple(data.split("\n-\n")) 	# Elements are separated from the recipes using a - (dash)
elements=elements.split("\n") 					# Every Element is defined in a new line
r=[]											# r is an empty array as of now
rkeys=[]										# rkeys is an empty array as of now
result = []
for x in recipes.split("\n"):					# going through every recipe. x= recipe[i]
	# What in the goddamn fuck is any of this
	com=set(x.split("=")[0].split("+"))			# com = first element + second element
	res=[x.split("=")[1]]						# res = the product of the above two elemnents
	
	if com in rkeys:							
		r[[x[0] for x in r].index(com)][1].append(res[0]) # ?????
	else:
		rkeys.append(com) 						# if com is not in rkeys, add the set of elemnts in rkeys
		r.append([com, res]) 					# and add the com and res as an array to r. [[{"earth, air"},["dust"]]...]
										# recipes has all the all the recipes in form [[{"earth, air"},["dust"]]...]

#to count total number of distinct elements
for x in recipes.split("\n"):
	res = [x.split("=")[1]]
	if res in result:
		continue
	elif res not in result:
		result.append(res[0])
		
import numpy


print(result)
print("The number of total products = "+ str(len(result)))
recipes=r
dispPage=0 # Which 8 elements to list
ePerPage=8 # How many elements to list per page
txt=""
new=""
while True:
	#print(elements)
	#print(recipes)
	pages=(len(elements)-1)//ePerPage			
	print("Page "+str(dispPage+1)+"/"+str(pages+1))
	plist=[x.capitalize() for x in elements[dispPage*ePerPage:(dispPage+1)*ePerPage]]
	print("---")
	print("\n".join(plist)+"\n"*(ePerPage-len(plist)))
	print("---")
	print(txt)
	if new!="":
		print("Discovered "+new)

	#Added code here
	#for i in 

	cin=input(">>>")
	if cin in ["next", ">", "+", "."]:
		dispPage+=1
		if dispPage*ePerPage>len(plist):
			dispPage=0
	elif cin in ["previous", "prev", "last", "<", "-", ",", "just fucking go back you piece of shit game"]:
		dispPage-=1
		if dispPage<0:
			dispPage=len(plist)//ePerPage
	elif cin=="exit":
		exit()
	else:
		cin=set(cin.split("+"))
		for x in recipes:
			if x[0]==cin:
				new=", ".join(x[1])
				for y in x[1]:
					if not y in elements:
						elements.append(y)
	os.system("cls")