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

@given("the company is logged in and on the menu for refer and earn")
def step_impl(context):
    perform_login(context)
    sleep(5)

@when("the company is logged in and on the menu for refer and earn")
def step_impl(context):
    # Wait until the "Edit Profile" button is visible and clickable
    wait = WebDriverWait(context.driver, 10)
    menu_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//mat-icon[normalize-space()='keyboard_arrow_down']")
    ))
    # Click the button
    menu_button.click()
    sleep(3)

@then("the company is logged in and select the refer and earn option")
def step_impl(context):
    # Assuming driver and wait are already defined
    wait = WebDriverWait(context.driver, 10)
    refer_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[.//span[normalize-space(text())='Refer & Earn']]"
    )))
    refer_button.click()
    sleep(3)

@then("Click on the copy icon for copied the refer and earn code")
def step_impl(context):
    # Assuming driver and wait are already defined
    wait = WebDriverWait(context.driver, 10)
    copy_icon = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//img[contains(@src, 'copy.png')]"
    )))
    copy_icon.click()
    sleep(3)

# @then("Click on the share icon for copied the refer and earn code")
# def step_impl(context):
#     # Assuming driver and wait are already defined
#     wait = WebDriverWait(context.driver, 10)
#     share_icon = wait.until(EC.element_to_be_clickable((
#         By.XPATH, "//mat-icon[normalize-space(text())='share']"
#     )))
#     share_icon.click()
#     sleep(3)

@then("Close the current section")
def step_impl(context):
    # Assuming driver and wait are already defined
    wait = WebDriverWait(context.driver, 10)
    close_icon = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//mat-icon[@mat-dialog-close and normalize-space(text())='close']"
    )))
    close_icon.click()

@then("Logout from the app")
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
    context.driver.save_screenshot("refer_error_screenshot.png")  # Save the screenshot in the project root
