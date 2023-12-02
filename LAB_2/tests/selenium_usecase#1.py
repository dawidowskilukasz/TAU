from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test(driver):
    driver.maximize_window()
    driver.get("https://demoqa.com/automation-practice-form")

    user_first_name = driver.find_element(By.ID, "firstName")
    user_first_name.send_keys('John')

    user_last_name = driver.find_element(By.ID, "lastName")
    user_last_name.send_keys('Smith')

    user_email = driver.find_element(By.ID, "userEmail")
    user_email.send_keys('john.smith@domain.com')

    user_gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-3']")
    user_gender.click()

    user_number = driver.find_element(By.ID, "userNumber")
    user_number.send_keys('1234567891')

    user_birthdate = driver.find_element(By.ID, "dateOfBirthInput")
    user_birthdate.click()
    user_birthdate_date = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    user_birthdate_date.click()
    user_birthdate_year = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[112]")
    user_birthdate_year.click()
    user_birthdate_month = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[8]")
    user_birthdate_month.click()
    user_birthdate_day = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[5]")
    user_birthdate_day.click()

    user_subject = driver.find_element(By.ID, "subjectsInput")
    user_subject.send_keys("Com")
    user_subject.click()
    user_subject.send_keys(Keys.ENTER)

    user_hobbies = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[7]/div[2]/div[2]")
    user_hobbies.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    user_address = driver.find_element(By.ID, "currentAddress")
    user_address.send_keys("somewhere 15/58")
    user_subject.send_keys(Keys.ENTER)

    driver.quit()


driver_firefox = webdriver.Firefox()

test(driver_firefox)

driver_chrome = webdriver.Chrome()

test(driver_chrome)
