#Index Equals Value :

#Write a function that takes in a sorted array of distinct integers and return the first index in the array that is equal to the value at that index. In the others words, your function should return the minimum index where index == array[index]

#If there is no such index, your function should return -1

#Sample Input
#Array = [ -5, -3 , 0 , 3 , 4, 5, 9 ]

#Sample Output  
#3

array = [ -5, -3 , 0, 3 , 4, 5, 9  ]

def index_equals_value(sorted_array):

    for idx,val in enumerate(sorted_array):
        if idx == val:
            print(val)
            break

        elif idx != val:
            pass

    else:
        print(-1)

index_equals_value(array)