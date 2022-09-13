import requests
import bs4
import time


def all_words():
    english_words = []
    url = "https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/"

    request = requests.get(url)
    soup = bs4.BeautifulSoup(request.content,"lxml")
    word =soup.prettify()
    word2 = list(soup.find_all("p"))
    for i in (word2[len(word2)-1]):
        if  str(i).isalpha():
            english_words.append(i)
    return(english_words)
