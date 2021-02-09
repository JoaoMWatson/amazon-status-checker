import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
Dev Notes:main scrapp 
    body   -> div class="pad8 bordered gradient"
    navBar -> ul clas="yui-nav"
        click -> li id="SA_block_tab"
"""

URL = "https://status.aws.amazon.com/"

content = requests.get(URL)

soup = BeautifulSoup(content.content, 'html.parser')
main_div = soup.find("div", attrs={"id": "SA_block"})
main_table = main_div.find_all("table", attrs={"style": "border-spacing: 0; margin-bottom: 8px;"})



#nav_bar = soup.find("ul", attrs={"class": "yui-nav"})

print(main_table[1])
#print(nav_bar)