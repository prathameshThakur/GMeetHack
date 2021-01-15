# For google meet meetings!!

import requests
import time
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

"""
#------------------Flow that need to be followed-----------------#
1. Open chrome browser
2. Open the google login page
3. Enter the email password and get in
4. Go to the desired G-meet  
5. After getting into meet keep an eye on the participants counts
   and end the meet after the min. threshold
#----------------------------------------------------------------#
"""

# google meet link
url = 'https://meet.google.com/landing?authuser=1'

# get data from user!
print("#+"*10)
email = input("Enter your email address: ").strip()
password = getpass("Password: ")
meet_code = input("Google meet code(eg: abc-defg-hij): ").strip()
set_threshold = int(
    input("Minimum count of participants after which you want to end the meet: "))
print("#+"*10)
time.sleep(1)
print("I have activated the system!!!!!\nEnjoy!")
# activate_task(opt, email, password, meet_code, set_threshold)


# -----The following code snipet disables the microphone and video access from the browser----- #
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2,
    "profile.default_content_setting_values.notifications": 2
})
#------------------------------------------------------------------------------------------------#

# install n open driver
chrome = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=opt)
chrome.get(url)
time.sleep(2)

# put email
emailid = chrome.find_element_by_xpath('//*[@id="identifierId"]')
emailid.send_keys(email)
# time.sleep(2)

# press next button
next1 = chrome.find_element_by_xpath(
    '//*[@id="identifierNext"]/div/button/div[2]')
next1.click()
time.sleep(2)

# put password
pswd = chrome.find_element_by_xpath(
    '//*[@id="password"]/div[1]/div/div[1]/input')
pswd.send_keys(password)
time.sleep(2)

# press next button
next2 = chrome.find_element_by_xpath(
    '//*[@id="passwordNext"]/div/button/div[2]')
next2.click()
time.sleep(3)

# enter meeting
chrome.get(f'https://meet.google.com/{meet_code}')
time.sleep(3)

# press dismiss for allow cam microphone msg
dismiss = chrome.find_element_by_xpath(
    '//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
dismiss.click()
time.sleep(2)

# join meeting
join = chrome.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span')
join.click()

# Now we are inside the meeting!
time.sleep(100)

# getting data
# from here we will get to know whether the ppl are leaving or not!
# finally automated to end call after a threshold
while True:
    print('Working fine!!!!')
    data = chrome.find_element_by_xpath(
        '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]')
    # num = data.get_attribute('value')
    num = data.text
    if int(num) < set_threshold:
        # by default threshold is 3.. meaning, when the no. of ppl decreased by less than 3 it will end the call!!
        end = chrome.find_element_by_xpath(
            '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div')
        end.click()
        print('SESSION ENDED!!! '*3)
        break
    else:
        time.sleep(2)


