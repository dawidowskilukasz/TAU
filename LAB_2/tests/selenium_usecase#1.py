import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Configure the logging module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test(driver):
    logger.info("Navigating to the website...")
    driver.get("https://demoqa.com/automation-practice-form")

    user_first_name = driver.find_element(By.ID, "firstName")
    user_first_name.send_keys('John')
    logger.info("Entered first name")

    user_last_name = driver.find_element(By.ID, "lastName")
    user_last_name.send_keys('Smith')
    logger.info("Entered last name")

    user_email = driver.find_element(By.ID, "userEmail")
    user_email.send_keys('john.smith@domain.com')
    logger.info("Entered email")

    user_gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-3']")
    user_gender.click()
    logger.info("Selected gender")

    user_number = driver.find_element(By.ID, "userNumber")
    user_number.send_keys('1234567891')
    logger.info("Entered phone number")

    user_birthdate = driver.find_element(By.ID, "dateOfBirthInput")
    user_birthdate.click()
    logger.info("Clicked on the birthdate input")

    user_birthdate_date = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    user_birthdate_date.click()
    logger.info("Opened datepicker")

    user_birthdate_year = driver.find_element(By.XPATH,
                                              "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[112]")
    user_birthdate_year.click()
    logger.info("Selected birthdate year")

    user_birthdate_month = driver.find_element(By.XPATH,
                                               "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[8]")
    user_birthdate_month.click()
    logger.info("Selected birthdate month")

    user_birthdate_day = driver.find_element(By.XPATH,
                                             "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[5]")
    user_birthdate_day.click()
    logger.info("Selected birthdate day")

    user_subject = driver.find_element(By.ID, "subjectsInput")
    user_subject.send_keys("Com")
    user_subject.click()
    user_subject.send_keys(Keys.ENTER)
    logger.info("Entered subject")

    user_hobbies = driver.find_element(By.XPATH,
                                       "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[7]/div[2]/div[2]")
    user_hobbies.click()
    logger.info("Selected hobbies")

    user_address = driver.find_element(By.ID, "currentAddress")
    user_address.send_keys("somewhere 15/58")
    user_subject.send_keys(Keys.ENTER)
    logger.info("Entered address")

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
