import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

# chrome webdriver
driver = webdriver.Chrome()
driver.maximize_window()

def setup():
    try:
        # navigate to login
        driver.get("https://www.instagram.com/accounts/login/")
        # wait for the username field to show up
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")

        username.send_keys(os.getenv("INSTA_USER"))
        password.send_keys(os.getenv("INSTA_PASS"))
        password.send_keys(Keys.RETURN)

        # wait for the not now button to show up
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@role="button" and text()="Not now"]')
            )
        )
        not_now_button = driver.find_element(
            By.XPATH, '//div[@role="button" and text()="Not now"]'
        )
        not_now_button.click()

        # wait for the not now button to show up
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Not Now"]'))
        )
        not_now_button = driver.find_element(By.XPATH, '//button[text()="Not Now"]')
        not_now_button.click()
    except Exception as e:
        print(f"An error occurred: {e}")

def post_video(video_path):
    try:
        # wait for the create button to show up
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Create"]'))
        )
        new_post_button = driver.find_element(By.XPATH, '//span[text()="Create"]')
        new_post_button.click()

        # wait for the upload button to show up
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[text()="Select from computer"]')
            )
        )
        upload = driver.find_element(By.XPATH, '//button[text()="Select from computer"]')
        upload.click()

        # next part will be diff depending on host, will hold off on this for now
        time.sleep(100)

    except Exception as e:
        print(f"An error occurred: {e}")

def quit_insta():
    driver.quit()

setup()
post_video("test.mp4")