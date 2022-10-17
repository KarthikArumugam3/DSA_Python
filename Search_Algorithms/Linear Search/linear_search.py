# Linear Search
# T.C. Best case :- O(1) - Constant time
#      Worst case:- O(n)
from datetime import datetime

cars = [4,3,2,7,6,9,1]

def find_car(current_parking, current_car):
    my_car = current_car

    for i in current_parking:
        if i == current_car:
            print(f"\nFound the car at position: {current_parking.index(i)+1}")
            break

        else:
            #print(f"car not found at position: {current_parking.index(i)+1}")
            pass


start = datetime.now()
find_car(cars, 7)
end = datetime.now()

time_difference = end - start

print("Time taken :: ",time_difference.total_seconds()," seconds")