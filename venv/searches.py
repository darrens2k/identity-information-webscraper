# import necessary modules
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# maybe let each target class contain an array of results, or the results of each type
class Result:
    '''A class to store the results, a result being a website or social media profile that was searched. It will store the url and score of the result.
    The score is determined by how many attributes of the target the result contains'''
    def __init__(self, url):
        self.score = 0
        self.url = url


# Common Parameters
    # sleep is the time the program waits for web pages to load, it can depend on internet speed and computer performance
        # 5 seconds works well for an internet speed of 200mb/s down and 10mb/s up, with 8gb of ram and an 8th gen laptop i5
        # 3 seconds works well for the same internet speed but with 32gb of ram and a 10th gen desktop i7

# create a function to access and login to instagram (use a fake account for this so your real one doesn't get banned)
# if the code is crashing, the sleep value may need to be increased
# iterations is the number of search results that are checked
def instagramSearch(username, password, target, sleep = 5, iterations = 5):

    # locate chrome driver
    browser = webdriver.Chrome('C:\\Users\\d\\Downloads\\chromedriver_win32\\chromedriver.exe')

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

    # creating loop to go through the number of search results indicated by the iterations parameter
    for i in range(1, iterations + 1):

        # search profiles using the name of the target
        time.sleep(sleep)
        searchBar = browser.find_element("xpath", "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        searchBar.send_keys(target.name)

        # clicking on first element in drop down menu
        time.sleep(sleep)
        profile = browser.find_element("xpath","//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[" + str(i) + "]/a/div")
        profile.click()

        # create instance of result class with this url
        result = Result(browser.current_url)

        # purpose of using the try-except here is because if the profile has no bio, then the score of the result should remain at 0, nothing in the try should be executed
            # and the except will simply add the result to target's instagramResults
        try:

            # retrieving text of the instagram bio of the selected profile
            time.sleep(sleep)
            bio = browser.find_element("xpath", "//*[@id='react-root']/section/main/div/header/section/div[2]/span").get_attribute('innerHTML')

            # convert the text in the bio into a list
            bioText = bio.split("<br>")

            # search the text in the bio for attributes about the person
            # use the find() method to do this, it finds a word in a string and returns the index, if it does not find it, it returns -1
                # one thing to look into is to check the bio for abbreviations of the attributes, or simply the occurence of a few of the characters but that will increase runtime
            # use loops to check if each of the attributes exists in the bio
            for attribute in target.attributes:
                for sentence in bioText:
                    index = sentence.find(attribute)
                    # -1 is returned if the attribute was not found in the bio
                    if index != -1:
                        result.score += 1
            # once the scoring method is implemented, define this as a function which will take some text as an input and search through it for attributes if code is repeated in other search functions

            # add the result to the instagramResults of the target so it can accessed later if necessary
            target.instagramResults.append(result)

        except:

            target.instagramResults.append(result)

# issues
    # what happens if an item in the search bar is not a profile but a hashtag instead?
        # a try-except might be the solution


# begin work on the linkedinSearch() function
# create function to log into LinkedIn and search for the target
def linkedinSearch(username, password, sleep = 5):
    # first step is to create a fake LinkedIn account