import requests
from bs4 import BeautifulSoup

URL = "https://scrap.tf/raffles"

def tf_scrap():
  title_list = []
  url_list = []

  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pag = soup.find_all("div", {"class": "panel-heading"})

  for loof_pag in pag:
   url = loof_pag.find('a')

   if url is not None:
     title_list.append(f'title : {url.get_text(strip=True)}, link : https://scrap.tf{url["href"]}')
     #title_list.append(f"{url.get_text(strip=True)}$%^&#$https://scrap.tf{url['href']}")
  return title_list


# for aa in tf_scrap():
#   print(aa)

  # for loof_pag in pag:
  #   url = loof_pag.find('a')
  #
  #   if url is not None:
  #     num += 1
  #
  #     if num == 60:
  #       url_list.append(f"https://scrap.tf{url['href']}") # 주소
  #       title_list.append(url.get_text(strip=True))
  #
  #       aa.append(f"'Title': {title_list},'Link': {url_list}")
  #       print(num)