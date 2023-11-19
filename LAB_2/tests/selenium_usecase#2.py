from selenium import webdriver

driver1 = webdriver.Firefox()
driver2 = webdriver.Chrome()

driver1.get("https://www.saucedemo.com/")
driver2.get("https://www.saucedemo.com/")

driver1.quit()
driver2.quit()
