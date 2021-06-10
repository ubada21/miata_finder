# miata_finder
A simple program to help me find a miata.

The idea was to make a program that would alert me everytime a new car was posted on craigslist matching my search. It was implemented using BeautifulSoup
for the web scraping portion, and a discord webhook for the alert system. It runs continously and re-scrapes the craigslist page every 10 minutes.

It scrapes craigslist for the car that I want (which can be changed in the settings.py file) and posts the results it finds to a discord channel.
The discord channel can be setup using a webhook, and if this program is allowed to run continously, it will re-scrape the craigslist page every 10 minutes.
It will post whatever new listings it finds to the discord channel, which then alerts the user.

The parameters can be changed to search for any car in any city.
