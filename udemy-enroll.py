import os
import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def  load_driver():
	options = webdriver.FirefoxOptions()
	
	# enable trace level for debugging 
	options.log.level = "trace"

	options.add_argument("-remote-debugging-port=9224")
	options.add_argument("-headless")
	options.add_argument("-disable-gpu")
	options.add_argument("-no-sandbox")

	binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))

	firefox_driver = webdriver.Firefox(
		firefox_binary=binary,
		executable_path=os.environ.get('GECKODRIVER_PATH'),
		options=options)

	return firefox_driver
load_driver()
################################################################
parser = argparse.ArgumentParser(description='Udemy Enrolling Script')
parser.add_argument('Email', metavar='Email', type=str , help='Enter your email')
parser.add_argument('Password', metavar='Password', type=str , help='Enter your password')
args = parser.parse_args()
Email = args.Email
Password = args.Password
web = webdriver.Firefox()
web.get("https://www.udemy.com/")
web.implicitly_wait(5)
login_in = web.find_element_by_link_text("Log in").click()
web.implicitly_wait(5)
email = web.find_element_by_id("email--1").send_keys(Email)
Pass = web.find_element_by_id("id_password").send_keys(Password)
login = web.find_element_by_id("submit-id-submit").click()
web.implicitly_wait(6)
links = open("links.txt","r+")
lst_link = [link.partition('|')[0].strip() for link in links]
for enroll_link in lst_link:
    web.get(enroll_link)
    time.sleep(3)
    try:
        enroll_button = WebDriverWait(web, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".sidebar-container--purchase-section--17KRp > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)"))
        )
        enroll_button.click()
        time.sleep(6)
        web.find_element_by_css_selector('.styles--checkout-pane-outer--1syWc > div:nth-child(1) > div:nth-child(4) > button:nth-child(2)').click()
        time.sleep(5)
    except:
        continue
print('======= Done :) =======')
#web.close()
