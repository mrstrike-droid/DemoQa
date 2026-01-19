import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


def login():
    driver = webdriver.Chrome()
    driver.get("http://demoqa.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").send_keys("<PASSWORD>")
    driver.find_element(By.NAME, "submit").click()
    driver.implicitly_wait(5)

if __name__ == "__main__":
    login()