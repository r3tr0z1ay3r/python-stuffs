Rot13 = {"A":"N","B":"O","C":"P","D":"Q","E":"R","F":"S","G":"T","H":"U","I":"V","J":"W","K":"X","L":"Y","M":"Z",
         "a":"n","b":"o","c":"p","d":"q","e":"r","f":"s","g":"t","h":"u","i":"v","j":"w","k":"x","l":"y","m":"z"}


def rot13(message):
    encrypted = ""
    for i in message:
        if not i.isalpha():
            encrypted += i
        if i in Rot13.keys():
            encrypted += Rot13.get(i)
        if i in Rot13.values():
            for key,value in Rot13.items():
                if i == value:
                    encrypted += key
    return encrypted

print(rot13("Test"))