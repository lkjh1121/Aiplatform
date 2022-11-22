# 셀레니움은 크롬 개발중에 만들어진 디버깅 툴
# 이벤트를 발생시켜서 해야할 경우에 셀레니움을 사용한다

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

path = './driver/chromedriver.exe'

driver = webdriver.Chrome(path) # 크롬 드라이버 파일을 로딩한다.
driver.implicitly_wait(5) # 3초 후에 검색을 시작해라

# driver가 가리키는 객체 안에 모든 정보가 다 들어있다. (requests대신 사용)
url = "http://google.com"
driver.get(url) # 웹 브라우저가 뜸
# 구글 파일을 불러와서 내부에서 처리가 다 이루어짐
# 검색창에 검색어를 입력해서 실행시킨다.

# driver.find_element(By.종류, "input") - 첫번째 것만 가지고 온다.
# driver.find_elements                  - 복수, 인덱스가 있어야한다.
search_box = driver.find_element(By.NAME, 'q') # find_element = 단수, find_elements = 복수
search_box.send_keys('파이썬') # 검색창에 글씨 출력

# search_box.submit() # 서버로 현재 입력한 내용을 전송하라 -> 검색창에 입력후 엔터키를 누르는 행위와 같다.
search_box.send_keys(Keys.RETURN) # 바로 위 코드와 같은 역할을 한다.
element = driver.find_element(By.CSS_SELECTOR, "#content > div ? section > form > ul > li:nth-child(1) > h3 > a")
element.click()
print(driver.page_source)
bs = BeautifulSoup(driver.page_source, 'html.parser')
h1 = bs.find('h1', {'class':'page-title'})
print(h1.text)