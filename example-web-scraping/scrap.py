from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

products = []
hrefs = []
prices = []
ratings = []

driver = webdriver.Firefox()
driver.get("https://www.amazon.com/b?node=18505469011&pf_rd_p=27643bbf-38ff-4db5-8032-83558fc1281c&pf_rd_r=KVXWW63EKNPN8QE90WH0")
content = driver.page_source

soup = BeautifulSoup(content, 'html.parser')
ul = soup.ul
for li in ul.findAll('li', attrs={'class': 'celwidget'}):
  name = li.h2.text
  href = li.h2.parent.get('href')
  print(href)
  print(name)

  products.append(name)
  hrefs.append(href)

df = pd.DataFrame({'Product Name': products, 'Url': hrefs})
df.to_csv('amazon-products.csv', index=False, encoding='utf-8')