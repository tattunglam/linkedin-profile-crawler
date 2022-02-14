from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

# Login to Linkedin
# Open chrome and direct to linkedin login page
driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
url = 'https://www.linkedin.com/login'
driver.get(url)
sleep(2)

# Extract credentital information
credential = open('login_credential.txt')
line = credential.readlines()
username = line[0]
password = line[1]

# Fill form & login
email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(username)
sleep(3)
password_field = driver.find_element(By.NAME, 'session_password')
password_field.send_keys(password)
sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
login_button.click()
sleep(3)

# Search for the profiles
driver.maximize_window()
search_field = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
search_query = input('What profile do you want to scrape?')
search_field.send_keys(search_query)
search_field.send_keys(Keys.RETURN)

people_button = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[4]')
people_button.click()


# Open the URLs of the profiles