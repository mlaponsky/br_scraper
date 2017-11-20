from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://www.basketball-reference.com/'

def get_soup(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    return soup

def get_player_links():
    url = BASE_URL + 'leagues/NBA_2018_per_game.html'
    soup = get_soup(url)

    player_table = soup.find('table', {'id': 'per_game_stats'})
    players = player_table.find_all('td', {'data-stat': 'player'})
    player_links = [BASE_URL + p.find('a')['href'] for p in players]
    return player_links

def get_salaries(player_link):
    soup = get_soup(player_link)
    salaries_table = soup.find('table', {'id': 'all_salaries'})
    return soup.find('tbody')
