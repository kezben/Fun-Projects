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
all_balls = []

#for link in end_urls:
for link in end_urls:
    current_link = (baseUrl + link)
    client2 = uo(current_link)
    webpage2 = client2.read()
    client2.close()
    webpage2_soup = soup(webpage2, "html.parser")
    extract_results = webpage2_soup.findAll("div", {"class":"row"})

    try:
        print(current_link)
        for lines in extract_results[1:]:
            balls = str(lines.select('ol')[0])
            for j in balls.split(">"):
                bum = [int(s) for s in j.split("<") if s.isdigit()]
                if bum:
                    all_balls.append(bum)
    except:
        pass

    while len(all_balls) > 0:
        b1.append(all_balls.pop(0))
        b2.append(all_balls.pop(0))
        b3.append(all_balls.pop(0))
        b4.append(all_balls.pop(0))
        b5.append(all_balls.pop(0))
        b6.append(all_balls.pop(0))
        bb.append(all_balls.pop(0))

def most_frequent(arr):
    frequency = {}
    for element in arr:
        element = str(element).strip("[]")
        element = int(element)
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1

    for key in sorted(frequency):
        return "%s" % (key)

def average(arr):
    sum = 0
    for element in arr:
        element = str(element).strip("[]")
        element = int(element)
        sum += element
    return round(sum / len(arr))

try:
    print("The most frequently occuring ball number 1 is", most_frequent(b1))
    print("The most frequently occuring ball number 2 is", most_frequent(b2))
    print("The most frequently occuring ball number 3 is", most_frequent(b3))
    print("The most frequently occuring ball number 4 is", most_frequent(b4))
    print("The most frequently occuring ball number 5 is", most_frequent(b5))
    print("The most frequently occuring ball number 6 is", most_frequent(b6))
    print("The most frequently occuring bonus ball number is", most_frequent(bb))
except:
    pass

try:
    print("The average ball for number 1 is", round(average(b1)))
    print("The average ball for number 2 is", round(average(b2)))
    print("The average ball for number 3 is", round(average(b3)))
    print("The average ball for number 4 is", round(average(b4)))
    print("The average ball for number 5 is", round(average(b5)))
    print("The average ball for number 6 is", round(average(b6)))
    print("The average bonus ball is", round(average(bb)))
except:
    pass
