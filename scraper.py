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

# open connections, read NZ Lotto archive webpage, close connection
client = uo(url)
webpage = client.read()
client.close()

# html parsing
webpage_soup = soup(webpage, "html.parser")

# grabs url for every month in every year and appends to an array
extract_months = webpage_soup.findAll("ul", {"class":""})
all_months = str(extract_months)
end_urls = []
i = 1
for month in all_months.split('"'):
    if (i % 2 == 0):
        end_urls.append(month)
    i+=1

# base url with each month added links to each results page
baseUrl = "http://lottoresults.co.nz"

# arrays for each ball, bonus ball & power ball
b1, b2, b3, b4, b5, b6 = [], [], [], [], [], []
bb = []
pb = []

#for link in end_urls:
current_link = (baseUrl + end_urls[0])
client2 = uo(current_link)
webpage2 = client2.read()
client2.close()
webpage2_soup = soup(webpage2, "html.parser")
