from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('./driver/chromedriver.exe')

driver.implicitly_wait(5)

driver.get('https://www.instagram.com/heartit.kr/?utm_source=ig_embed')

ID = 'id'
PW = 'pw'


driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a').click()
driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div > div > div:nth-child(3) > a').click()

driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input').send_keys(ID)
driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input').send_keys(PW)
driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div').click()

# follow 클릭
driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a').click()

target_num = int(driver.find_elements_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a > span')[0].text)
#target_num = 30
print(target_num)

driver.implicitly_wait(3)

follow = driver.find_elements_by_css_selector('.PZuss > li')
while len(follow) < target_num:
    driver.implicitly_wait(3)
    follow[-1].click()
    driver.execute_script("window.scrollTo(0, 3000)")
    follow = driver.find_elements_by_css_selector('.PZuss > li')
follow_ids = []

for f in follow:
    follow_ids.append(f.find_element_by_css_selector('.d7ByH > a').text)
print(follow_ids)

driver.close()