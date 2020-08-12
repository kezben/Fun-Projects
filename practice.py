import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com/")

if result.status_code != 200:
    print("The page cannot be loaded. Check that the url used is correct")

webpage = result.content

soup = BeautifulSoup(webpage, "lxml")

links = soup.find_all("a")

for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])
