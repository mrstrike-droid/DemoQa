from datetime import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time



def login():
    driver = webdriver.Chrome()
    driver.get("http://demoqa.com/")
    driver.maximize_window()
    time.sleep(3)
    first_clickable_object = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[1]")))
    first_clickable_object.click()
    time.sleep(3)
    text_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'text')]")))
    text_box.click()
    time.sleep(3)

if __name__ == "__main__":
    login()