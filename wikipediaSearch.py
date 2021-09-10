#wikipediaSearch

import wikipedia  # pip install wikipedia

try:
    search = input("Search Wikipedia: ")  # what to 'search'?
    search = search.replace("wikipedia", "")  # if wikipedia present in search then replace it with nothing.
    result = wikipedia.summary(search, sentences=2)  # extracting the summary from wikipedia, sentences means the number of sentences to be print. 
    print(result)  # printing the result.
except:
    print("No available page related to the 'search' on wikipedia.")

"""
Tips:
You can use this with your Python Projects like an Assistant to extract data from wikipedia. 
"""