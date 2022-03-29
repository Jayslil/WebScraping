from bs4 import BeautifulSoup

from selenium.webdriver import Chrome


def get_html(url):
    driver = Chrome(executable_path='C:\\Program Files (x86)\\chromedriver.exe')
    driver.get(url)
    return driver.page_source


def get_link():
    url = 'https://iamovers.mobilityex.com/#/search/service-providers/1?loc=Europe&lat=54.5259614&lng=15.2551187' \
          '&range=50&assocs=800&fvw=true '
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    contact = soup.find_all('div', class_ = 'panel-body')
    print(contact)
    # for info in contact:
    #     name = soup.find_all('b')
    #     print(name)

    # for sub_page in company:
    #     sub_page = soup.find('a', {'style': 'text-decoration: none; font-size: 22px; font-weight: 500; line-height: '
    #                                         '1em; color: #000; color: #0000FF'})
    #
    #     if str(sub_page["href"].startswith("#")):
    #         full_link = starting_link + sub_page["href"][1:]
    #         print(full_link)


get_link()