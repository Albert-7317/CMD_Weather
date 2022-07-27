import requests
from bs4 import BeautifulSoup
from art import *

URL = 'https://www.bbc.co.uk/weather/2643743'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

result_temp = soup.find("div", {"class":"wr-value--temperature gel-trafalgar"})

current_temp = result_temp.find("span", {"class":"wr-hide-visually"}).text

###need to go and het these things as variables###

range_of_temprtures = 0 #some notes ot help later // div class = wr-time-slot-list__item wr-time-slot-list__item--time-slots
                        # thisll give the div with all the different temps

current_humidity = 0



current_condition = soup.find("div", {"class":"wr-weather-type__text"}).text

result_location = soup.find("div", {"id":"wr-forecast"})

current_location = result_location.find("h1", {"id":"wr-location-name-id"}).text

print('you are currently in:')
tprint(current_location.split(" ")[0])
print("    _________", "     ___________________________________")
print("   / /  /  XD", "   < the conditions are: ", current_condition, " |")
print("  /  |  |    /", "    \ the humidity is: ", current_humidity, " |")
print(" /          /", "      ----------------------------------")
print(" |   ||//\/")
print(" |  /  \//")
print("  \ |")
print("  /|")
print("  |\ ")
print('Current Temprature is:')
tprint(current_temp)
