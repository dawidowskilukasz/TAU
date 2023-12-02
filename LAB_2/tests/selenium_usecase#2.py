from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test(driver):
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    password.send_keys(Keys.ENTER)

    backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    backpack.click()

    cart_button = driver.find_element(By.ID, "shopping_cart_container")
    cart_button.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("lukasz")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("dawidowski")

    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("12/123")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()

    time.sleep(2)

    driver.close()
    driver.quit()


driver_firefox = webdriver.Firefox()

test(driver_firefox)

driver_chrome = webdriver.Chrome()

test(driver_chrome)
