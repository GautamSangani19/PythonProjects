from behave import given, when, then
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.login_utils import perform_login


# Initialize WebDriver and handle context

@given("the company is logged into the platform for test")
def step_impl(context):
    perform_login(context)
    sleep(5)

@when("the company clicks on the Logout button")
def step_impl(context):
    # Add logic to click the logout button here
    pass

@then("the company should be logged out of the platform")
def step_impl(context):

    wait = WebDriverWait(context.driver, 10)
    menu_button1 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//mat-icon[normalize-space()='keyboard_arrow_down']")
    ))
    # Click the button
    menu_button1.click()
    sleep(3)

    # Assuming driver and wait are already defined
    wait = WebDriverWait(context.driver, 10)
    logout_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[.//span[normalize-space(text())='Logout']]"
    )))
    logout_button.click()
    sleep(3)

    # Assuming driver and wait are already defined
    yes_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[.//p[normalize-space(text())='Yes']]"
    )))
    yes_button.click()
    sleep(3)

@then("the login screen should be displayed")
def step_impl(context):
    # Add logic to verify the login screen is displayed after logout
    pass


