from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

path = './driver/chromedriver.exe'

driver = webdriver.Chrome(path)
driver.implicitly_wait(5)

# url = "https://www.python.org/"
# driver.get(url)
# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys('pycon')
# # search_box.submit()
# search_box.send_keys(Keys.RETURN)

# # 규칙성 찾기
# #content > div > section > form > ul > li:nth-child(1) > h3 > a 
# #content > div > section > form > ul > li:nth-child(2) > h3 > a
# element = driver.find_element(By.CSS_SELECTOR, "#content > div > section > form > ul > li:nth-child(1) > h3 > a")
# element.click()
# # print(driver.page_source)
# bs = BeautifulSoup(driver.page_source, 'html.parser')
# maintag = bs.find('div', {'class':'section'})
# p_list = maintag.find_all('p')
# for p in p_list:
#     print(p.text)

url = 'https://www.codingworldnews.com/news/articleList.html?sc_area=A&view_type=sm&sc_word=IoT'
driver.get(url)
print(driver.page_source)