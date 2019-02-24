import requests
import pandas as pd
from bs4 import BeautifulSoup

## Session start
my_session = requests.session()
for_cookies = my_session.get("https://ctftime.org/stats/2019/GB")
cookies = for_cookies.cookies
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
url = 'https://ctftime.org/stats/2019/GB'
##

## Response test
response = my_session.get(url, headers=headers, cookies=cookies)
print(response.status_code)  # 200
##


## Find table and print contents
soup = BeautifulSoup(response.content,'lxml')
table = soup.findAll("table",{"class":"table table-striped"})
df = pd.read_html(str(table))
data = print(df[0].to_json(orient='records'))
##

## Output to file
f = open("example_output.txt", "w")
f.write(str(df[0].to_json(orient='records')))
f.close()
##