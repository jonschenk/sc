from bs4 import BeautifulSoup
import requests
import time

current_time = time.asctime(time.localtime())

url = "ENTER NEWEGG PRODUCT URL HERE"
doc = BeautifulSoup(requests.get(url).text, "html.parser")
prices = doc.find_all(string ="$")
parent = prices[0].parent
strong = parent.find("strong")
result = int(strong.string.replace(",", ""))

print("$" + result, current_time)
