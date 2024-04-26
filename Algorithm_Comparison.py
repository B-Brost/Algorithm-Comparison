"""
Algorithm_Comparison.py
Brianna Brost
4/21/23
This code compares the time complexity of three different algorithms that solve the same problem. The problem is to determine if there are two numbers in a list that sum to zero. The three algorithms are brute-force, binary search, and two-pointer. The code times each algorithm for lists of increasing length and graphs the results.
"""

import sys
import subprocess
import time
import matplotlib.pyplot as plt
import random
def algorithm_1(the_list:list[int])->bool:
# This is a brute-force approach where you’re checking every pair of numbers to see if they sum to zero. This has a time complexity of O(n^2).
    # sequesntial search for if neg is in list return bool, takes list
    # error is list empty
    if len(the_list)==0:
        raise ValueError('The list is empty.')
    #sort list
    the_list.sort()

    #iterate through the list using a nested for-loop
    for i in range(len(the_list)-1):
        # store first
        value=the_list[i]
        for j in range(1, len(the_list)):
            # num+(-num)=0 returns true
            if value+the_list[j]==0:
                return True
    
    # if no negative of value, return false
    return False           

def algorithm_2(the_list:list[int])->bool:
# This algorithm uses binary search. For each number in the list, it checks if its negative counterpart is in the list using binary search. This has a time complexity of O(n log n).
    # binary search for negative return bool, takes list
    # error is list is empty
    if len(the_list)==0:
        raise ValueError('The list is empty.')
    #sort list
    the_list.sort()

    # checks each element for negative version of it return true if binary search return true
    for element in the_list:
        num=element * -1
        if binary_search(the_list, num)==True:
            return True
    
    # if no negative then return false
    return False

def binary_search(the_list:list[int],num:int)->bool:
    # actual search for num, halfs list until negative found returns bool, takes list and num
    #variables
    start=0
    end=len(the_list)
    # false if list is empty
    if start>end:
        return False

    while start<end:
        # find the middle
        mid=(start+end)//2 

        #if the middle is num return True
        if the_list[mid]==num:
            return True
        # if num less than middle value, cut off the end of list
        elif num<the_list[mid]:
            end=mid-1
        # if num larger than middle value cut off first half of list
        else:
            start=mid+1

    # returns false if no negative
    return False

def algorithm_3(the_list:list[int])->bool:
    # This algorithm uses the two-pointer technique. It maintains two indices, one at the start and one at the end of the sorted list. Depending on whether the sum of the numbers at these indices is less than, greater than, or equal to zero, it adjusts the indices accordingly. This has a time complexity of O(n)
    # Maintain two indices i and j, initialized to the first and last element in the list, respectively.  If the two elements being indexed sum to 0, then x has been found. Otherwise, if the sum is smaller than 0, advance i; if the sum is larger than 0 then retreat j, and repeatedly test the sum until either x is found or i and j meet. 
    # return bool take list
    # error if list is empty
    if len(the_list)==0:
        raise ValueError('The list is empty.')
    #sort list
    the_list.sort()
    # i is first j is last in list
    i=the_list[0]
    j=the_list[-1]

    # before the variables are at the same point
    while i<j:
        # if found negative return true
        if i+j==0:
            return True
        # if value is negative, increment i
        elif i+j<0:
            i=i+1
        # if value is positive decrement j
        elif i+j>0:
            j=j-1
    
    # no negative, return false
    return False

def show_graph(x_vals:list,y_vals:list):
    #creates a graph where x values and y values are plotted
    #every point is of the form (x_vals[i],y_vals[i])
    plt.plot(x_vals,y_vals)
    plt.xlabel('List Length')
    plt.ylabel('Time(s)')
    plt.title(f"{algorithm}")
    plt.show()

# create lists to be graphed
x=[]
y=[]
algorithm="algorithm1"
print(algorithm)
# length of list starting at half the first length to double it everytime
n=250000
for i in range(5):
    n*=2
    # this is the num that will be first and it will be the one that has neg and pos num
    nums=[-n]
    # add all the odd neg nums 
    for i in range(-n+3,0,2):
        nums.append(i)
    # add all the even pos nums
    for i in range(2,n+2,2):
        nums.append(i)
    # timing for algorithm1
    start=time()
    algorithm_1(nums)
    end=time()
    elapsed=end-start
    # add to list to be graphed - length of list and elapsed time
    x.append(n)
    y.append(elapsed)
# shows the graph and prints the table
show_graph(x,y)
for i in range(len(x)):
    print (f"{x[i]}, {y[i]}")

algorithm="algorithm2"
print(algorithm)
n=250000
# create lists to be graphed
x=[]
y=[]
for i in range(5):
    n*=2
    # this is the num that will be first and it will be the one that has neg and pos num
    nums=[-n]
    # add all the odd neg nums 
    for i in range(-n+3,0,2):
        nums.append(i)
    # add all the even pos nums
    for i in range(2,n+2,2):
        nums.append(i)
    # timing for algorithm1
    start=time()
    algorithm_2(nums)
    end=time()
    elapsed=end-start
    # add to list to be graphed - length of list and elapsed time
    x.append(n)
    y.append(elapsed)
# shows the graph and prints the table
show_graph(x,y)
for i in range(len(x)):
    print (f"{x[i]}, {y[i]}")

algorithm="algorithm3"
print(algorithm)
n=250000
# create lists to be graphed
x=[]
y=[]
for i in range(5):
    n*=2
    # this is the num that will be first and it will be the one that has neg and pos num
    nums=[-n]
    # add all the odd neg nums 
    for i in range(-n+3,0,2):
        nums.append(i)
    # add all the even pos nums
    for i in range(2,n+2,2):
        nums.append(i)
    # timing for algorithm1
    start=time()
    algorithm_3(nums)
    end=time()
    elapsed=end-start
    # add to list to be graphed - length of list and elapsed time
    x.append(n)
    y.append(elapsed)
# shows the graph and prints the table
show_graph(x,y)
for i in range(len(x)):
    print (f"{x[i]}, {y[i]}")
