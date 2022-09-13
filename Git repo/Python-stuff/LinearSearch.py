#Binary Search
from function import *

#FUNCTION FOR SEARCHING THROUGH LIST
def bin_search(list:list,to_find):
    found = False
    index = 0
    for i in list:
        if i == to_find:
            found = True
            break
        else:
            pass
        index += 1
    if found == False:
        #print("A match cannot be found in the given list!")
        pass
    if found == True:
        #print(f"Match found at index {index}")
        return index


#START OF PROGRAM

list = []
to_search = 0