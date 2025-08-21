from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://localhost:5000")

# the following commented-out code is for creating the sjohn user; not needed if user has already been created!
driver.implicitly_wait(5)

buttons = driver.find_elements(By.TAG_NAME, 'button')
signup_button = buttons[1]

signup_button.click() # routes to signup page

driver.implicitly_wait(5)

id = driver.find_element(By.ID, value='id')
description = driver.find_element(By.ID, value='description')
rep_name = driver.find_element(By.ID, value='representative_name')
email = driver.find_element(By.ID, value='email')
address = driver.find_element(By.ID, value='address')
phone = driver.find_element(By.ID, value='phone')
city = driver.find_element(By.ID, value='city')
state = driver.find_element(By.ID, value='state')
website = driver.find_element(By.ID, value='website')
password = driver.find_element(By.ID, value='passwd')
password_confirm = driver.find_element(By.ID, value='passwd_confirm')

id.send_keys('sjohn')
description.send_keys('Sage Brewing Company')
rep_name.send_keys('Sage Johnson')
email.send_keys('sage@hotmail.com')
address.send_keys('Metropolitan State University of Denver 890 Auraria Parkway')
phone.send_keys('3035565740')
city.send_keys('Denver')
state.send_keys('Colorado')
website.send_keys('msudenver.edu')
password.send_keys('1')
password_confirm.send_keys('1')

submit = driver.find_element(By.ID, 'submit')
submit.click() # signs user up with given info above

driver.implicitly_wait(5)

buttons = driver.find_elements(By.TAG_NAME, 'button')
login_button = buttons[0]
login_button.click() # redirects to login page

driver.implicitly_wait(5)

username = driver.find_element(By.ID, value='id')
password = driver.find_element(By.ID, value='passwd')

username.send_keys('sjohn')
password.send_keys('1')

submit = driver.find_element(By.ID, 'submit')
submit.click() # logs sjohn into the app

driver.implicitly_wait(5)

# need to accept last offer
buttons = driver.find_elements(By.TAG_NAME, 'button')
newest_offer_button = buttons[len(buttons) - 3]

newest_offer_button.click()

# buttons for confirmation page
buttons = driver.find_elements(By.TAG_NAME, 'button')
signout_button = buttons[1] # last button, which is signout

signout_button.click() # offer is now accepted!

driver.quit()
