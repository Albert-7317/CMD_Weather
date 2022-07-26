import requests
from bs4 import BeautifulSoup

URL = 'https://www.bbc.co.uk/weather/2643743'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

result_temp = soup.find("div", {"class":"wr-value--temperature gel-trafalgar"})

current_temp = result_temp.find("span", {"class":"wr-hide-visually"}).text

current_condition = soup.find("div", {"class":"wr-weather-type__text"}).text

result_location = soup.find("div", {"id":"wr-forecast"})

current_location = result_location.find("h1", {"id":"wr-location-name-id"}).text

print("-------------------------------------------------------------|")
print("| your curent location is: ",current_location)
print("-------------------------------------------------------------|")
print("| The current conditions are: ",current_condition)
print("-------------------------------------------------------------|")
print("| and the current temprature is: ",current_temp)
print("-------------------------------------------------------------|")
print("          ,$Y$$$$Y$")
print("         $$,   ,+$P,")
print("        $,      $Y,")
print("        Y,                 $$,")
print("      , ,Y,                $Y+%PYYY$$$$$Y,,")
print("    ,$Y$..$$,,,,  ,,,$+Y$$$$$Y%+,,,   ,,+P$$$$,")
print("    ,Y,,   ,,,$YYYYY$$YPY,,,            ,$Y  ,$+Y$,")
print("     ,,$$$,,,,,,        ,,$$$$$$,         ,  ,,+$,$$$")
print("                              ,$Y$,,           $$  ,YY")
print("                                 ,$$$$$,       $,  ,Y*,")
print("                                     ,,$Y$Y$       $Y,+,")
print("                                         ,,Y$,     , ,%,")
print("                                          $Y++,     ,YP$")
print("                                         ,PP+$$,,   ,,+,")
print("                                         ,YPPY+Y$,  ,+Y")
print("                                 YPP,,     $,$+,    $+")
print("                                 YYP$++,   ,$Y$,  ,$+,")
print("                                  $$Y,Y+Y$$$$$, ,$Y$")
print("                                   ,$$,,$$$,,,$$,,")
