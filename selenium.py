from selenium import webdriver
from bs4 import BeautifulSoup
import requests


# choisir marque et année min et max de la voiture
brand = "BMW"
year_min = 2010
year_max = 2019
url = """https://www.lacentrale.fr/listing?makesModelsCommercialNames={brand}&yearMax={year_max}&yearMin={year_min}""".format(
   brand=brand, year_min=year_min, year_max=year_max)


print(url)


# partie scrap


driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')


