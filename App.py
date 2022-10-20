import requests
from bs4 import BeautifulSoup as bs
import csv
import datetime
# private engg in karnataka
private_engg_in_kntka = 'https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india?state=Karnataka&ownership=Private&degree=B.E%20/B.Tech&branch=Computer%20Science%20Engineering&page='
URL = 'https://engineering.careers360.com/colleges/list-of-computer-science-engineering-colleges-in-karnataka?sort=popularity&page='
URL = 'https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india?state=Karnataka&ownership=Public/Government&degree=B.E%20/B.Tech&branch=Computer%20Science%20Engineering'
prvt_bsc_cs_kt = 'https://university.careers360.com/colleges/list-of-bsc-in-computer-science-degree-colleges-in-karnataka'
grvnt_btech_clg = 'https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india?state=Maharashtra&ownership=Public/Government&degree=B.E%20/B.Tech&branch=Computer%20Science%20Engineering'
prvt_btech_college_mh = 'https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india?state=Maharashtra&ownership=Private&degree=B.E%20/B.Tech&branch=Computer%20Science%20Engineering&page='
prvt_bsc_cs_mh = 'https://university.careers360.com/colleges/list-of-bsc-in-computer-science-degree-colleges-in-maharashtra?ownership=Private&page='
count = 1

# for page in range(1, 6):
#     req = requests.get(URL + str(page))
#     soup = bs(req.content, 'html.parser')

#     titles = soup.find_all('div', attrs={'class', 'c-entry-box--compact__body'})
#     titles_list = []

# page = 1
for page in range(1,6):
    req = requests.get(prvt_bsc_cs_mh + str(page))
    # req = requests.get(grvnt_btech_clg)
    soup = bs(req.content, 'html.parser')
    # titles = soup.find_all('div', attrs={'class', 'c-entry-box--compact__body'})
    titles = soup.find_all('div',attrs={'class','content'})
    titles_list = []
    # print(titles)
        # print(soup)
        
        # for i in titles:
        #     if i.find("a") is not None:
        #         # print(i.find("a").get('href'))
        #         pass
        # # for link in titles.find_all('a',attrs={'href': re.compile("^https://")}):
        # # # display the actual urls
        # #     print(link.get('href'))  



    for title in titles:
        d = {}
        # d['id'] = count
        d['College name'] = title.find('h2').text
        # d['desc'] = title.find('ul').text
        
        count += 1
        titles_list.append(d)
        # print(titles_list)

    print(titles_list)
    # filename = str("page "+str(page)+".csv")
    filename = str("result"+".csv")
    with open(filename, 'a', newline='') as f:
        w = csv.DictWriter(f,['College name',])
        # w.writeheader()
        w.writerows(titles_list)


