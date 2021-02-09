from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = "https://www.teamrankings.com/nfl/"
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

#html parser
pageSoup = soup(page_html, "html.parser")
items = pageSoup.find_all('td', class_="text-right")
teamNames = pageSoup.find_all('div', class_="table-team-logo-text")
empty = []
emptyNames = []
i = 0
x = 0
0

filename = 'info.csv'
f = open(filename, 'w')
headers = 'Team, Playoff Percent \n'
f.write(headers)

for item in items:
    i = i + 1
    if (i % 4 == 3):
        new = item.text
        empty.append(new)
i = 0
for team in teamNames:
        i = i + 1
        emptyNames.append(team.a.text)
        f.write(team.a.text + "," + empty[i] + "\n")

print(empty)
print(emptyNames)
f.close()