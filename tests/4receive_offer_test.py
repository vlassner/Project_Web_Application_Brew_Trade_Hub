from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://localhost:5000")

driver.implicitly_wait(10)

buttons = driver.find_elements(By.TAG_NAME, 'button')
login_button = buttons[0]
login_button.click() # redirects to login page

driver.implicitly_wait(10)

username = driver.find_element(By.ID, value="id")
password = driver.find_element(By.ID, value="passwd")

username.send_keys('sjohn')
password.send_keys('1')

submit = driver.find_element(By.ID, 'submit')
submit.click()

driver.implicitly_wait(15)

buttons = driver.find_elements(By.TAG_NAME, 'button')
your_listings_button = buttons[2] # clicks your_listings button
your_listings_button.click()

driver.implicitly_wait(10)

buttons = driver.find_elements(By.TAG_NAME, 'button')
received_button = buttons[1]
received_button.click() # clicking the 'received' status button

driver.implicitly_wait(15)

buttons = driver.find_elements(By.TAG_NAME, 'button')
sign_out_button = buttons[2]
sign_out_button.click() # signs out

driver.quit()
