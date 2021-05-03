from car import Car
from bs4 import BeautifulSoup
import requests

"""
city = input("Enter City: ")
model = input("Enter Car Model: ")
trans = input("Enter transmission (auto or manual, else, leave empty): ")
max_yr = str(input("Max year (or leave empty): "))
min_yr = str(input("Min year (or leave empty): "))
max_km = str(input("Max KM (or leave empty): "))

if trans == 'auto':
    trans = 0
elif trans == 'manual':
    trans = 1

 craigs_link = "https://" + city + ".craigslist.org/search/rds/cto?" \
                                  "query=" + model + "&" \
                                  "&min_auto_year=" + min_yr + "&" \
                                  "max_auto_year=" + max_yr +"&" \
                                  "min_auto_miles=0&" \
                                  "max_auto_miles=" + max_km +"&" \
                                  "auto_transmission=" + str(trans)"""

craigs_link = "https://vancouver.craigslist.org/search/cto?query=c63&" \
              "purveyor-input=owner"

page = requests.get(craigs_link).text

soup = BeautifulSoup(page, 'html.parser')

links = soup.find_all('a')
links_only = []
for link in links:
    links_only.append(link.get('href'))

all_links = []
for link in links_only:
    if "https" in link and '.html' in link:
        all_links.append(link)

all_links = list(dict.fromkeys(all_links))

car_list = []

for link in all_links:
    car = Car(link)
    car_list.append(car)


for car1 in car_list:
    print(car1.listing)
    print('date posted: ' + str(car1.date))
    print('URL: ' + car1.url)
    print('Make/Model: ' + car1.makemodel)
    print('Price: ' + str(car1.price))
    print('Location: ' + car1.location)
    print('Fuel Type: ' + car1.fuel)
    print('Odometer: ' + str(car1.odometer) + " Km")
    print('Title: ' + car1.title_status)
    print('Transmission: ' + car1.transmission)
    print('\n')

