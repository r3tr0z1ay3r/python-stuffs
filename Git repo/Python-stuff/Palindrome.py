"""
Reverse a word provide and compare with original to check if palindrome
"""
print("\t\tTHIS PROGRAM WILL CHECK IF THE GIVEN WORD IS A PALINDROME!")
inp = input("\tEnter the word: ")
inp_lower = inp.lower()
inp_rev = ""
for i in inp_lower[::-1]:
    inp_rev += i
if inp_rev == inp_lower:
    print("\tThe given word is a palindrome!")
else:
    print("\tThe given word is not a palindrome!")