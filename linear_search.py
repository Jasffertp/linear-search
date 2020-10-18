#Author: Jasffer T. Padigdig
#Date: September 10, 2020
#Description: This code takes an n-input of numbers and prompts the user to enter a number if it's inside the array
#References: 
#https://www.geeksforgeeks.org/linear-search/
#

import random

def linear_search(A, l, x):
    for i in range(0, l):
        if A[i] == x:
            return i
    return 0

A = []
l = int(input("How many items do you want in a list? "))

for i in range(0, l):
    #A.append(random.randint(1, 100))
    val = int(input(f"what is the {i} element? "))
    A.append(val)
    
length = len(A)
item = int(input("what value do you want to search for? "))
print(" ")
result = linear_search(A, length,item);

if result == 0:
    print('the item is not in the array')
    #print(A)
else:
    print(f'the item is in index {result}')
    #print(A)