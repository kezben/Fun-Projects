from urllib.request import urlopen as uo
from bs4 import BeautifulSoup as soup

# make scraper appear to website as a legitimate browser
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = "http://lottoresults.co.nz/lotto/archive"

# open conncetions, read NZ Lotto archive webpage, close connection
client = uo(url)
webpage = client.read()
client.close()

# html parsing
webpage_soup = soup(webpage, "html.parser")

# grabs each month from each year
all_months = webpage_soup.findAll("div", {"class":"archive-box"})


month = all_months[0].findAll("a", {"href":"/lotto/august-2020"})

print(all_months)
print(month)
