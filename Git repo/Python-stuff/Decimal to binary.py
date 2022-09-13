def bin_to_dec(a:str):
    #(101)₂ = (1 × 2²) + (0 × 2¹) + (1 × 2⁰) = (5)₁₀
    final = 0
    length = len(a)
    str_sub = -1
    power = 0
    for i in range(0, length):
        current_powered = int(2 ** power)
        current_str_variable = int(a[str_sub])
        final += int(current_powered * current_str_variable)
        str_sub -= 1
        power += 1
    print(f"The decimal value of the binary value {a} is {final}!")

def dec_to_bin(a:str):
    b = int(a)
    final = []
    while b != 0:
        b = b // 2
        final.append(b % 2)
    print(f"The binary value {a} in decimal will be")
    print(*final,sep="")

print("Welcome to this program! \n You are asked to choose either to convert decimal to binary or vice versa \n")
while True:
    choice=input("Type bd for binary to decimal or db for decimal to binary: ")
    if choice == "bd":
        binary = input("Please enter the binary value: ")
        bin_to_dec(binary)
        break
    elif choice == "db":
        decimal = input("Please enter the decimal value: ")
        dec_to_bin(decimal)
        break
    else:
        print("Please enter *bd* or *db* !!")
    #divide the number by 2 until u get 0 and then the remainders in reverse is the required binary
