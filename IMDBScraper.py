from bs4 import BeautifulSoup
import requests, openpyxl
from requests.adapters import HTTPAdapter, Retry

excel = openpyxl.Workbook()
sheet = excel.activeSheet
sheet.title = 'Top Rated Movies'
sheet.append(['Movie Rank', 'Movie Name', 'Year of Releases', 'IMDB Rating'])

try:
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    url = 'https://www.imdb.com/chart/top/'
    
    source = session.get(url, headers=HEADERS)
    
    source.raise_for_status()
    
    soup = BeautifulSoup(source.text,'html.parser')
    
    movies = soup.find('tbody', class_="lister_list").find_all('tr')
    
    for movie in movies:
        name = movie.find('td', class_="titleColumn").a.text
        
        rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
        
        year = movie.find('td', class_="titleColumn").span.text.strip('()')
        
        rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
        
        sheet.append([rank, name, year, rating])
    
except Exception as e:
    print(e)
    
excel.save('IMDB Movie Ratings.xlsx')