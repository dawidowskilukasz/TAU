import logging
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@given('User is on the demoqa.com automation practice form page')
def step_navigate_to_website(context):
    context.driver = webdriver.Firefox()
    logger.info("Navigating to the website...")
    context.driver.get("https://demoqa.com/automation-practice-form")

@when('User enters first name as "{first_name}"')
def step_enter_first_name(context, first_name):
    user_first_name = context.driver.find_element(By.ID, "firstName")
    user_first_name.send_keys(first_name)
    logger.info("Entered first name")

@when('User enters last name as "{last_name}"')
def step_enter_last_name(context, last_name):
    user_last_name = context.driver.find_element(By.ID, "lastName")
    user_last_name.send_keys(last_name)
    logger.info("Entered last name")

@when('User enters email as "{email}"')
def step_enter_email(context, email):
    user_email = context.driver.find_element(By.ID, "userEmail")
    user_email.send_keys(email)
    logger.info("Entered email")

@when('User selects gender')
def step_select_gender(context):
    user_gender = context.driver.find_element(By.XPATH, "//label[@for='gender-radio-3']")
    user_gender.click()
    logger.info("Selected gender")

@when('User enters phone number as "{phone_number}"')
def step_enter_phone_number(context, phone_number):
    user_number = context.driver.find_element(By.ID, "userNumber")
    user_number.send_keys(phone_number)
    logger.info("Entered phone number")

@when('User selects birthdate')
def step_select_birthdate(context):
    user_birthdate = context.driver.find_element(By.ID, "dateOfBirthInput")
    user_birthdate.click()
    logger.info("Clicked on the birthdate input")

    user_birthdate_date = context.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    user_birthdate_date.click()
    logger.info("Opened datepicker")

    user_birthdate_year = context.driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']/option[@value='2022']")
    user_birthdate_year.click()
    logger.info("Selected birthdate year")

    user_birthdate_month = context.driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']/option[@value='7']")
    user_birthdate_month.click()
    logger.info("Selected birthdate month")

    user_birthdate_day = context.driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--005']")
    user_birthdate_day.click()
    logger.info("Selected birthdate day")

@when('User enters subject as "{subject}"')
def step_enter_subject(context, subject):
    user_subject = context.driver.find_element(By.ID, "subjectsInput")
    user_subject.send_keys(subject)
    user_subject.click()
    user_subject.send_keys(Keys.ENTER)
    logger.info("Entered subject")

@when('User selects hobbies')
def step_select_hobbies(context):
    user_hobbies = context.driver.find_element(By.XPATH, "//div[@class='custom-control custom-checkbox custom-control-inline'][1]")
    user_hobbies.click()
    logger.info("Selected hobbies")

@when('User enters address as "{address}"')
def step_enter_address(context, address):
    user_address = context.driver.find_element(By.ID, "currentAddress")
    user_address.send_keys(address)
    user_address.send_keys(Keys.ENTER)
    logger.info("Entered address")

@then('Test is completed successfully')
def step_test_completed_successfully(context):
    logger.info("Test completed successfully")
    context.driver.close()
    context.driver.quit()
    logger.info("Closed browser")
