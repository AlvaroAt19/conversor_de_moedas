from bs4 import BeautifulSoup
import requests
  
#Raspagem das moedas existentes listadas no wikipédia

URL = "https://pt.wikipedia.org/wiki/Lista_de_moedas"
  
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
  
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "html.parser")
lst = soup.find_all("tr")

l = []
for i in lst[2:]:
    cot = str(i).split('<td>')[4].strip()
    fin = cot.split('\n')
    if len(fin[0]) < 4 and fin[0] not in l :
        l.append(fin[0])

with open('src/opcoes.txt', 'w') as opcoes:
    for i in l:
        opcoes.write(i + '\n')