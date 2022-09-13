# 0 1 1 2 3 5 8
while True:
    try:
        n = int(input("Enter a value to generate fibo seq upto: "))
        break
    except ValueError:
        print("Please enter a number!")
fibo_seq = [0]
a = 0
b = 1
for i in range(1,n):
    c = a + b
    fibo_seq.append(c)
    a = b
    b = c
    if i == n:
        break
print(fibo_seq)