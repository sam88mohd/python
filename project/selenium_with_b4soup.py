from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get("https://realpython.github.io/fake-jobs/")

page_source = driver.page_source
soup = bs(page_source, 'lxml')
job_titles = []
cards_selector = soup.find_all('div', class_='card-content')

for card in cards_selector:
    media_div = card.find('div', class_='media')
    content = media_div.find('div', class_='media-content')
    job_title = content.find('h2').get_text()
    job_title.strip()
    job_titles.append(job_title)

print(job_titles)
