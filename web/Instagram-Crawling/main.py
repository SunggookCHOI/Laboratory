from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('./driver/chromedriver.exe')

ID='id'
PW='pw'

driver.implicitly_wait(5)

driver.get('https://www.instagram.com/heartit.kr/?utm_source=ig_embed')

driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a').click()
driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div > div > div:nth-child(3) > a').click()

driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input').send_keys(ID)
driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input').send_keys(PW)
driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div').click()

# follow 클릭
driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a').click()

target_num = int(driver.find_elements_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(3) > a > span')[0].text)
target_num = 30
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
#print(follow_ids)

INSTA = "https://www.instagram.com/"
start_date = "2020-01-15"

for f in follow_ids[:1]:
    driver.implicitly_wait(1)
    driver.get(INSTA+f+'/')
    driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a > div.eLAPa > div._9AhH0').click()
    datetime = driver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > div > li > div > div > div.C4VMK > div > div > time').get_attribute('datetime')[:10]
    #while datetime > start_date:
    for _ in range(7):
        print(datetime, datetime<'2020-02-04')
        try:
            location = driver.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.M30cS > div.JF9hh > a').text
            print(location)
        except:
            print('없어')
        # 다음 게시물로
        try:
            driver.find_element_by_css_selector('div._2dDPU.vCf6V > div.EfHg9 > div > div > a.HBoOv.coreSpriteRightPaginationArrow').click()
        except:
            continue
driver.close()

