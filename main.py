from bs4 import BeautifulSoup
import requests

try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()#raise a status error if any is found
    
    soup = BeautifulSoup(source.txt, 'html.parser')#source.txt returns the html content of the webpage
    print(soup)
except Exception as e:
    print (e)