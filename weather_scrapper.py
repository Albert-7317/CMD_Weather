import requests
from bs4 import BeautifulSoup

URL = 'https://www.bbc.co.uk/weather/2643743'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

result_temp = soup.find("div", {"class":"wr-value--temperature gel-trafalgar"})

current_temp = result_temp.find("span", {"class":"wr-hide-visually"}).text

current_condition = soup.find("div", {"class":"wr-weather-type__text"}).text

print(current_condition)
print(current_temimport requests
from bs4 import BeautifulSoup

URL = 'https://www.bbc.co.uk/weather/2643743'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

result_temp = soup.find("div", {"class":"wr-value--temperature gel-trafalgar"})

current_temp = result_temp.find("span", {"class":"wr-hide-visually"}).text

current_condition = soup.find("div", {"class":"wr-weather-type__text"}).text

print(current_condition)
print(current_tem
