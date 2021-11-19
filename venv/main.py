# import necessary modules
import selenium
from selenium import webdriver
import time

# define sample information about target person
name = "Darren Singh"
location = "Toronto"
Occupation = "Student"
School = "York University"

# locate chrome driver
browser = webdriver.Chrome('C:\\Users\\d\\Downloads\\chromedriver_win32\\chromedriver.exe')

# create a function to access and login to instagram (use a fake account for this so you're real one doesn't get banned)
def instagram(username, password):
    url = "https://www.instagram.com"
    browser.get(url)
    # allow time for page to load
    time.sleep(5)

    # locate the password and username text fields, then feed in the password and username for the account you are using


instagram(1, 1)