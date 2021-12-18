# import necessary modules
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tools import dictionaryParser

# define sample information about target person
name = "Darren Singh"
location = "Toronto"
occupation = "Student"
school = "York University"

# define dictionary with the sample input information
sampleDict = {"name": name, "loc": location, "job": occupation, "School": school}

# locate chrome driver
browser = webdriver.Chrome('C:\\Users\\d\\Downloads\\chromedriver_win32\\chromedriver.exe')

# create a function to access and login to instagram (use a fake account for this so your real one doesn't get banned)
# sleep is the time the program waits for web pages to load, it can depend on internet speed and computer performance
    # 5 seconds works well for an internet speed of 200mb/s down and 10mb/s up, with 8gb of ram and an 8th gen laptop i5
    # 3 seconds works well for the same internet speed but with 32gb of ram and a 10th gen desktop i7
# if the code is crashing, the sleep value may need to be increased


def instagramSearch(username, password, inputDict, sleep = 5):

    # call the dictionary parser to extract useful attributes for the search function
    name, loc, job, school, attributes = dictionaryParser(inputDict)

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

    # clicking on first element in drop down menu
    time.sleep(sleep)
    browser.find_element("xpath","//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()

    # retrieving text of the instagram bio of the selected profile
    time.sleep(sleep)
    bio = browser.find_element("xpath", "//*[@id='react-root']/section/main/div/header/section/div[2]/span").get_attribute('innerHTML')

    # convert the text in the bio into a list
    bioText = bio.split("<br>")

    # search the text in the bio for attributes about the person
    # use the find() method to do this, it finds a word in a string and returns the index, if it does not find it, it returns -1
    # use loops to check if each of the attributes exists in the bio
    for attribute in attributes:
        for sentence in bioText:
            index = sentence.find(attribute)
            if index != -1:
                # do something there like award a point

instagramSearch("tester77707", "tester789", sampleDict, sleep=5)

