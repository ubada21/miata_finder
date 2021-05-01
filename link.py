import requests
from bs4 import BeautifulSoup


class Car:
    def __init__(self, link):

        self.link = link
        self.title = 'hello'
        link_info = requests.get(link).text
        car_soup = BeautifulSoup(link_info, 'html.parser').find_all(class_='attrgroup')
        car_title = car_soup[0]
        car_attr = car_soup[1]
        car_attrs = str(car_attr).split('<span>')
        car_attributes = []
        for i in car_attrs:
            car_attributes.append(i.split(':'))

        self.car_attributes = car_attributes[1:]

        for j in self.car_attributes:
            if len(j) == 1:
                self.car_attributes.remove(j)

        for j in self.car_attributes:
            j[1] = j[1].split("<b>")[1].split("</b>")[0]


        self.title = str(car_title).split('<span>')[1].split('<b>')[1].split('</b>')[0]
        self.attrbt_dict = dict(self.car_attributes)

        self.fuel = self.attrbt_dict['fuel']
        self.odometer = self.attrbt_dict['odometer']
        self.title_status = self.attrbt_dict['title status']
        self.transmission = self.attrbt_dict['transmission']

















