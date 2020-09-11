from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

#ig user name & password
with open('user.txt','r') as u:
    user_name = u.read()
with open('password.txt') as pas:
    password = pas.read()

driver = webdriver.Chrome(executable_path=r'chrome_driver_path')
driver.get('https://google.com')
driver.maximize_window()
src = driver.find_element_by_xpath('search_xpath')
src.click()
src.send_keys('IHSG')
time.sleep(3)
src.send_keys(Keys.ENTER)
time.sleep(5)

wkt = driver.find_element_by_xpath('xpath_of_time')
wkt_txt = wkt.text
jm = wkt_txt[6:12]

while True:
    try:
        wkt = driver.find_element_by_xpath('xpath_of_time')
        wkt_txt = wkt.text
        jm = wkt_txt[6:12]

        p = driver.find_element_by_xpath('xpath of price')
        p_txt = p.text
        base = int(p_txt[0])

        #conditions
        if jm == "11.30" or jm == "14.49":
            if base < 5:
                driver.get('https://instagram.com')
                time.sleep(5)
                us = driver.find_element_by_xpath('login_xpath')
                #login
                us.click()
                us.send_keys(user_name)
                pa = driver.find_element_by_xpath('password_xpath')
                pa.click()
                pa.send_keys(password)
                pa.send_keys(Keys.ENTER)
                time.sleep(5)
                #sending message
                driver.get('https://www.instagram.com/direct/t/xxxxxxxxxxx') #get the address to direct message to your account
                time.sleep(4)
                no = driver.find_element_by_xpath('xpath to no')
                no.click()
                msg = driver.find_element_by_xpath('xpath to send message')
                msg.click()
                snd = driver.find_element_by_xpath('xpath to write the message')
                snd.click()
                snd.send_keys("sekarang jam:"+jm+", "+"harga IHSG sekarang: "+p_txt)
                snd.send_keys(Keys.ENTER)
                time.sleep(3)
                driver.get('https://get back to the first address openned')
                time.sleep(5)

        #checking every 5 minutes
        print(jm)
        time.sleep(300)
        driver.refresh()
        time.sleep(5)
    except NoSuchElementException:
        driver.quit()
