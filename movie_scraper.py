import urllib2
import movie
from bs4 import BeautifulSoup

class Movie_Scrapper
    def Scrape_Movies():
        page = urllib2.urlopen('http://www.boxofficemojo.com/seasonal/?view=releasedate&yr=2015&season=Summer')
        soup = BeautifulSoup(page.read(), 'html.parser')
        rows = soup.select('table[bgcolor="#ffffff"] tr')
                
        movies = []                
                
        for i in range(2, len(rows) - 4, 1):
            rank = rows[i].find_all('td')[0].font.get_text()
            title = ""
            if(rows[i].find_all('td')[1].b.font.a != None):
                title = rows[i].find_all('td')[1].b.font.a.get_text()
            else:
                title = rows[i].find_all('td')[1].b.font.get_text()
            amount = rows[i].find_all('td')[3].font.get_text()
            movie = Movie(rank, title, amount)
            movies.append(movie);
            
    movie.print_me()
    print '\n'

# print(soup.prettify())