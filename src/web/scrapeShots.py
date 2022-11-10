# Created: October 25, 2022
# Last updated: October 25, 2022
# Author: Brendan Keane
# Purpose: Scrape shot chart data from NBAstats.com

# Terminal prompt to initialize remote web control on Chrome
# sudo /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9812 --user-data-dir=/Users/brendankeane/Desktop/mapping-social-movements/data/chromeprofile


# Packages
import re
import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
driver.get("https://www.nba.com/schedule")
assert "NBA Schedule" in driver.title
driver.refresh()


# # Pull text inside <source id="__NEXT_DATA__">...</script>
# def getShotScript():
#   return find_element(By.ID, "__NEXT_DATA__")

# # Extract play-by-play data
# def getPlayByPlay(exp):
#   return exp.match(exp, getShotScript().getText())

# # Connects to Chrome Driver based on port number
#     host = "localhost:" + str(sys.argv[1])
#     opt = Options()
#     opt.add_experimental_option("debuggerAddress", host)
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
#     wait = WebDriverWait(driver, maxwait)

# # Connects to Chrome Driver based on port number
# host = "localhost:9812"
# opt = Options()
# opt.add_experimental_option("debuggerAddress", host)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
# wait = WebDriverWait(driver, 5)

# # Refresh to check if session is timed out
# driver.refresh()

# # Set up the Regex used to get play-by-play data
# playByPlay = re.compile("\"playByPlay\":{\"gameId\":\"\d+\",\"videoAvailable\":\d,\"actions\":\[\{.*\}\],")

