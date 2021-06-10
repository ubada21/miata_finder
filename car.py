import requests
from bs4 import BeautifulSoup
import settings as s
from datetime import datetime


class Car:
    def __init__(self, link):

        self.link_info = requests.get(link).text
        car_soup = BeautifulSoup(self.link_info, 'html.parser')
        car_attrbtgroup = car_soup.find_all(class_='attrgroup')
        car_attrs = str(car_attrbtgroup[1]).split('<span>')
        car_attributes = []

        for i in car_attrs:
            car_attributes.append(i.split(':'))

        car_attributes = car_attributes[1:]

        for j in car_attributes:
            if len(j) == 1:
                car_attributes.remove(j)

        for j in car_attributes:
            j[1] = j[1].split("<b>")[1].split("</b>")[0]

        makemodel = s.get_makemodel((car_soup.find_all(class_='attrgroup')))
        location = s.get_location(str(car_soup.find_all('head')))
        unfrmtdate = s.get_datetime(car_soup.find_all(class_='date timeago'))
        date = datetime.strptime(unfrmtdate, "%Y-%m-%d %H:%M")
        price = s.format_price(s.get_price(car_soup.find_all(class_='price')))
        listing = s.get_listing(str(car_soup.find_all('head')))
        clid = s.get_clid(str(car_soup.find_all(class_='postinginfo')))

        self.attrbt_dict = dict(car_attributes)

        self.attrbt_dict['url'] = link
        self.attrbt_dict['makemodel'] = makemodel
        self.attrbt_dict['location'] = location
        self.attrbt_dict['date'] = date
        self.attrbt_dict['price'] = price
        self.attrbt_dict['listing'] = listing
        self.attrbt_dict['clid'] = clid
