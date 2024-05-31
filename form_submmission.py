from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fill_form(form_link):
    driver = webdriver.Firefox()
    driver.get(form_link)

    time.sleep(5)
    
    # Finding inputs
    items = driver.find_elements(By.XPATH, "//div[contains(@role, 'listitem')]")
    
    for item in items:
        inputs = item.find_elements(By.XPATH, ".//input[not(@type='hidden')] | .//textarea")
        title = item.find_element(By.XPATH, ".//span[contains(@class, 'M7eMe')]").text
        for input in inputs:
            role = input.get_attribute('role')
            if role and role == 'combobox':
                input.send_keys(10)
            elif 'code' in title:
                code = title.split(': ')[1]
                input.send_keys(code)
            else:
                input.send_keys('test')

    submit_btn = driver.find_element(By.XPATH, "//div[contains(@role, 'button')]")
    submit_btn.click()

    time.sleep(5)
    driver.save_screenshot('confirmation.png')