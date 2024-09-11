from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# chrome webdriver
driver = webdriver.Chrome()

# navigate to login
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

# Input username and password
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

username.send_keys("brainrotgen1") # 😴
password.send_keys("Tyler1738!")
password.send_keys(Keys.RETURN)
time.sleep(5)

# close save pass popup
try:
    not_now_button = driver.find_element(By.XPATH, '//div[@role="button" and text()="Not now"]')
    not_now_button.click()
except Exception as e:
    print(f"An error occurred: {e}")
time.sleep(2)

# another not now
try:
    not_now_button = driver.find_element(By.XPATH, '//button[text()="Not Now"]')
    not_now_button.click()
except Exception as e:
    print(f"An error occurred: {e}")
time.sleep(3)

# navigate to the create button
try:
    new_post_button = driver.find_element(By.XPATH, '//span[text()="Create"]')
    new_post_button.click()
except Exception as e:
    print(f"An error occurred: {e}")
time.sleep(2)

# from computer
try:
    upload = driver.find_element(By.XPATH, '//button[text()="Select from computer"]')
    upload.click()
except Exception as e:
    print(f"An error occurred: {e}")
time.sleep(4)

# upload video here, code will be different depending on host so will hold out for now


# close the browser
driver.quit()
