"""
Get a string from user and count the number of vowels in it
"""
print("\t\tTHIS PROGRAM WILL COUNT THE NO OF VOWELS IN THE SETENCE PROVIDED!")
usr_inp = input("\tEnter a sentence: ")
split = usr_inp.split(" ")
vowel_count = 0
for i in split:
    if i.isdigit() == True:
        continue
    if "a" or "e" or "i" or "o" or "u" in i.lower():
        vowel_count+=1
        print(f"There is a vowel in {i}")
print(f"The number of vowels in the setence provided is {vowel_count}")
