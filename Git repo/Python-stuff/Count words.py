"""
Count words from a string
"""
print("\t\tTHIS PROGRAM WILL COUNT THE NUMBERS OF WORDS IN THE SETENCE PROVIDED!")
str = input("\tEnter a string: ")
str_split = str.split(" ")
str_count = 0
for i in str_split:
    print(i)
    if i.isdigit() == True:
        pass
    str_count+=1
print(f"The number of words in the string provide is: {str_count}")