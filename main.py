from bs4 import BeautifulSoup
import requests

try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()#raise a status error if any is found
    
    soup = BeautifulSoup(source.txt, 'html.parser')#source.txt returns the html content of the webpage
    
    movies = soup.find('tbody', class_='lister-list').find_all('tr')
    
    for movie in movies:
        name = movie.find('td', class_='titleColumn').a.text
        
        rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
        
        year = movie.find('td', class_='titleColumn').span.text.strip('{}')
        
        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
        
        print(rank,name,rating,year)
        
    
except Exception as e:
    print (e)