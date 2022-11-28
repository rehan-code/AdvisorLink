import time
import unittest
import argparse

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
    time.sleep(SLEEP_TIME)

    # Search for course 'CIS 2750'
    print('1.2 Searching: \'CIS 2750\'...')
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input')
    search_box.send_keys('CIS 2750')
    time.sleep(SLEEP_TIME)

    # Press search
    search_box.send_keys(Keys.RETURN)
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/div/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Add course to schedule
    print('1.3 Adding to schedule: \'CIS 2750\'...')
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[6]/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Search for course 'Management Accounting'
    print('1.4 Searching: \'Management Accounting\'...')
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input').clear()
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input')
    search_box.send_keys('Management Accounting')
    time.sleep(SLEEP_TIME)

    # Press search
    search_box.send_keys(Keys.RETURN)
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/div/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Add course to schedule
    print('1.5 Adding to schedule: \'Management Accounting\'...')
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[6]/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Scroll to Courses
    print('1.6 Scrolling to Courses...')
    element = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[4]')
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(SLEEP_TIME)

    # Remove course to schedule
    print('1.7 Deleting from schedule: \'Management Accounting\'...')
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/div[3]/div/div/table/tbody/tr[2]/td[5]/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Scroll to Courses
    print('1.8 Scrolling to Courses...')
    element = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[4]')
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(SLEEP_TIME)

    print('\n...Test 1 passed.\n')


# TEST 2 - ADD WINTER 2023 COURSES
def add_winter_courses(driver):

    print('\nTest 2 - Add Winter 2022 Courses\n')

    # Navigate to calendar page
    print('2.1 Navigating to calendar page...')
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/button")
    link.click()
    time.sleep(SLEEP_TIME)
    
    # Select 'W2023' in term dropdown
    print('2.2 Switching to W2023 schedule...')
    select = Select(driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[1]/div/select'))
    select.select_by_visible_text('Winter 2023')
    time.sleep(SLEEP_TIME)

    # Search for course 'Management Accounting'
    print('2.3 Searching: \'Management Accounting\'...')
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input').clear()
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input')
    search_box.send_keys('Management Accounting')
    time.sleep(SLEEP_TIME)

    # Press search
    search_box.send_keys(Keys.RETURN)
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/div/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Add course to schedule
    print('2.4 Adding to schedule: \'Management Accounting\'...')
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[6]/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Scroll to Courses
    print('2.5 Scrolling to Courses...')
    element = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[4]')
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(SLEEP_TIME)

    print('\n...Test 2 passed.\n')

def switch_schedule(driver):

    print('\nTest 3 - Switching Schedules\n')

    # Navigate to calendar page
    print('3.1 Navigating to calendar page...')
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/button")
    link.click()
    time.sleep(LONG_SLEEP_TIME)

    # Switch to F2022 schedule
    print('3.2 Switching to F2022 schedule...')
    select = Select(driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[1]/div/select'))
    select.select_by_visible_text('Fall 2022')
    time.sleep(LONG_SLEEP_TIME)

    # Search for course 'Calculus'
    print('3.3 Searching: \'Calculus\'...')
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input').clear()
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input')
    search_box.send_keys('Calculus')
    time.sleep(SLEEP_TIME)

    # Press search
    search_box.send_keys(Keys.RETURN)
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/div/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Add course to schedule
    print('3.4 Adding to schedule: \'Calculus\'...')
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[6]/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Switch to exam schedule
    print('3.5 Switching to exam schedule...')
    link = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[5]/div/div[2]/button[1]')
    link.click()
    time.sleep(SLEEP_TIME * 2)

    # Switch to weekly exam view
    print('3.6 Switching to week exam view...')
    link = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[5]/div/div[1]/div[2]/div/div[1]/div[3]/button[2]')
    link.click()
    time.sleep(SLEEP_TIME * 2)

    # Switch back to monthly exam view
    print('3.7 Switching back monthly exam view...')
    link = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[5]/div/div[1]/div[2]/div/div[1]/div[3]/button[1]')
    link.click()
    time.sleep(SLEEP_TIME)

    # Navigate to previous month
    print('3.8 Navigate to the previous month...')
    link = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[5]/div/div[1]/div[2]/div/div[1]/div[1]/button')
    link.click()
    time.sleep(SLEEP_TIME)

    # Navigate to next month
    print('3.9 Navigate to next month...')
    link = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[5]/div/div[1]/div[2]/div/div[1]/div[3]/button[3]')
    link.click()
    time.sleep(SLEEP_TIME)

    # Switch back to Weekly schedule
    print('3.10 Switching to weekly schedule...')
    link = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[5]/div/div[2]/button[1]')
    link.click()
    time.sleep(SLEEP_TIME)

    print('\n...Test 3 passed.\n')

def export_schedule(driver):

    print('\nTest 4 - Export Functionality\n')

    # Navigate to calendar page
    print('4.1 Navigating to calendar page...')
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Search for course 'Calculus'
    print('4.2 Searching: \'Calculus\'...')
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input').clear()
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input')
    search_box.send_keys('Calculus')
    time.sleep(SLEEP_TIME)

    # Press search
    search_box.send_keys(Keys.RETURN)
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/div/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Add course to schedule
    print('4.3 Adding to schedule: \'Calculus\'...')
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[6]/button")
    link.click()
    time.sleep(SLEEP_TIME)
    
    # Export calendar
    print('4.4 Exporting calendar...')
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[5]/div/div[2]/button[2]")
    link.click()
    time.sleep(LONG_SLEEP_TIME)

    print('\n...Test 4 passed.\n')

def search_by_course_name(driver):

    print('\nTest 5 - Search by Course Name\n')

    # Navigate to calendar page
    print('5.1 Navigating to calendar page...')
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/button")
    link.click()
    time.sleep(SLEEP_TIME)
    
    # Select 'Search by Course Name' in search query dropdown
    print('5.2 Switching to \'Search by Course Name\'...')
    select = Select(driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/div/select'))
    select.select_by_visible_text('Search by Course Name')
    time.sleep(SLEEP_TIME)

    # Search for course 'Soil Management'
    print('5.3 Searching: \'Soil Management\'...')
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input').clear()
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input')
    search_box.send_keys('Soil Management')
    time.sleep(SLEEP_TIME)

    # Press search
    search_box.send_keys(Keys.RETURN)
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/div/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Add course to schedule
    print('5.4 Adding to schedule: \'Soil Management\'...') ##
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[6]/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Scroll to visual calendar
    print('5.5 Scrolling to visual calendar...')
    element = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[5]/div/div[1]/div[1]/div/div/div[2]/div/table/thead/tr/th/div/div/table/thead/tr/th[1]')
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(SLEEP_TIME * 2)
    
    print('\n...Test 5 passed.\n')

def search_by_course_code(driver):

    print('\nTest 6 - Search by Course Code\n')

    # Navigate to calendar page
    print('6.1 Navigating to calendar page...')
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Select 'Search by Course Code' in search query dropdown
    print('6.2 Switching to \'Search by Course Code\'...')
    select = Select(driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/div/select'))
    select.select_by_visible_text('Search by Course Code')
    time.sleep(SLEEP_TIME)

    # Search for course 'ARTH 3210'
    print('6.3 Searching: \'3210\'...')
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input').clear()
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input')
    search_box.send_keys('3210')
    time.sleep(SLEEP_TIME)

    # Press search
    search_box.send_keys(Keys.RETURN)
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/div/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Add course to schedule
    print('6.4 Adding to schedule: \'ARTH 3210\'...')
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[6]/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Scroll to visual calendar
    print('6.5 Scrolling to visual calendar...')
    element = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[5]/div/div[1]/div[1]/div/div/div[2]/div/table/thead/tr/th/div/div/table/thead/tr/th[1]')
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(SLEEP_TIME * 2)
    
    print('\n...Test 6 passed.\n')

def search_by_instructor(driver):
    
    print('\nTest 7 - Search by Instructor\n')

    # Navigate to calendar page
    print('7.1 Navigating to calendar page...')
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/button")
    link.click()
    time.sleep(SLEEP_TIME)
    
    # choose Search by Instructor in the dropdown
    select = Select(driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/div/select'))
    select.select_by_visible_text('Search by Instructor')
    time.sleep(SLEEP_TIME)

    # Search for course by instructor 'stacey'
    print('7.2 Searching: \'stacey\'...')
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input').clear()
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input')
    search_box.send_keys('stacey')
    time.sleep(SLEEP_TIME)

    # Press search
    search_box.send_keys(Keys.RETURN)
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/div/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Add course to schedule
    print('7.3 Adding to schedule: \'Topics in Computer Science\'...')
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[6]/button")
    link.click()

    # Scroll to visual calendar
    print('7.4 Scrolling to visual calendar...')
    element = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[5]/div/div[1]/div[1]/div/div/div[2]/div/table/thead/tr/th/div/div/table/thead/tr/th[1]')
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(SLEEP_TIME)
    
    print('\n...Test 7 passed.\n')

def course_dropdown(driver):

    print('\nTest 8 - Display Course Details\n')

    # Navigate to calendar page
    print('8.1 Navigating to calendar page...')
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/button")
    link.click()
    time.sleep(SLEEP_TIME)

    # Search for course 'ARTH 3210'
    print('8.2 Searching: \'calculus\'...')
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input').clear()
    search_box = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/input')
    search_box.send_keys('calculus')
    time.sleep(SLEEP_TIME)

    # Press search
    search_box.send_keys(Keys.RETURN)
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[1]/div/div/div/form/div/button")
    link.click()
    time.sleep(SLEEP_TIME)
    
    # Display course information
    print('8.3 Display course information...')
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[1]")
    link.click()
    time.sleep(SLEEP_TIME)

    # Minimize course information
    print('8.4 Minimize course information...')
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[1]")
    link.click()
    time.sleep(SLEEP_TIME)

    print('\n...Test 8 passed.\n')
    
def course_suggestion(driver):

    print('\nTest 9 - Suggest Courses\n')

    # Navigate to calendar page
    print('9.1 Navigating to calendar page...')
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/button")
    link.click()
    time.sleep(SLEEP_TIME)

    print('9.2 Applying Tues/Thurs filter...')
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[2]/div/div/button[2]")
    link.click()
    time.sleep(SLEEP_TIME)

    print('9.3 Suggesting courses...')
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[2]/div/button")
    link.click()
    time.sleep(SLEEP_TIME)

    print('9.4 Display course information...')
    link = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[1]")
    link.click()
    time.sleep(SLEEP_TIME)

    print('\n...Test 9 passed.\n')

def view_about_us(driver):
    print('10. Navigating to "About Us" page...')
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div/div[2]/a")
    link.click()
    time.sleep(LONG_SLEEP_TIME + 1)

    print('\n...Test 10 passed.\n')

class TestAdvisorLink(unittest.TestCase):
    HEADLESS = 'false'

    #Driver initialization
    def setUp(self):

        # Setup chrome options
        print('\nSetting up chromedriver options...')

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        
        if (self.HEADLESS == 'true'):
            chrome_options.add_argument("--headless")
            
        chrome_options.add_argument("--disable-gpu")

        # Choose Chrome Browser
        print('Choosing Chrome browser...')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # Navigate to website
        print('Navigating to ' + WEBSITE + '...')
        self.driver.get(WEBSITE)

    def test_1_add_remove_fall_courses(self):
        add_remove_fall_courses(self.driver)

    def test_2_add_winter_courses(self):
        add_winter_courses(self.driver)

    def test_3_switch_schedule(self):
        switch_schedule(self.driver)

    def test_4_export_schedule(self):
        export_schedule(self.driver)

    def test_5_search_by_course_name(self):
        search_by_course_name(self.driver)

    def test_6_search_by_course_code(self):
        search_by_course_code(self.driver)

    def test_7_search_by_instructor(self):
        search_by_instructor(self.driver)

    def test_8_course_dropdown(self):
        course_dropdown(self.driver)

    def test_9_course_suggestion(self):
        course_suggestion(self.driver)

    def test_10_view_about_us(self):
        view_about_us(self.driver)

    #Clean up
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Selenium testing program for Advisorlink.ml')
    parser.add_argument('-headless', action='store_true', help='turns on headless mode', required=False)
    parser.add_argument('-t', help='choose a specific test case to run', required=False)

    args = parser.parse_args()    

    # Run tests in gui-less mode
    if (args.headless):
        TestAdvisorLink.HEADLESS = 'true'

    # Run specific test, if specified
    if (args.t):
        
        try:
            testToRun = unittest.TestSuite()
            testToRun.addTest(TestAdvisorLink(args.t) )

            print('test_frontend: running test case \'' + args.t + '\'...')
            unittest.TextTestRunner().run(testToRun)

        except:
            print('ERROR - No test case \'' + args.t + '\' exists.')

    # Run all tests
    else:
        testSuite = unittest.TestLoader().loadTestsFromTestCase(TestAdvisorLink)
        allTests = unittest.TestSuite(testSuite)
        unittest.TextTestRunner().run(allTests) 