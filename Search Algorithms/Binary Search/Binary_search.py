sorted_nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

def find_num(sorted_list, num):
    """Binary search function:- Given a sorted list/array and a element, returns the index at which the element is found
       If element not found, it returns "not found"

    Args:
        sorted_list (list/array): A sorted list / array
        num (int): Element to be found in the sorted_list 
    """
    
    start = 0
    end = len(sorted_list)-1
    middle = int((start + end)/2)

    while not sorted_list[middle] == num and start < end:

        if sorted_list[middle] < num:
            #print("Number you are searching is on the right of middle element")
            start = middle + 1
            middle = int((start + end)/2)

        elif sorted_list[middle] > num:
            #print("Num you are searching is on the left of middle element")
            end = middle - 1
            middle = int((start + end)/2)

    if sorted_list[middle] == num:
        print(f"The num {num} was found at index {middle}.")

    elif sorted_list[middle] != num and start > end:
        print(f"The number {num} was not found in the given list.")


find_num(sorted_nums, 14)
