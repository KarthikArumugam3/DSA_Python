#Write a function that takes in a sorted array of integers as well as target integer.
#The function should use binary search algo to determine if the target integer is contained in the array and should return its index if it is, otherwise -1

#Sample Input:
#array = [ 0, 1, 21, 33, 45,45,61,71, 72, 73 ]
#target = 33

#Sample Output:
#3


array = [0,1,21,33,45,45,61,71,72,73]
target = 33
 
def find_num(sorted_array, target):

    start = 0
    end = len(sorted_array)-1
    middle = int((start + end)/2)

    while not sorted_array[middle] == target and start < end:
        if sorted_array[middle] < target:
            start+=1
            middle = int((start+end) /2)

        elif sorted_array[middle] > target:
            end = end - 1
            middle = int((start+end) /2)

    if sorted_array[middle] == target:
        print(f"The {target} was found at index: {middle}")

    elif start >= end:
        print(-1)

find_num(array, target)
