from selenium import webdriver

driver1 = webdriver.Firefox()
driver2 = webdriver.Chrome()

driver1.get("https://demoqa.com/automation-practice-form")
driver2.get("https://demoqa.com/automation-practice-form")

driver1.quit()
driver2.quit()
