from selenium import webdriver
from selenium.webdriver.common.by import By

# Please note:
# In order to run this test there should be a comment already written
# on the test user's profile. If there is not one, Please run test #5.

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
your_listings_button = buttons[12] # clicks Seller Profile button
your_listings_button.click()

driver.implicitly_wait(15)

buttons = driver.find_elements(By.TAG_NAME, 'button')
reply_button = buttons[1] # button to reply to the first comment
reply_button.click()

driver.implicitly_wait(10)

comment = driver.find_element(By.ID, value="comment")
comment.send_keys('this is a new reply')

submit = driver.find_element(By.ID, 'submit')
submit.click()

driver.quit()