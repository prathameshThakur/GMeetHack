#For google meet meetings!!

import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options



 
url = 'https://meet.google.com/landing?authuser=1'  #meets website

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })


chrome = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)
chrome.get(url)
time.sleep(2)

#put email
email = chrome.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys('thakur.prathamesh18@siesgst.ac.in')
# time.sleep(2)

# #press next button
next1 = chrome.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
next1.click()
time.sleep(2)

#put password
pswd = chrome.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
pswd.send_keys('password')
time.sleep(2)

#press next button
next2 = chrome.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
next2.click()
time.sleep(3)

#enter meeting 
chrome.get('https://meet.google.com/yxc-hvun-ede')  #here enter the meeting url shared by teacher!
time.sleep(3)

#press dismiss for allow cam microphone msg
dismiss = chrome.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
dismiss.click()
time.sleep(2)
#join meeting
join = chrome.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
join.click()
# Now we are inside the meeting!
# aabhi code ka sleeping time aaisa set karna hai ke 2-3 min baad agar log eek threshod se kam ho gaye tho aapan bhi direct leave karneka..
time.sleep(10) # so ye me meeting join karneke 2min baad me dekhna chalu karunga



#getting data
#from here we will get to know whether the ppl are leaving or not!
"""
first attempt!
===========================
# data = chrome.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]')
# data.get_attribute('value')
# time.sleep(3)
===========================
second try
===========================
# while True:
#    get_url = chrome.current_url 

#     page = requests.get(meet_url)
#     tree = html.fromstring(page.content)
#     num = tree.xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]')[0].get('content')
#     if num<1:
#         end = chrome.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[9]/div[2]/div[2]/div')
#         end.click()
#         break
#     else:
#         time.sleep(2)
=============================
------------------------------------------------------------------
#ending call
# end = chrome.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[9]/div[2]/div[2]/div')
# end.click()
------------------------------------------------------------------
"""

#finally automated to end call after a threshold
while True:
    print('Working fine!!!!')
    data = chrome.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]')
    # num = data.get_attribute('value')
    num=data.text
    if int(num)<15: #here threshold is 3.. meaning, when the no. of ppl decreased by less than 3 it will end the call!!
        end = chrome.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[2]/div')
        end.click()
        print('SESSION ENDED!!!'*3)
        break
    else:
        time.sleep(2)