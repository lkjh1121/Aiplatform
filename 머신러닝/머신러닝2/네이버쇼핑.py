import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

"""
https://search.shopping.naver.com/search/all?frm=NVSHATC base1
&origQuery=%EB%85%B8%ED%8A%B8%EB%B6%81 query1
&pagingIndex=1 page
&pagingSize=40&productSet=total base2
&query=%EB%85%B8%ED%8A%B8%EB%B6%81 query2
&sort=rel&timestamp=&viewType=list base3

https://search.shopping.naver.com/search/all?frm=NVSHATC
&origQuery=%EB%85%B8%ED%8A%B8%EB%B6%81
&pagingIndex=2
&pagingSize=40&productSet=total
&query=%EB%85%B8%ED%8A%B8%EB%B6%81
&sort=rel&timestamp=&viewType=list
"""

custom_header = {
            'referer':'https://search.naver.com/search.naver?where=news&sm=tab_pge',
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko"
        }

def getUrl(keyword="", end_page = 0):
    baseurl1 = "https://search.shopping.naver.com/search/all?frm=NVSHATC"
    baseurl2 = "&pagingSize=40&productSet=total"
    baseurl3 = "&sort=rel&timestamp=&viewType=list"
    query1 = "&origQuery=" + quote(keyword)
    query2 = "&query=" + quote(keyword)
    page = "&pagingIndex=" + str(end_page)
    url = baseurl1 + query1 + page + baseurl2 + query2 + baseurl3
    return url

def crawling(keyword="", start_page = 0, end_page = 0, filename = ""):
    f = open(filename, 'w', encoding='utf8')
    for page in range(start_page, end_page+1):
        url = getUrl(keyword, page)
        ress = requests.get(url, headers=custom_header)
        if ress.status_code != 200:
            print('문서로딩 실패')
            return
        soup = BeautifulSoup(ress.content)

        ul = soup.find('ul', {'class':'list_basis'})
        div1List = ul.find('div')
        div2List = div1List.find_all('div')
        for div in div2List:
            a = div.find('a', {'class':'basicList_link__JLQJf'})
            if a != None:
                print(f"{a['href']} 작업중.....")
                url2 = a['href']
                title, price = getTitle(url2)
                print(title, price, file = f)
    f.close()

def getTitle(url):
    response = requests.get(url, headers=custom_header)
    if response.status_code != 200:
        print('문서 로딩 실패')
        return
    title = ""
    price = ""

    soup = BeautifulSoup(response.content, 'html.parser')
    title_div = soup.find('div', {'class':'top_summary_title__ViyrM'})
    titletag = title_div.find('h2')
    title = titletag.text

    price_div = soup.find('div', {'class':'lowestPrice_low_price__Ypmmk'})
    pricetag = price_div.find('em', {'class':'lowestPrice_num__A5gM9'})
    price = pricetag.text + '원'

    if titletag != None and pricetag != None:
        return title, price

if __name__ == "__main__":
    keyword = input('어떤 품목을 검색하시겠습니까?')
    start_page = int(input('검색 시작 페이지 : '))
    end_page = int(input('검색 종료 페이지 : '))
    filename = input('저장할 파일 명 : ')
    crawling(keyword, start_page, end_page, filename)