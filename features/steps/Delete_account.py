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

@given("the company is logged in and on the settings page for delete account")
def step_impl(context):
    perform_login(context)
    sleep(5)

@when("the company is logged in and on the settings page for delete account")
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

@then("the company clicks on Delete Account")
def step_impl(context):
    # Locate the "Delete Account" button by the text in <p> tag
    delete_account_button = context.driver.find_element(By.XPATH, "//p[text()='Delete Account']")

    # Optionally, if you want to click the entire container, you can locate the div element containing the text:
    # delete_account_button = driver.find_element(By.XPATH, "//div[.//p[text()='Delete Account']]")

    # Hover over the "Delete Account" text (if needed)
    actions = ActionChains(context.driver)
    actions.move_to_element(delete_account_button).perform()

    # Click the "Delete Account" button
    delete_account_button.click()
    sleep(3)

@then("the company clicks on Send OTP")
def step_impl(context):
    # Wait for the button to be clickable
    wait = WebDriverWait(context.driver, 10)
    send_otp_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='Send OTP']]")))

    # Click the button
    send_otp_button.click()
    sleep(10)

@then("Enter your verification code")
def step_impl(context):
    # Wait until the OTP input is visible and interactable
    otp_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.otp-input"))
    )

    # Send OTP digits (replace '123456' with actual OTP value)
    otp_input.send_keys("000000")
    sleep(5)

# @when("the company selects their own number")
# def step_impl(context):
#     # Choose the registered number from the list
#     pass
#
# @when("clicks on Send OTP")
# def step_impl(context):
#     # Send OTP for deletion confirmation
#     pass
#
# @then("OTP should be sent to the selected number")
# def step_impl(context):
#     # Verify the OTP delivery
#     pass
#
# @when("the company clicks on Change Mobile Number")
# def step_impl(context):
#     # Navigate to the change number page/section
#     pass
#
# @then("the company should receive an OTP for number change")
# def step_impl(context):
#     # Confirm OTP is sent for number change
#     pass
#
# @when("the company enters a new mobile number")
# def step_impl(context):
#     # Input another mobile number
#     pass
#
@then("Delete account successfully")
def step_impl(context):
    # Wait for the button to be clickable
    wait = WebDriverWait(context.driver, 10)
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(// p[normalize-space() = 'Submit'])[1]")))

    # Click the button
    submit_button.click()
    sleep(5)
