from behave import given, when, then
from time import sleep
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from features.login_utils import perform_login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from selenium.webdriver import Keys, ActionChains

@given("the company is logged in and on the settings page for change mobile number")
def step_impl(context):
    perform_login(context.driver)
    sleep(5)

@when("the company is logged in and on the settings page for change mobile number")
def step_impl(context):
    # Wait until the "Edit Profile" button is visible and clickable
    wait = WebDriverWait(context.driver, 10)
    menu_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//mat-icon[normalize-space()='keyboard_arrow_down']")
    ))
    # Click the button
    menu_button.click()
    sleep(3)

    # Wait for the "Settings" menu item and click it
    settings_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@role='menuitem']//span[text()='Settings']"))
    )
    settings_button.click()
    sleep(3)

@then("Click on change details button")
def step_impl(context):
    change_details = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//img[contains(@src, 'edit-file.png')]/following-sibling::p[text()='Change Details']/ancestor::div[contains(@class, 'cursor')]"))
    )
    change_details.click()
    sleep(3)

@then("Click on send OTP button")
def step_impl(context):
    # Click a button that has the text "Submit"
    submit_button = context.driver.find_element(By.XPATH, "(//p[normalize-space()='Send OTP'])[1]")
    submit_button.click()

    sleep(3)

@then("add otp")
def step_impl(context):
    # Wait for the OTP input field to appear
    otp_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@autocomplete='one-time-code']"))
    )

    # Send OTP value
    otp_input.send_keys("000000")
    sleep(3)


@then("click on the next button")
def step_impl(context):
    next_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//p[normalize-space()='Next'])[1]"))
    )
    next_button.click()
    sleep(3)

@then("Enter Your New Mobile Number")
def step_impl(context):
    # Locate the input field by ID and enter mobile number
    # Wait for the input field and enter mobile number
    mobile_input = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='mobileNumber']"))
    )
    # Scroll into view (optional but useful for stability)
    context.driver.execute_script("arguments[0].scrollIntoView(true);", mobile_input)

    # Use ActionChains to click and type
    actions = ActionChains(context.driver)
    actions.move_to_element(mobile_input).click().send_keys("9909274231").perform()
    sleep(3)

@then("Click on submit button")
def step_impl(context):
    # Locate the parent clickable element via the <p> text
    send_otp_element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Send OTP']"))
    )
    # Scroll to it (optional)
    context.driver.execute_script("arguments[0].scrollIntoView(true);", send_otp_element)
    # Click using ActionChains
    ActionChains(context.driver).move_to_element(send_otp_element).click().perform()
    sleep(3)

    context.driver.save_screenshot("error_screenshot.png")  # Save the screenshot in the project root
