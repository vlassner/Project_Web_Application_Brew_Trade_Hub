from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://localhost:5000")

driver.implicitly_wait(5)

buttons = driver.find_elements(By.TAG_NAME, 'button')
login_button = buttons[0]

login_button.click()

driver.implicitly_wait(5)

confirm_button = driver.find_elements(By.TAG_NAME, 'button')

username = driver.find_element(By.ID, value="id")
password = driver.find_element(By.ID, value="passwd")

username.send_keys('tmota')
password.send_keys('1')

submit = driver.find_element(By.ID, 'submit')

submit.click()

driver.implicitly_wait(5)

buttons = driver.find_elements(By.TAG_NAME, 'button')
create_offer_button = buttons[0]

create_offer_button.click()

driver.implicitly_wait(5)

description = driver.find_element(By.ID, 'description')
year = driver.find_element(By.ID, 'year')
productType = driver.find_element(By.ID, 'productType')
brand = driver.find_element(By.ID, 'brand')
price = driver.find_element(By.ID, 'price')

description.send_keys('SeleniumInYear')
year.send_keys('2024')
productType.send_keys('Project2')
brand.send_keys('ButterBeer')
price.send_keys('9999.99')

submit = driver.find_element(By.ID, 'submit')
submit.click() # creates offer under tmota's name

driver.implicitly_wait(10)

buttons = driver.find_elements(By.TAG_NAME, 'button')

signout_button = buttons[12]
signout_button.click() # signs out after creating offer

driver.quit()