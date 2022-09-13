from translate import Translator
class customError(Exception):
    pass
def translate(text,from_lang,to_lang):
    translator= Translator(from_lang=from_lang,to_lang=to_lang)
    translated = translator.translate(text)
    if "INVALID SOURCE LANGUAGE" in translated:
        raise customError("That language either doesnt exist or isnt supported!")
    return translated
    

