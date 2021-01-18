import requests
from bs4 import BeautifulSoup

URL = "https://scrap.tf/raffles"

def tf_scrap():
  title_list = []
  url_list = []

  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pag = soup.find_all("div", {"class": "panel-heading"})

  # pag2 = soup.find_all("div", {"class": "items-container"}) 사진 추출
  #
  # for loof_pag2 in pag2:
  #     url = loof_pag2.find('div')
  #     print(url['style'])

  for loof_pag in pag:
   url = loof_pag.find('a')

   test = loof_pag.find('items-container')



   if url is not None:
     a = f"https://scrap.tf{url['href']}"

     pom = {
           'title': url.get_text(strip=True),
           'link': a
     }
     title_list.append(pom)
  return title_list