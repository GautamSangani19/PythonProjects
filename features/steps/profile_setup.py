from time import sleep
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from features.login_utils import perform_login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from selenium.webdriver import Keys


@given("the company is on the profile setup page")
@allure.step("the company is on the profile setup page")
def step_impl(context):
    perform_login(context.driver)
    sleep(10)

@when("the company fills in all mandatory fields")
@allure.step("the company fills in all mandatory fields")
def step_impl(context):
    name = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "mat-input-1"))
    )
    name.send_keys("GenAI Novuscode")
    sleep(3)

@then("the company fills the username")
@allure.step("the company fills the username")
def step_impl(context):
    user_name = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@formcontrolname="name"]'))
    )
    user_name.send_keys("Gautam")
    sleep(3)

@then("the company add the establishedSince")
@allure.step("the company add the establishedSince")
def step_impl(context):
# Wait for the input field to be visible and interactable
    established_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='establishedSince']"))
    )
    established_input.send_keys("2010")
    sleep(3)

@then("the company add the address")
def step_impl(context):
    # Wait for the address input field to be visible and interactable
    address_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='address']"))
    )
    # Clear and enter address text
    address_input.clear()
    address_input.send_keys("A-407 Safal pegasus, Anand nagar road, Ahmedabed")
    sleep(3)

@then("the company adds the city")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    # Step 1: Type partial text in the location input field
    location_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//input[@formcontrolname="city"]')))
    location_input.clear()
    location_input.send_keys("mum")

    # Step 2: Wait for suggestions to appear
    suggestion_xpath = "//mat-option//span[contains(text(), 'Mumbai, Maharashtra')]"
    suggestion = wait.until(EC.element_to_be_clickable((By.XPATH, suggestion_xpath)))
    suggestion.click()

@then("the company add the email address")
def step_impl(context):
# Wait for the email input field to be visible
    email_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='email']"))
    )
    # Clear and enter email
    email_input.clear()
    email_input.send_keys("Gautam@yopmail.com")
    sleep(3)

@then("the company add the Type of Establishment")
def step_impl(context):
# Wait until the chip is visible and click it
    wait = WebDriverWait(context.driver, 10)
    chip = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()=' Operating Industrial Machinery ']")))
    chip.click()

@then("the company add Size Of Your Establishment")
def step_impl(context):
# Wait and click on the chip button with label '1-5'
    chip_button = WebDriverWait(context.driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@role='option']//span[contains(text(), '1-5')]"))
    )
    chip_button.click()

    sleep(3)


@then ("the company select Currently Hiring For")
def step_impl(context):
# Wait for and click the chip button labeled "Full-Time"
    chip_full_time = WebDriverWait(context.driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@role='option']//span[contains(text(), 'Full-Time')]"))
    )
    chip_full_time.click()
    sleep(3)


@then("the company add the description")
def step_impl(context):
# Wait for the CKEditor div to be visible
    ckeditor_div = WebDriverWait(context.driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@role='textbox' and @contenteditable='true']"))
    )

# Click to focus (optional but helps)
    ckeditor_div.click()
    ckeditor_div.send_keys("Novuscode is an agency to provide generative AI solutions, LLM, mobile & web Apps, websites with quality services and develop long-term connections.")
    ckeditor_div.send_keys(Keys.ENTER)


# Use JavaScript to set content in CKEditor
#     context.driver.execute_script("""
#         arguments[0].innerHTML = '<p>This is an automated test input.</p>';
#         arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
#     """, ckeditor_div)

@then ("click on save button")
def step_impl(context):
    # Click the Save button
    save_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='Save']]"))
    )
    save_button.click()
    sleep(3)


@given("the company has filled in all required fields")
def step_impl(context):
    # Assume mandatory fields are already filled
    pass

@when("the company submits the profile")
def step_impl(context):
    # Submit the profile form
    pass

@then("the company's account should be marked as successfully created")
def step_impl(context):
    # Verify account creation success
    pass
