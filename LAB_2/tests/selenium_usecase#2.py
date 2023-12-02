import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test(driver):
    logger.info("Navigating to the website...")
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    logger.info("Entered username")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    password.send_keys(Keys.ENTER)
    logger.info("Entered password and pressed Enter")

    backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    backpack.click()
    logger.info("Added a backpack to the cart")

    cart_button = driver.find_element(By.ID, "shopping_cart_container")
    cart_button.click()
    logger.info("Clicked on the shopping cart")

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    logger.info("Clicked on the checkout button")

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("lukasz")
    logger.info("Entered first name")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("dawidowski")
    logger.info("Entered last name")

    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("12/123")
    logger.info("Entered postal code")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    logger.info("Clicked on the continue button")

    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()
    logger.info("Clicked on the finish button")

    logger.info("Test completed successfully")

    driver.close()
    driver.quit()

    logger.info("Closed browser")


logger.info("Running the test for Firefox")
driver_firefox = webdriver.Firefox()

test(driver_firefox)

logger.info("Running the test for Chrome")
driver_chrome = webdriver.Chrome()

test(driver_chrome)
