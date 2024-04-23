from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servive = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=servive, options=options)

url = 'http://bianca.com'
driver.get(url)
print('titulo do site:', driver.title)
busca = driver.find_element(By.XPATH, '/html/body').text
print('conteudo do site: ', busca)