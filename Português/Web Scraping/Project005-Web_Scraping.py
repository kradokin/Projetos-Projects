# I take no responsibility for what others do with the code, I do not advise for insane scraping (basically dosing)
# websites and it's posted as a learning exercise.
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


def movies_imdb_charts(url_imdb):
    get_link = url_imdb.text
    link_parser = BeautifulSoup(get_link, 'html.parser')
    name_movie = link_parser.find_all('td', {'class': 'titleColumn'})
    year_movie = link_parser.find_all('span', {'class': 'secondaryInfo'})

    # name_each_soup = soup_service.find_all('td', {'class': re.compile('str.+str')})
    # print(name_each_soup[0].contents[1].text)
    list_overall = []

    for title, year in zip(name_movie, year_movie):
        name_title = title.find('a').text
        released_year = title.find('span').text
        list_overall.append((name_title, released_year))
        # print(f'{name_title:<30}{year_release:>4}')
    df_movies = pd.DataFrame(list_overall, columns=['Title', 'Release Date'])
    return print(df_movies)


movies_imdb_charts(requests.get('https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1'))
