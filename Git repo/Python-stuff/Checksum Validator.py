from function import *
while True:
    a = input("Enter the account number: ")
    if handle_value_error(a):
        break
copy_a = list(a)
list_a = []
to_split = []
to_multiply = []
splitted = []
split = []
j = 0
k = 0

for i in a:
    list_a.append(i)

for i in range(0,len(a)):
    if i % 2 == 0:
        pass
    else:
        to_multiply.append(a[i])

for i in range(0,len(to_multiply)):
    to_multiply[i] = int(to_multiply[i]) * 2
#['9', '2', '3', '8', '1']
#[ 18 , 4 , 6 , 16 , 2]

for i in range(0,len(a)):
    if i % 2 == 0:
        pass
    else:
        list_a[i] = str(to_multiply[j])
        j+=1

for i in list_a:
    if len(i) > 1:
        to_split.append(i)
for i in to_split:
    splitted.append( i.split("1") )
for i in splitted:
    for j in i:
        if j == "":
            pass
        else:
            split.append(j)
for i in range(0,len(split)):
    sum = 1 + int(split[i])
    split[i] = sum
for i in range(0,len(list_a)):
    if len(list_a[i]) > 1:
        list_a[i] = split[k]
        k+=1
sum2 = 0
for i in list_a:
    sum2 += int(i)
total_sum = sum2 * 9
mod = total_sum % 10
copy_a.append(mod)
acct_no = copy_a
print(f"The check digit is {mod}")
print("The account number with the check digit attached will be:",*acct_no,end="")