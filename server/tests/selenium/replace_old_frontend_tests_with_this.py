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
WEBSITE = 'http://www.advisorlink.ml/'

# TEST 1 - ADD/REMOVE FALL 2022 COURSES
def add_remove_fall_courses(driver):

    print('\nTest 1 - Add/Remove Fall 2022 Courses\n')

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

    print('\n...Test 1 passed.\n')


# TEST 2 - ADD WINTER 2023 COURSES
def add_winter_courses(driver):

    print('\nTest 2 - Add Winter 2022 Courses\n')

    # Navigate to calendar page
    print('2.1 Navigating to calendar page...')
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/button")
    link.click()
    time.sleep(LONG_SLEEP_TIME)
    
    # Select 'W2023' in term dropdown
    print('2.2 Switching to W2023 schedule...')
    select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/select'))
    select.select_by_visible_text('Winter 2023')
    time.sleep(LONG_SLEEP_TIME)

    # Search for course 'Management Accounting'
    print('2.3 Searching: \'Management Accounting\'...')
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
    print('2.4 Adding to schedule: \'Management Accounting\'...')
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[5]/button")
    link.click()
    time.sleep(SLEEP_TIME)

    print('\n...Test 2 passed.\n')

def switch_schedule():
    return

def export_schedule():
    return

def search_by_course_name():
    return

def search_by_course_code():
    return

def search_by_instructor():
    return

def view_about_us():
    return

class TestAdvisorLink(unittest.TestCase):

    #Driver initialization
    def setUp(self):

        # Setup chrome options
        print('\nSetting up chromedriver options...')

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")

        # Choose Chrome Browser
        print('Choosing Chrome browser...')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # Navigate to website
        print('Navigating to ' + WEBSITE + '...')
        self.driver.get(WEBSITE)

    def test_add_remove_fall_courses(self):
        add_remove_fall_courses(self.driver)

    def test_add_winter_courses(self):
        add_winter_courses(self.driver)

    def test_switch_schedule(self):
        switch_schedule(self.driver)

    def test_export_schedule(self):
        export_schedule(self.driver)

    def test_search_by_course_name(self):
        search_by_course_name(self.driver)

    def test_search_by_course_code(self):
        search_by_course_code(self.driver)

    def test_search_by_instructor(self):
        search_by_instructor(self.driver)

    def test_view_about_us(self):
        view_about_us(self.driver)

    #Clean up
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':

    # Run specific test, if specified
    if len(sys.argv) > 1:

        try:
            testToRun = unittest.TestSuite()
            testToRun.addTest(TestAdvisorLink(sys.argv[1]))

            print('test_frontend: running test case \'' + sys.argv[1] + '\'...')
            unittest.TextTestRunner().run(testToRun)

        except:
            print('ERROR - No test case \'' + sys.argv[1] + '\' exists.')

    # Run all tests
    else:
        print('test_frontend: running all tests...')
        print('\nNOTE - To specify a specific test, use: \n\t\'$ [python/python3] test_frontend [test_to_run]\'\n')
        unittest.main()