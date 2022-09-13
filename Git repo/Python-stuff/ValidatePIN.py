import re
def validate_pin(pin):
    #return true or false
    pattern = "^\d{4}$"
    pattern1 = "^\d{6}"
    final = False
    if re.search(pattern,pin):
        final = True
    if re.search(pattern1,pin):
        final = True
    return final

print(validate_pin('1234'))