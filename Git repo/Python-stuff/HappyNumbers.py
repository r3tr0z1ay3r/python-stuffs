from function import handle_value_error


def happy_check(inp):
    n_list = [inp]
    if len(inp) == 2 or len(inp) > 2:
        n_list = []
        for i in inp:
            n_list.append(i)
    four_count = 0
    while True:
        sum_list = 0
        for i in n_list:
            int_i = int(i)
            sum_list += int_i ** 2
        total = sum_list
        if int(total) == 4:
            four_count += 1
        if total == 1:
            return True
        if four_count == 4:
            return False
        n_list = str(sum_list)


#Start of program

count = 1
happy_nums = []

while True:
    times = input("How many happy numbers do u want: ")
    if handle_value_error(times):
        times = handle_value_error(times)
        break


while len(happy_nums) != times:
    if happy_check(str(count)) == True:
        happy_nums.append(count)
    count += 1


print(f"The first {times} happy numbers are: {happy_nums}")
