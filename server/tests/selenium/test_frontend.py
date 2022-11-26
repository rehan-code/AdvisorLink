import time
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

SLEEP_TIME = 3
LONG_SLEEP_TIME = 5

# Setup chrome options
print('Setting up chromedriver options...')
chrome_options = Options()

if ( len(sys.argv) > 1 and sys.argv[1] == '--headless' ):
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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navigate to website
print('Navigating to website...')
driver.get('http://www.advisorlink.ml/')


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

# TEST 2 - ADD A WINTER COURSE
# Select 'W2023' in term dropdown
print('2.1 Switching to W2023 schedule...')
select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/select'))
select.select_by_visible_text('Winter 2023')
time.sleep(LONG_SLEEP_TIME)

# Search for course 'Management Accounting'
print('2.2 Searching: \'Management Accounting\'...')
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
print('2.3 Adding to schedule: \'Management Accounting\'...')
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[5]/button")
link.click()
time.sleep(SLEEP_TIME)

# TEST 3 - SWITCH TO EXAM SCHEDULE
# Select 'F2022' in term dropdown
print('3.1 Switching to F2022 schedule...')
select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/select'))
select.select_by_visible_text('Fall 2022')
time.sleep(LONG_SLEEP_TIME)

# Search for course 'Management Accounting'
print('3.2 Searching: \'Calculus\'...')
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input').clear()
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input')
search_box.send_keys('Calculus')
time.sleep(SLEEP_TIME)

# Press search
search_box.send_keys(Keys.RETURN)
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/div/button")
link.click()
time.sleep(SLEEP_TIME)

# Add course to schedule
print('3.3 Adding to schedule: \'Calculus\'...')
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[5]/button")
link.click()
time.sleep(SLEEP_TIME)

# Switch to exam schedule
print('3.4 Switching to exam schedule...')
link2 = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div/div[4]/div/div[2]/button[1]')
link2.click()
time.sleep(SLEEP_TIME * 2)

# Switch back to Weekly schedule
print('3.5 Switching to weekly schedule...')
link2 = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div/div[4]/div/div[2]/button[1]')
link2.click()
time.sleep(SLEEP_TIME * 2)

# TEST 4 - EXPORT FUNCTIONALITY
# Scroll to visual calendar
# print('4.1 Scrolling to visual calendar...')
# element = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[3]/div/div[2]/button[2]')
# driver.execute_script("arguments[0].scrollIntoView(true);", element)
# time.sleep(SLEEP_TIME*2)

# Export calendar
print('4. Exporting calendar...')
link2 = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div/div[4]/div/div[2]/button[2]")
link2.click()
time.sleep(LONG_SLEEP_TIME)

# TEST 5 - SEARCH BY COURSE NAME
# Select 'Search by Course Name' in search query dropdown
print('5.1 Switching to \'Search by Course Name\'...')
select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/div/select'))
select.select_by_visible_text('Search by Course Name')
time.sleep(5)

# Search for course 'Soil Management'
print('5.2 Searching: \'Soil Management\'...')
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input').clear()
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input')
search_box.send_keys('Soil Management')
time.sleep(SLEEP_TIME)

# Press search
search_box.send_keys(Keys.RETURN)
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/div/button")
link.click()
time.sleep(SLEEP_TIME)

# Add course to schedule
print('5.3 Adding to schedule: \'Soil Management\'...') ##
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[5]/button")
link.click()
time.sleep(SLEEP_TIME)

# Scroll to visual calendar
print('5.4 Scrolling to visual calendar...')
element = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div/div[4]/div/div[1]/h1')
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(SLEEP_TIME * 2)

# TEST 6 - SEARCH BY COURSE CODE
# Select 'Search by Course Name' in search query dropdown
print('6.1 Switching to \'Search by Course Code\'...')
select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/div/select'))
select.select_by_visible_text('Search by Course Code')
time.sleep(LONG_SLEEP_TIME)

# Search for course 'ARTH 3210'
print('6.2 Searching: \'3210\'...')
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input').clear()
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input')
search_box.send_keys('3210')
time.sleep(SLEEP_TIME)

# Press search
search_box.send_keys(Keys.RETURN)
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/div/button")
link.click()
time.sleep(SLEEP_TIME)

# Add course to schedule
print('6.3 Adding to schedule: \'ARTH 3210\'...')
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[5]/button")
link.click()
time.sleep(SLEEP_TIME)

# Scroll to visual calendar
print('6.4 Scrolling to visual calendar...')
element = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div/div[4]/div/div[1]/h1')
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(SLEEP_TIME * 2)

# SEARCH BY INSTRUCTOR
# choose Search by Instructor in the dropdown
select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/div/select'))
select.select_by_visible_text('Search by Instructor')
time.sleep(LONG_SLEEP_TIME)

# Search for course by instructor 'CIS 2500'
# print('2.2 Searching: \'CIS 2500\'...')
# search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input').clear()
# search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input')
# search_box.send_keys('2500')
# time.sleep(SLEEP_TIME)

# Press search
# search_box.send_keys(Keys.RETURN)
# link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/div/button")
# link.click()
# time.sleep(SLEEP_TIME)

# Add course to schedule
# print('2.3 Adding to schedule: \'CIS 2500\'...')
# link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[5]/button")
# link.click()

# Scroll to visual calendar
# print('3.1 Scrolling to visual calendar...')
# element = driver.find_element(By.XPATH, '/html/body/div/div/main/div[2]/div/div/div[4]/div/div[1]/h1')
# driver.execute_script("arguments[0].scrollIntoView(true);", element)
# time.sleep(SLEEP_TIME)

# TEST 7 - ABOUT US
# Navigate to calendar page
print('7. Navigating to "About Us" page...')
link = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div/div[2]/a")
link.click()
time.sleep(LONG_SLEEP_TIME + 1)

print('\nAll tests completed.')
driver.quit()
