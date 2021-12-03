# import necessary modules
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# define sample information about target person
name = "Darren Singh"
location = "Toronto"
occupation = "Student"
school = "York University"

# define dictionary with the sample input information
sampleDict = {"name": name, "loc": location, "job": occupation, "School": school}

# locate chrome driver
browser = webdriver.Chrome('C:\\Users\\d\\Downloads\\chromedriver_win32\\chromedriver.exe')

# create a function to access and login to instagram (use a fake account for this so you're real one doesn't get banned)
# sleep is the time the program waits for web pages to load, it can depend on internet speed and computer performance
    # 5 seconds works well for an internet speed of 200mb/s down and 10mb/s up, with 8gb of ram and an 8th gen laptop i5
    # 3 seconds works well for the same internet speed but with 32gb of ram and a 10th gen desktop i7
# if the code is crashing, the sleep value may need to be increased

def instagramSearch(username, password, inputDict, sleep = 5):

    # parse through input dictionary, maybe create a function to do this since it will be done for every search function
    name = inputDict.get("name")
    loc = inputDict.get("loc")
    job = inputDict.get("job")
    school = inputDict.get("School")

    # later on store the number of attributes in the dictionary so the social media profiles can be used

    url = "https://www.instagram.com"
    browser.get(url)

    # allow time for page to load
    time.sleep(sleep)

    # locate the password and username text fields, then feed in the password and username for the account you are using
    usernameField = browser.find_element("name", "username")
    usernameField.send_keys(username)
    passwordField = browser.find_element("name", "password")
    passwordField.send_keys(password)

    # click submit
    browser.find_element("xpath", "//*[@id='loginForm']/div/div[3]/button/div").click()

    # by pass popups
    time.sleep(sleep)
    browser.find_element("xpath", "//*[@id='react-root']/section/main/div/div/div/div/button").click()
    time.sleep(sleep)
    browser.find_element("xpath", "/html/body/div[5]/div/div/div/div[3]/button[2]").click()

    # search profiles using the name attribute of the target
    time.sleep(sleep)
    searchBar = browser.find_element("xpath", "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
    searchBar.send_keys(name)

    # next step is to click on each profile in the drop down menu and check if its bio has any of attributes of the target
    # maybe do this using item.sendKeys(Keys.ENTER)

instagramSearch("null", "null", sampleDict, sleep=3)