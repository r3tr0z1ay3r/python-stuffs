import time
from BinarySearch import bin_search
strip = []
test = [4,3,6,5,1,4]
def insert_sort(test:list):
    for i in range(len(test)):
        if i == 0:
            continue
        if test[i] < test[i-1]:
            current = test[i] # assinging the value to check to a local variable
            elm_pos = bin_search(test,test[i]) # Search thro the list to get index of elm
            count = 0 
            check_list = test[0:elm_pos] # Create a list of elms before the elm
            for i in check_list[::-1]: #Compare the current with elms in inverse of the above list
                if current < i: 
                    count += 1 
            test.remove(current)
            test.insert(elm_pos-count,current)
    return test
print("The give list was: ",test)
print("The sorted list will be: ",insert_sort(test))