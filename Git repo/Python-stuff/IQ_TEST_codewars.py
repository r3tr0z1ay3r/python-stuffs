import random
def iq_test(numbers:str):
    list = numbers.strip().split()
    list = [int(i) for i in list]
    odd_list = []
    even_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    if len(odd_list) == 1:
        to_check = odd_list[0]
    else:
        to_check = even_list[0]
    #Search through to find the element and return index of it
    for i in range(len(list)):
        if list[i] == to_check:
            return i+1

print(iq_test("2 4 7 8 10"))