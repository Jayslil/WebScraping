from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get(
    "https://iamovers.mobilityex.com/#/search?loc=Europe&lat=54.5259614&lng=15.2551187&range=50&assocs=800&fvw=c&ctry")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'cc-btn cc-dismiss'))).click()

list_links = []

left_component = driver.find_element(By.ID, 'left')
for company_box in left_component.find_elements(By.CSS_SELECTOR, 'div[ng-repeat="sp in sr track by $index"'):
    url_div = company_box.find_element(By.CLASS_NAME, 'col-md-6')
    url_a = url_div.find_element(By.TAG_NAME, 'a')
    url = url_a.get_attribute('href')
    print(url)



# driver.get('https://iamovers.mobilityex.com/#/search?loc=Europe&lat=54.5259614&lng=15.2551187&range=50&assocs=800&fvw=c&ctry=undefined%5C')
# print([my_elem.get_attribute("href") for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#left div[ng-repeat='sp in sr track by $index'] .col-md-6 a")))])