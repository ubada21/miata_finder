import requests
from bs4 import BeautifulSoup
import re
import settings


class Car:
    def __init__(self, link):

        self.link_info = requests.get(link).text
        car_soup =  BeautifulSoup(self.link_info, 'html.parser')
        car_attrgroup = car_soup.find_all(class_='attrgroup')
        car_attrs = str(car_attrgroup[1]).split('<span>')
        car_attributes = []
        for i in car_attrs:
            car_attributes.append(i.split(':'))

        car_attributes = car_attributes[1:]

        for j in car_attributes:
            if len(j) == 1:
                car_attributes.remove(j)

        for j in car_attributes:
            j[1] = j[1].split("<b>")[1].split("</b>")[0]

        makemodel = settings.get_makemodel((car_soup.find_all(class_='attrgroup')))
        location = settings.get_location(str(car_soup.find_all('head')))
        date = settings.get_datetime(car_soup.find_all(class_='date timeago'))
        price = settings.get_price(car_soup.find_all(class_='price'))
        listing = settings.get_listing(str(car_soup.find_all('head')))

        attrbt_dict = dict(car_attributes)

        attrbt_dict['url'] = link
        attrbt_dict['makemodel'] = makemodel
        attrbt_dict['location'] = location
        attrbt_dict['date'] = date
        attrbt_dict['price'] = price
        attrbt_dict['listing title'] = listing

        self.listing = attrbt_dict['listing title']
        self.date = attrbt_dict['date']
        self.url = attrbt_dict['url']
        self.makemodel = attrbt_dict['makemodel']
        self.price = attrbt_dict['price']
        self.location = attrbt_dict['location']
        self.fuel = attrbt_dict['fuel']
        self.odometer = attrbt_dict['odometer']
        self.title_status = attrbt_dict['title status']
        self.transmission = attrbt_dict['transmission']
