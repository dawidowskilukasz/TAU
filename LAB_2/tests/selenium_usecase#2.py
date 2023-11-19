from selenium import webdriver


def test(driver):
    driver.get("https://www.saucedemo.com/")

    driver.quit()


driver_firefox = webdriver.Firefox()

test(driver_firefox)

driver_chrome = webdriver.Chrome()

test(driver_chrome)
