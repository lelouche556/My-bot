"""
Thanks, You came here to check me. Let me describe my working-
1. User will enter one of the pre-defined task.
3. Chrome Webdriver will be opened.
4. User wiil be asked for username and password if required.
5. I will do my job with Selenium, PyautoGUI.
6. User will be asked whether he wants to continue.

If still facing any issue, feel free to contact my developer at dmangla3@gmail.com.
"""
# One thing you can do in this code is adding error handling if user enters incorrect username or password.
# Try adding new features like Speech recognition.

import os
print("\nHey, My name is Autobot.\n")
os.system("espeak 'Hey,My name is Autobot. '")
from datetime import datetime
response = os.system("ping -c 1 google.com")
if response == 0:
    print('You internet is working properly')
    os.system("espeak 'Sir, Your internet is working properly'")
else:
    print('Sir, your internet is not working')
    os.system("espeak ' Internet is not working. Going ahead, is waste, of time.'")
print("Current time is ",str(datetime.now()))
os.system("espeak 'Welcome'")
reaction = 'y'


while reaction == "y":
	print('\n\tWhat you want me to do')
	os.system("espeak 'What you want me to do'")
	print('\nI can\n\nopenfb\nopengmail\nsend_wtsp_msg\nwhoislookup\ngithubsearch\nsearchgoogle')
	os.system("espeak 'I can.open facebook. open gmail. send whatsapp messages. search on who, is lookup. github search. Search google.'" )
	task = input('\t')
	import pyautogui, time


	if task == "openfb":
		import os
		import pyautogui
		import time
		from selenium import webdriver
		from selenium.webdriver.common.keys import Keys
		os.system('espeak "Enter email and Password"')
		email_ = input("Enter email")
		pass_ = input("Enter password")
		browser = webdriver.Chrome()
		browser.get('http://facebook.com')
		os.system("espeak 'I think it is slow internet not letting me work properly..Dont you think so? '")
		emailElem = browser.find_element_by_id("email")
		emailElem.send_keys(email_)
		passElem = browser.find_element_by_id("pass")
		passElem.send_keys(pass_)
		passElem.send_keys(Keys.RETURN)

	elif task == "opengmail":
		import time
		from selenium import webdriver
		from selenium.webdriver.common.keys import Keys
		os.system('espeak "Enter Email and Password"')
		email_ = input("Enter your email")
		pass_ = input("Enter password")
		browser = webdriver.Chrome()
		browser.get('https://gmail.com')
		elem = browser.find_element_by_css_selector('#identifierId')
		elem.click()
		elem.send_keys(email_)
		print('Email id has been entered')
		elem.send_keys(Keys.ENTER)
		time.sleep(4)
		pas = browser.find_element_by_name('password')
		pas.click()
		pas.send_keys(pass_)
		print('Password has been entered')
		pas.send_keys(Keys.ENTER)
		print('We have logged in your account')


	elif task == "searchgoogle":
		import os

		print("Where you want to go:")
		os.system("espeak 'Where you, want to go'")
		query = input()
		print("INITIALISING...")
		from selenium import webdriver as wd
		bro = wd.Chrome()
		bro.get('https://www.google.co.in')
		import pyautogui as pag
		pag.typewrite(query)
		os.system("espeak 'Now, you will be redirected to another page'")
		pag.click(165,313)
		time.sleep(1)
		elem = bro.find_element_by_css_selector('#tsf > div.tsf-p > div.jsb > center > input[type="submit"]:nth-child(2)')
		elem.click()


	elif task == "send_wtsp_msg":
		from selenium import webdriver
		import pyautogui
		from selenium.webdriver.common.keys import Keys
		import time
		# Open Whatsapp
		print('A QR code page will open, scan it with your phone Master')
		ready = input('Are you ready,Master?  y/n  ')
		if ready == 'y':
			print('After scanning QR code click on person whom who want to send the message')
			messa = input('Enter the message, Master:  ')
			print('I will ask you later for no of messages, Master')
			print("INITIALISING...")
			browser = webdriver.Chrome()
			browser.get('https://web.whatsapp.com')
			os.system('espeak "Scan code with your phone"')
			print("Scan QR code from your phone.\nClick on person you want to send this message.\n\n")
			os.system('espeak "Enter no of messages"')
			num_of_t = int(input("How many times you want to send message:  "))
			elem = browser.find_element_by_css_selector(
				'#main > footer > div.block-compose > div.input-container > div > div.input')
			# click on message box
			elem.click()
			# Give user 10 sec to click on message box again
			ini = time.time()
			time.sleep(10)
			for i in range(num_of_t):
				pyautogui.typewrite(messa)
				elem.send_keys(Keys.ENTER)
			ou = time.time()
			print("I have sent ", messa, " to person you selected ", num_of_t, " times.\n\nThis process took ",
				  ou - ini, " secs.")


	elif task == "whoislookup":
		print('\n\nI am glad buddy you thought about using me..I\'ll not disappoint you.')
		domain = input('Enter the domain or ip you want to lookup: ')
		print('INITIALISING...')
		import time

		time.sleep(2)
		from selenium import webdriver

		browser = webdriver.Chrome()
		browser.get('https://www.whois.com/whois')
		elem = browser.find_element_by_css_selector('#query')
		import pyautogui

		elem.click()
		pyautogui.typewrite(domain)
		pyautogui.typewrite('\n')

		print('Now leave me alone')


	elif task == "githubsearch":

		import os
		from selenium import webdriver
		import pyautogui as pag
		os.system('espeak "Enter username and password"')
		user = input("What's your github username?  ")
		passw = input("Enter your password  ")
		search = input("Enter what you want me to search on Github:  ")
		print("\n")
		print("Initialising...")
		bro = webdriver.Chrome()
		try:
			bro.get('https://www.github.com/login/')
			elem = bro.find_element_by_css_selector('#login_field')
		except:
			print("Sir, you internet is not working properly")
			os.system("espeak ' Sorry, sir. Your internet is not working'")
			continue

		elem.click()
		pag.typewrite(user)
		pag.typewrite('\t')
		pag.typewrite(passw)
		elem = bro.find_element_by_css_selector(
			'#login > form > div.auth-form-body.mt-3 > input.btn.btn-primary.btn-block')
		elem.click()
		import time

		pag.typewrite('\t\t\t\t')
		time.sleep(1)
		pag.typewrite(search)
		pag.typewrite('\n')
		elem.click()

	print("INITIALIZING...")
	reaction = input("Do you want to continue? y/n:  ")
	if reaction == "y":
		os.system("espeak 'Oh! So you will not let me sleep? '")
