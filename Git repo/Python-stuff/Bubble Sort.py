#BUBBLE SORT
"""
Take elemnts in pair, Compare them
if not in order
switch
else
pass to the next pair
repeat till the whole list in order
"""
import time
print("\t\tTHIS PROGRAM WILL SORT A LIST USING BUBBLE SORT METHOD!")
list=[]
while True:
    try:
        no_elms = int(input("\tNumber of elements to add to list: "))
        break
    except:
        print("Please enter a valid number!")
for i in range(1,no_elms+1):
    while True:
        try:
            list_elm = int(input(f"Enter elemnt number {i} to add: "))
            list.append(list_elm)
            break
        except:
            print("Please enter a number to add to the list!")
list_sorted = list.copy()
list_sorted.sort()
i = 0
print("\t Sorting the list...")
time.sleep(1)
while True:
        for i in range(0,len(list)):
            try:
                if list[i] > list[i+1]:
                    list[i],list[i+1] = list[i+1],list[i]
                else:
                    a = (f"{list[i]} is smaller than {list[i+1]}")
            except IndexError:
                break
        if list == list_sorted:
            print(f"{list}  is the sorted version of the list provided!")
            print("Ending the algorithm...")
            break
