from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.advisorlink.ml/');
time.sleep(5) # Let the user actually see something!
link = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div/button");
link.click();
# search for courses
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input')
search_box.send_keys('CIS 2750')
time.sleep(5) # show the tester the input 
search_box.send_keys(Keys.RETURN)
link = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/div/button")
link.click();
time.sleep(5) # Let the user actually see something!
# add the course to the schedule
link = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[5]/button")
link.click()
# Now search by Course name 
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input').clear()
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input')
search_box.send_keys('Management Accounting')
time.sleep(5) # show the tester the input 
search_box.send_keys(Keys.RETURN)
# click the search button 
link = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/div/button")
link.click()
time.sleep(5) # show the tester the input 
# now add the course to the schedule 
link = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[5]/button")
link.click()
time.sleep(5) # show the tester the input 
#############################################################
# add course to winter term 
select = Select(driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/select'))
select.select_by_visible_text('Winter 2023')
time.sleep(8) # show the tester the input 
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input').clear()
search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/input')
search_box.send_keys('Management Accounting')
time.sleep(5) # show the tester the input 
search_box.send_keys(Keys.RETURN)
# click the search button 
link = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div[1]/div[1]/div/div/div/form/div/button")
link.click()
time.sleep(5) # show the tester the input 
# now add the course to the schedule 
link = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]/div/div/table/tbody/tr[1]/td[5]/button")
link.click()
############################################################
#print the schedule 
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5) # show the tester the input 
time.sleep(10) # show the tester the input 
link2 = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div[3]/div/div[2]/button")
link2.click()
time.sleep(5) # show the tester the input 
driver.quit()