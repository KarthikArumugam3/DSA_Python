sorted_nums = [1,2,3,4,5,6,7,8,9,10]

def binary_search(sorted_list,num):

    start = 0
    end = len(sorted_nums)-1
    middle = int((start + end)/2)

    while not sorted_nums[middle] == num and start < end:
        if sorted_nums[middle] <  num:
            #print("Num you are finding is on the right of middle of num")
            start = middle+1
            middle = int((start + end)/2)

        elif sorted_nums[middle] > num:
            #print("Num you are finding is on the left of middle of num")
            end = middle-1
            middle = int((start + end)/2)

    if sorted_nums[middle] == num:
        print(f"The number {num} is found at {middle} position.")
    
    elif start>end:
        print("The no is not in this list")


binary_search(sorted_nums,8)
