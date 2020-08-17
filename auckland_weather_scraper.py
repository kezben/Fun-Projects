import requests
from bs4 import BeautifulSoup as bs

# gets page
page = requests.get('https://www.weatherwatch.co.nz/forecasts/Auckland')

# parses webpage as html
soup = bs(page.content, 'html.parser')
current_week = soup.find(class_='jsx-2427370272 forecast extended')

# scrape all data containing weather info
data = current_week.find_all(class_='jsx-462560009')

#get list of date, description, day temp & night temp
dates = [datapoint.find(span, class_='jsx-462560009 grid-width-10 date cell desktop') for datapoint in data]

print(dates)
