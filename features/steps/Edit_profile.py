from time import sleep
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from features.login_utils import perform_login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from selenium.webdriver import Keys

@given("the company is on the edit profile setup page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    perform_login(context.driver)
    sleep(5)


@when("the company is on the Homepage for edit profile setup")
def step_impl(context):
# Wait until the "Edit Profile" button is visible and clickable
    wait = WebDriverWait(context.driver, 10)
    edit_profile_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//mat-icon[normalize-space()='keyboard_arrow_down']")
    ))

# Click the button
    edit_profile_button.click()

@then("the company is on the edit profile section")
def step_impl(context):
    # Wait for the "Edit Profile" menu item to be visible and clickable
    wait = WebDriverWait(context.driver, 10)
    edit_profile_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@role='menuitem']//span[normalize-space()='Edit Profile']")
    ))
    # Click the button
    edit_profile_button.click()
    sleep(3)

@then("the company is on the edit profile icon")
def step_impl(context):
    # Wait for the image or parent div to be clickable and click it
    wait = WebDriverWait(context.driver, 10)
    edit_icon = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//img[contains(@src, 'carbon_edit.png')]")
    ))
    # Click the icon
    edit_icon.click()
    sleep(3)


@then("Add th website")
def step_impl(context):
# Wait for the input field to be visible
    wait = WebDriverWait(context.driver, 10)
    website_input = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@formcontrolname='website']")
    ))

# Clear any existing text and enter new value
    website_input.clear()
    website_input.send_keys("www.dev-polypackrecruiter.foodismconnect.com")
    sleep(3)


@then("Unselect the option in type of establishment")
def step_impl(context):
    # Wait for the chip button to be clickable by text
    wait = WebDriverWait(context.driver, 10)
    chip_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@role='option']//span[contains(text(), 'Operating Industrial Machinery')]")
    ))

    # Click the chip
    chip_button.click()
    sleep(3)

@then("select the another option in type of establishment")
def step_impl(context):
    # Wait and click the "Knowledge of Building Systems" chip
    wait = WebDriverWait(context.driver, 10)
    chip = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@role='option']//span[contains(text(), 'Knowledge of Building Systems')]")
    ))

    chip.click()
    sleep(3)

@then ("click on save button for edit profile")
def step_impl(context):
    # Click the Save button
    wait = WebDriverWait(context.driver, 10)
    save_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.//p[normalize-space()='Save']]")
    ))

    save_button.click()
    sleep(3)


