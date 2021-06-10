from car import Car
from bs4 import BeautifulSoup
import requests
from discord import Webhook, RequestsWebhookAdapter

webhook = Webhook.from_url("INSERT DISCORD WEBHOOK HERE",
                           adapter=RequestsWebhookAdapter())

seen_links = []
# change these parameters to the desired search
city = "vancouver"
model = "miata"
trans = "manual"  # for automatic transmission, use 'auto'
max_yr = "2004"
min_yr = "1996"
max_km = "250000"


def trans_frmt(tran):
    if tran == 'auto':
        return "auto_transmission=2&"
    elif tran == 'manual':
        return "auto_transmission=1&"
    else:
        pass


def format_car(car):
    desc = "{0} | {1} | {2} | {3} | {4} | {5} | {6} " \
           " ".format('**' + car.attrbt_dict["makemodel"] + '**', '$' +
                      str(car.attrbt_dict["price"]),
                      car.attrbt_dict["odometer"] + ' km',
                      car.attrbt_dict["location"],
                      car.attrbt_dict["transmission"],
                      car.attrbt_dict["url"], car.attrbt_dict["listing"])
    return desc


def scrape_link(carlink):

    page = requests.get(carlink).text
    soup = BeautifulSoup(page, 'html.parser')
    links = soup.find_all('a')
    links_only = []
    all_links = []
    car_list = []

    for link in links:
        links_only.append(link.get('href'))

    for link in links_only:
        if "https" in link and '.html' in link:
            all_links.append(link)

    all_links = list(dict.fromkeys(all_links))

    for link in all_links:
        car = Car(link)
        if car.attrbt_dict["listing"] == 'preview':
            pass
        else:
            car_list.append(car)

    for car in car_list:
        if car.attrbt_dict['url'] in seen_links:
            pass
        else:
            webhook.send(format_car(car))
            seen_links.append(car.attrbt_dict['url'])


def get_location(lctn):
    if len(lctn.split('<meta')) == 15:
        return lctn.split('<meta')[13].split('"')[1]
    else:
        return lctn.split('<meta')[14].split('"')[1]


def get_listing(lstng):
    if len(lstng.split('<meta')) == 15:
        return lstng.split('<meta')[5].split('"')[1].split('-')[0]
    else:
        return lstng.split('<meta')[6].split('"')[1].split('-')[0]


def get_price(prc):
    return str(prc[0]).split('<span class='
                             '"price">')[1].split('</span>')[0].split('$')[1]


def format_price(prc):
    return prc.replace(",", "")


def get_datetime(dttm):
    return str(dttm[1]).split('<')[-2].split('>')[1]


def get_makemodel(mkmdl):
    return str(mkmdl[0]).split('<span>')[1].split('<b>')[1].split('</b>')[0]


def get_clid(clid):
    return str(clid).split('post id: ')[1].split('</p>')[0]


craigs_link = "http://" + city + ".craigslist.org/d/cars-trucks-by-owner/" \
                                 "search/cto?" + trans_frmt(trans) + \
              "max_auto_miles=" + max_km + "&max_auto_year=" + max_yr + \
              "&min_auto_year=" + min_yr + "&query=" + model + "&sort=date"
