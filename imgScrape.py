# Library used to create file directory
import os

# Libraries used to web scrape
import urllib
from urllib.request import Request, urlopen
import requests

# Library used to format what has been scraped
from bs4 import BeautifulSoup

# Lists used to store user input
nouns = []
adjectives = []
describers = []

# Noun user input
nounUserInputComplete = False
nounInput = input("Tell me what you want to scrape: ")
nouns.append(nounInput)
print("Enter multiple words similar to what you want to scrape. For example, if your word was trees type forest (Type e to end): ")
print("Best Results if you input 5 similar words")
while nounUserInputComplete == False:
    nounInput = input("")
    if (nounInput == "e"):
        nounUserInputComplete = True
    else:
        nouns.append(nounInput)

# Adjective user input
adjUserInputComplete = False
print("Enter multiple adjectives which describe what you want to scrape, for example big, small (Type e to end):")
while adjUserInputComplete == False:
    adjInput = input("")
    if (adjInput == "e"):
        adjUserInputComplete = True
    else:
        adjectives.append(adjInput)

# Describer user input
descUserInputComplete = False
print("Enter multiple describers which may define what you want to scrape, these should be more unique and descriptive than the former.  (Type e to end):")
while descUserInputComplete == False:
    descInput = input("")
    if (descInput == "e"):
        descUserInputComplete = True
    else:
        describers.append(descInput)


# Triple nested for loop used to build the list of search urls
searchList = []
for noun in range(len(nouns)):
    search = nouns[noun]
    search = "https://www.google.com/search?q=" + search + "&sxsrf=ALeKk0348sanMpqKWP6QTpvsftCG1-pD3g:1624207489297&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjSksOz1KbxAhUlA2MBHcjtBBAQ_AUoAXoECAEQAw&biw=952&bih=999"
    searchList.append(search)
 
    for adjective in range(len(adjectives)):
        search = adjectives[adjective] + "+" + nouns[noun]
        search = "https://www.google.com/search?q=" + search + "&sxsrf=ALeKk0348sanMpqKWP6QTpvsftCG1-pD3g:1624207489297&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjSksOz1KbxAhUlA2MBHcjtBBAQ_AUoAXoECAEQAw&biw=952&bih=999"
        searchList.append(search)

        for describer in range(len(describers)):
            search = describers[describer] + "+" + adjectives[adjective] + "+" + nouns[noun]
            search = "https://www.google.com/search?q=" + search + "&sxsrf=ALeKk0348sanMpqKWP6QTpvsftCG1-pD3g:1624207489297&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjSksOz1KbxAhUlA2MBHcjtBBAQ_AUoAXoECAEQAw&biw=952&bih=999"
            searchList.append(search)

# Makes folder where files will be stored with relevant name
if(os.path.isdir(nouns[0]) == False):
    os.mkdir(nouns[0])

# Nested for loop which scrapes all the images on the page, and then downloads all the images individually into the folder
imgSearchSaveCount = 0
for search in range(len(searchList)):

    # Retrieves the next search URL
    url = searchList[search]

    # Goes to the webpage through a given 'agent'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    # Reads the webpage
    web_byte = urlopen(req, timeout=10).read()

    # Decodes the webpage
    webpage = web_byte.decode('utf-8')

    # Formats the webpage
    soup = BeautifulSoup(webpage, 'html.parser')

    # Retrieves all images on the webpage
    images = soup.find_all('img')

    # For loop which downloads all the images found on the webpage
    for item in images:
        # Try and except is necessary to handle a number of impossible to predict errors
        try:
            # Generating Image Name
            imgName = str(imgSearchSaveCount) + ".jpg"

            # Getting Image
            imgResponse = requests.get(item['src'])

            # Writing Image to File
            image = open(nouns[0]+ "/" +imgName, "wb")
            image.write(imgResponse.content)

            # Ending Process
            image.close()
            imgSearchSaveCount += 1
            print("Image Process Success")

        except:
            # Generic failure statement, usually irrelevant
            print("Image Process Error")
