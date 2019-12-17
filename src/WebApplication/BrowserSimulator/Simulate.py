from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import sys

url = sys.argv[1]
viewfilename = sys.argv[2]
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options,executable_path="../../include/chromedriver")
browser.get(url)

path = "WebApp/static/img/"
browser.save_screenshot(path+viewfilename)
print ('done')
sys.stdout.flush()
input()
browser.quit()