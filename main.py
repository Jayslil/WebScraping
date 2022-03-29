from bs4 import BeautifulSoup

from selenium.webdriver import Chrome


def get_html(url):
    driver = Chrome(executable_path='C:\\Program Files (x86)\\chromedriver.exe')
    driver.get(url)
    return driver.page_source


def get_link():
    url = 'https://iamovers.mobilityex.com/#/search?loc=Europe&lat=54.5259614&lng=15.2551187&range=50&assocs=800&fvw' \
          '=c&ctry=undefined%5C '
    starting_link = 'https://iamovers.mobilityex.com/'
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    company = soup.find_all('div', class_ = 'col-md-6')
    list_links = []
    # print(company)

    for sub_page in company:
        sub_page = soup.find('a', {'style': 'text-decoration: none; font-size: 22px; font-weight: 500; line-height: '
                                            '1em; color: #000; color: #0000FF'})

        if str(sub_page["href"].startswith("#")):
            full_link = starting_link + sub_page["href"][1:]
            print(full_link)


get_link()

# sub_page = soup.find('a', {'style': 'text-decoration: none; font-size: 22px; font-weight: 500; line-height: 1em; color: #000; color: #0000FF'})
    # for link in sub_page:
    #     if str(sub_page["href"].startswith("#")):
    #         full_link = starting_link + sub_page["href"]
    #         print(full_link)
