"""
author Name : Shishir 
author FB Link : facebook.com/shishirislam80
author github link : github.com/Devsabirul
"""
# Python code to demonstrate stdev() function
# importing Statistics module
from re import A
import statistics

# creating an empty list
lists = []
# number of elemetns as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
    ele = int(input())
    lists.append(ele)  # adding the element

# Calculate Standard_Deviation

Standard_Deviation = statistics.stdev(lists)


# Calculate Standardization

print("------------------------------")
print("Standardization Value Is : ")


def standardization(x, list):
    a = x
    b = statistics.mean(list)
    z = a - b
    return z / Standard_Deviation


for i in lists:
    print(standardization(i, lists))
