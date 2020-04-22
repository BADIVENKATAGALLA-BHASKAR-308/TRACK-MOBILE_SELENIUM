from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

def find_and_trace():

	#input for the search box
	mobile_num = input("Enter the mobile_num:-")
	driver = webdriver.Chrome("chromedrive_64/chromedriver")
	driver.get("https://www.findandtrace.com/")
	# #find the tracking path:-
	mobile_tracker = driver.find_element_by_link_text("Trace Mobile").click()
	search_box = driver.find_element_by_id("searchbox")
	search_box.send_keys(mobile_num)
	trace = driver.find_element_by_xpath('//input[@name="submit"]').click()
	#parsing the data into text format:-
	document_format = driver.execute_script("return document.documentElement.outerHTML")
	soup = BeautifulSoup(document_format,"html.parser")
	time.sleep(5)
	# #finding link for the mobile tracking:-
	dict_for_mobile_tracking = {}
	table = soup.find("table",class_="shop_table")
	tr_tags = table.find_all("tr")
	for tr in tr_tags:
		ths = tr.find("th").text
		bs = tr.find("b").text
		dict_for_mobile_tracking[ths]=bs
	print(dict_for_mobile_tracking)

find_and_trace()



			
		







































