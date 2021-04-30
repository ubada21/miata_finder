from link import Car
from bs4 import BeautifulSoup
import requests
import html.parser
import re
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

craigs_link = 'https://vancouver.craigslist.org/search/cta?query=850i&purveyor-input=all'
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
print(all_links)

print(len(all_links))

link = all_links[0]

car_link = requests.get(link).text
car_soup = BeautifulSoup(car_link, 'html.parser')
# print(car_soup)

car_links = car_soup.find_all(class_='attrgroup')
#print(car_links)

#car_attr = car_links[1]
#car_attrs = str(car_attr).split("<span>")
#car_attributes = []
#for link in car_attrs:
#    car_attributes.append(link.split(':'))

#car_attributes = car_attributes[1:]

#for attrbt in car_attributes:
#    attrbt[1] = attrbt[1].split("<b>")[1].split("</b>")[0]

car_attributes2 = []

for link in all_links:
    link = BeautifulSoup(requests.get(link).text, 'html.parser').find_all(class_='attrgroup')
    link = str(link).split('<span>')
    for l in link:
        l = l.split(':')
    #    #car_attributes2.append(l)
    car_attributes2.append(link)
car_attributes3 = []
car_attributes5 = []

for i in car_attributes2:
    car_attributes3.append(i)


for i in car_attributes3:
    for item in range(len(i)):
        i[item] = i[item].split(':')


dict1 = []

for i in car_attributes3:
    cardict = dict(i[2:])
    dict1.append(cardict)

print(dict1)
#print(attr_dict)


# make class with each individual link, all formatting happens within class?
cars = []
#for link in all_links:
#    car = Car(link)
#    cars.append(car)

car1 = Car(all_links[0])

print(car1.car_attributes)