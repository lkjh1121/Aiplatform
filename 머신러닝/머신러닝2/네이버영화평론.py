from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

path = './driver/chromedriver.exe'

driver = webdriver.Chrome(path)

# url = "https://movie.naver.com/movie/point/af/list.naver?&page=1"
# driver.get(url)
# driver.implicitly_wait(1)

def showData():
    table = driver.find_element(By.CLASS_NAME, "list_netizen")
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    trList = tbody.find_elements(By.TAG_NAME, 'tr')
    for tr in trList:
        for td in tr.find_elements(By.TAG_NAME, 'td'):
            print(td.text, end='\t')
        print()

# showData()

#old_content > div.paging > div > a:nth-child(2)
#old_content > div.paging > div > a:nth-child(3)
#old_content > div.paging > div > a.pg_next
import time

# showData()
# for i in range(1, 5):
#     page = driver.find_element(By.CSS_SELECTOR, "#old_content > div.paging > div > a.pg_next")
#     page.click()
#     time.sleep(2)
#     showData()

url = "https://www.python.org/"
driver.get(url)
driver.implicitly_wait(1)

element = driver.find_element(By.CSS_SELECTOR, "#content > div ? section > form > ul > li:nth-child(1) > h3 > a")
element.click()
print(driver.page_source)
bs = BeautifulSoup(driver.page_source, 'html.parser')
h1 = bs.find('h1', {'class':'page-title'})
print(h1.text)


###########################################################################################################################################################
# custom_header = {
#             'referer':'https://search.naver.com/search.naver?where=news&sm=tab_pge',
#             "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko"
#         }

# def getUrl(page_end):
#     baseurl = "https://movie.naver.com/movie/point/af/list.naver?"
#     page = "&page=" + str(page_end)
#     url = baseurl + page
#     return url

# def crawling(page_start = 0, page_end = 0, filename = ''):
#     f = open(filename, 'w', encoding='utf8')
#     for page in range(page_start, page_end+1):
#         url = getUrl(page)
#         ress = requests.get(url, headers = custom_header)
#         if ress.status_code != 200:
#             print('문서 로딩 실패.')
#             return
#         soup = BeautifulSoup(ress.content)
#         tbody = soup.find('tbody')
#         trList = tbody.find_all('tr')
#         tdList = trList.find_all('td')
#         for td in tdList:
#             a = td.find('a', {'class':'movie color_b'})
#             if a != None:
#                 url2 = a['href']
#                 print(f'{url2} 작업중...')
#                 title, contents = getTitleContents(url2)
#                 print(title, contents, file = f)
#     f.close()
                
# def getTitleContents(url):
#     ress = requests.get(url, headers=custom_header)
#     if ress.status_code != 200:
#         print('문서 로딩 실패')
#         return
#     title = ''
#     contents = ''
#     soup = BeautifulSoup(ress.content, 'html.parser')

#     titletag = soup.find('a', {'title':'캐릭터'})
#     if titletag != None:
#         title = titletag.text

#     contenttag = soup.find(r'//*[@id="old_content"]/table/tbody/tr[1]/td[2]/text()')
#     if contenttag != None:
#         contents = contenttag.text

#     return title, contents
    

# if __name__ == "__main__":
#     page_start