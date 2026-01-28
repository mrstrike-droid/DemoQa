from datetime import time
import logging
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

logger = logging.getLogger("log_event")
logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DemoQA:
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.implicitly_wait(10)
        self._url = "http://demoqa.com/"

    def open_page(self):
        self._driver.get(self._url)
        self._driver.maximize_window()

    def text_box(self):
        first_clickable_object = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[1]")))
        first_clickable_object.click()
        time.sleep(1)
        text_box = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Text Box')]")))
        text_box.click()
        time.sleep(1)
        full_name = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'userName')]")))
        full_name.send_keys("<NAME>")
        time.sleep(1)
        email = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id, 'userEmail')]")))
        email.send_keys("123@gmail.com")
        time.sleep(1)
        current_address = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[contains(@id, 'currentAddress')]")))
        current_address.send_keys("123 Main St")
        time.sleep(1)
        permanent_address = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[contains(@id, 'permanentAddress')]")))
        permanent_address.send_keys("33 West St")
        time.sleep(1)
        submit_button = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'btn btn-primary')]")))
        submit_button.click()
        time.sleep(1)
        result = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@id, 'output')]")))
        logger.info(result.text)

    def check_box(self):
        check_box = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Check Box')]")))
        check_box.click()
        time.sleep(1)
        button_collapse_1 = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/span/button")))
        button_collapse_1.click()
        time.sleep(1)
        button_collapse_2 = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/ol/li[1]/span/button")))
        button_collapse_2.click()
        time.sleep(1)





if __name__ == "__main__":
    test1 = DemoQA()
    test1.open_page()
    test1.text_box()
    test1.check_box()

