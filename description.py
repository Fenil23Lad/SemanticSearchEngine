import requests
from bs4 import BeautifulSoup

def getrec():
    key = "Paneer"
    url = "http://allrecipes.com/search/results/?wt="+key+"&sort=re"
    print(url)
    response = requests.get(url)
    result_page = BeautifulSoup(response.content,'lxml')
    r = result_page.find_all('a')
    f=open("desc.txt",'w')
    for res in r:
            f.write(res.get('data-click-id')+'\n')
    f.close()
getrec()
