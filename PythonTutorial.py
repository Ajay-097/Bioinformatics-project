# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 19:15:57 2022

@author: ASUS
"""

# PYTHON Tutorials

#%%
# Using enumerate 

flavours = ["vanilla", "chocolate", "strawberry"]
prices = [10.0,12.5,11.5]

for i,flavour in enumerate(flavours):
    print( flavour + " costs -- " , prices[i])

# vanilla costs --  10.0
# chocolate costs --  12.5
# strawberry costs --  11.5

#%%

# Using zip is a better solution. If we require the entries of multiple lists that have the same size and indices correspond to values
# that map between the lists

flavours = ["vanilla", "chocolate", "strawberry"]
prices = [10.0,12.5,11.5]
quantity = [10,20,30]

for i, (flavour,price,qt) in enumerate(zip(flavours,prices,quantity)):
    print(i, flavour + " costs -- ", price , qt)

#%%

#Usage of contunue key word - coupled with an if condition we can skip the current iteration and move to the next iteration

flavours = ["vanilla", "chocolate", "strawberry"]
prices = [10.0,12.5,11.5]

for (flavour,price) in zip(flavours,prices):
    if(price > 11.5):
        continue
    print(flavour + " costs -- ", price)
    
#%%

#Dictionaries are key - value pairs. We can loop over them just like lists

menu = {"vanilla icecream":1.25,
        "sickleberry swirl":2.50,
        "apple cone":2.10,
        "strawberry cup":1.50
        }

for thing in menu.items():
    print(thing[1]) #prints the result as a tuple of key - value pairs that have index

#%%

#function can also be passed as an argument. Lambda is used to write inline functions

def printList(lst, func):
    for item in lst:
        print(func(item))
        
printList(["a","b","c"], lambda item: " __" + item + "__")

#%% Slicing

#negative index starts from -1 which is the last element.
# v1:v2:(this value) is the incrementor

numList = list(range(25))
#print (numList[:])
print(numList[20:])
print(numList[:-2])

print(numList[12::4])

print(numList[::-1])

#%%
#exception Handling
#key words - try , except , finally

#assertion instance -assert

A = [1,2,4,5,6,7,8,9]

A.sort()
min = 1
for num in A:
    if num == min:
        min+=1
print(A,min)

#%%

N = 32

bin_num = str(bin(N))
bin_num = bin_num.replace('0b','')

print(bin_num)

max = 0
numList = bin_num.split('1')
for i in range (len(numList) - 1):
    if len(numList[i]) > max:
        max = len(numList[i])

print(numList)
print(max)




    

    
