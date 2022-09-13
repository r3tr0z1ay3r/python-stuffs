word="The quick brown fox jumps over the lazy dog"
def pangram(a:str):
    no_space = a.replace(" ", "")
    set1 = set(no_space)
    import string
    set2 = set(string.ascii_letters)
    return set1.issubset(set2)
print(pangram(word))
