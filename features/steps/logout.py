from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver and handle context

@given("the company is logged into the platform for test")
def step_impl(context):
    # Add login implementation here to ensure the company is logged in
    # e.g., navigate to login page, enter credentials, and click login
    pass

@when("the company clicks on the Logout button")
def step_impl(context):
    # Add logic to click the logout button here
    pass

@then("the company should be logged out of the platform")
def step_impl(context):
    # Add logic to check if the company is logged out
    pass

@then("the login screen should be displayed")
def step_impl(context):
    # Add logic to verify the login screen is displayed after logout
    pass


