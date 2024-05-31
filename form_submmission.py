from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fill_form(form_link):
    driver = webdriver.Firefox()
    driver.get(form_link)

    time.sleep(5)
    
    # Find each input form
    items = driver.find_elements(By.XPATH, "//div[contains(@role, 'listitem')]")
    
    for item in items:

        # get the input field (or fields in case of date of birth) and the title of this input
        inputs = item.find_elements(By.XPATH, ".//input[not(@type='hidden')] | .//textarea")
        title = item.find_element(By.XPATH, ".//span[contains(@class, 'M7eMe')]").text

        for input in inputs:
            role = input.get_attribute('role')
            if role and role == 'combobox': # check if it is date of birth input
                input.send_keys(10)
            elif 'code' in title: # check if the input requires entering a code
                code = title.split(': ')[1] # extracting the code from the title
                input.send_keys(code)
            else: # other inputs
                input.send_keys('test')

    submit_btn = driver.find_element(By.XPATH, "//div[contains(@role, 'button')]") # get the submit button
    submit_btn.click()

    time.sleep(5)
    driver.save_screenshot('confirmation.png') # take screenshot