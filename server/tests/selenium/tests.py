import time
import sys
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

SLEEP_TIME = 3
LONG_SLEEP_TIME = 5

class TestAdvisorLink(unittest.TestCase):
    def setUp(self):
        # Setup chrome options
        print('Setting up chromedriver options...')
        chrome_options = Options()

        if ( len(sys.argv) > 1  ):
            if ( sys.argv[1] == '--headless' ):
                print('DEBUG: Running in gui-less mode...')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-gpu")

        else:
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument("--disable-gpu")

        # Set path to chromedriver
        print('Setting path to chromedriver...')

        # Choose Chrome Browser
        print('Choosing Chrome browser...')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # Navigate to website
        print('Navigating to website...')
        driver.get('http://www.advisorlink.ml/')

    def test_example(self):
        actual = example('Hello')
        expected = 'val has exactly 5 characters'
        self.assertEqual(actual, expected)

# TEST 1 - ADD/REMOVE FALL 2022 COURSES
# Navigate to calendar page
print('1.1 Navigating to calendar page...')
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/button")
link.click()
time.sleep(LONG_SLEEP_TIME)

# Search for course 'CIS 2750'
print('1.2 Searching: \'CIS 2750\'...')
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input')
search_box.send_keys('CIS 2750')
time.sleep(SLEEP_TIME)

# Press search
search_box.send_keys(Keys.RETURN)
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/div/button")
link.click()
time.sleep(SLEEP_TIME)

# Add course to schedule
print('1.3 Adding to schedule: \'CIS 2750\'...')
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[5]/button")
link.click()
time.sleep(SLEEP_TIME)

# Search for course 'Management Accounting'
print('1.4 Searching: \'Management Accounting\'...')
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input').clear()
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input')
search_box.send_keys('Management Accounting')
time.sleep(SLEEP_TIME)

# Press search
search_box.send_keys(Keys.RETURN)
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/div/button")
link.click()
time.sleep(SLEEP_TIME)

# Add course to schedule
print('1.5 Adding to schedule: \'Management Accounting\'...')
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[5]/button")
link.click()
time.sleep(SLEEP_TIME)

# Remove course to schedule
print('1.6 Deleting from schedule: \'Management Accounting\'...')
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/div[3]/div/div/table/tbody/tr[2]/td[5]/button")
link.click()
time.sleep(SLEEP_TIME)