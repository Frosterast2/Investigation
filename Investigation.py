import googlesearch
import requests
from bs4 import BeautifulSoup as bs4
import webbrowser

def investigate(search_word, web_search="Ufo"):
    """investigate(search_word, web_search) -> Searches google based on the search_word, iterates through the resuls and searches for the string web_search in each website.
       Arguments:
            search_word: KeyWord to search on google
            web_search: Keyword to search in every website found
    """

    
    search = googlesearch.search(search_word, tld="com", lang="en", num=10, start=0, stop=10)
    results2 = []
    results3 = []
    results4 = []
    results5 = []
    for i in search:
        try:
            results = requests.get(i)
            results = bs4(results.content,"html.parser")
            result = results.find_all(text=web_search.lower())
            result2 = results.find_all(text=web_search.upper())
            result3 = results.find_all(text=web_search)
            if result != []:
                results2.append(i)
            if result2 != []:
                results2.append(i)
            if result3 != []:
                results2.append(i)
        except:
            pass
    
    search = googlesearch.search(web_search, tld="com", lang="en", num=10, start=0, stop=10)
    for i in search:
        try:
            results = requests.get(i)
            results = bs4(results.content,"html.parser")
            result = results.find_all(text=search_word.lower())
            result2 = results.find_all(text=search_word.upper())
            result3 = results.find_all(text=search_word)
            if result != []:
                results3.append(i)
            if result2 != []:
                results3.append(i)
            if result3 != []:
                results3.append(i)
        except:
            pass

    search = googlesearch.search(search_word, tld="com", lang="en", num=10, start=0, stop=10)
    for i in search:
        try:
            results = requests.get(i)
            results = bs4(results.content,"html.parser")
            result = results.find_all(text=search_word.lower())
            result2 = results.find_all(text=search_word.upper())
            result3 = results.find_all(text=search_word)
            if result != []:
                results4.append(i)
            if result2 != []:
                results4.append(i)
            if result3 != []:
                results4.append(i)
        except:
            pass

    search = googlesearch.search(web_search, tld="com", lang="en", num=10, start=0, stop=10)
    for i in search:
        
        try:
            results = requests.get(i)
            results = bs4(results.content,"html.parser")
            result = results.find_all(text=web_search.lower())
            result2 = results.find_all(text=web_search.upper())
            result3 = results.find_all(text=web_search)
            if result != []:
                results5.append(i)
            if result2 != []:
                results5.append(i)
            if result3 != []:
                results5.append(i)
        except:
            pass
    return [results2, results3, results4, results5]

#In this example, I'm taking Ufo

print(investigate("Ufo", "ufo"))