# import necessary modules
import selenium
from selenium import webdriver

# define sample information about target person
name = "Darren Singh"
location = "Markham"
Occupation = "Student"
School = "York University"

# begin opening webpages
browser = webdriver.Chrome('C:\\Users\\d\\Downloads\\chromedriver_win32\\chromedriver.exe')
url = 'https://www.google.ca'
browser.get(url)
