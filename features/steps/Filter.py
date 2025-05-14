import pyautogui
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from time import sleep
from features.login_utils import perform_login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from selenium.webdriver import Keys, ActionChains
from PIL import Image


image_path = r"C:\Users\admin\Downloads\test.jpg"


@given("the company is logged in for filter option")
def step_impl(context):
    perform_login(context)
    sleep(5)

@when("click on machine tab list")
def step_impl(context):
    # Wait until the Machinery tab is clickable and click it
    machinery_tab = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='tab' and .//span[text()='Machinery']]"))
    )
    machinery_tab.click()
    sleep(3)

# @then("Machine details screen for filter")
# def step_impl(context):
#     more_details = WebDriverWait(context.driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//p[text()=' More Details ']"))
#     )
#     more_details.click()
#     sleep(3)

@then("CLick on filter icon for machinery filter")
def step_impl(context):
    filter_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[span[contains(text(), 'Filter')]]"))
    )
    filter_button.click()
    sleep(3)

@then("Add the brand name for filter option")
def step_impl(context):
    brand_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='brand']"))
    )
    brand_input.clear()
    brand_input.send_keys("Bosch")
    sleep(3)

@then("select type for filter option")
def step_impl(context):
    # 1. Click the mat-select to open the dropdown
    type_dropdown = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='type']"))
    )
    type_dropdown.click()

    # 2. Wait and click the desired option (replace 'CNC' with your option)
    desired_option = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//mat-option//span[contains(text(), 'CNC')]"))
    )
    desired_option.click()
    sleep(3)

@then("select condition for filter option")
def step_impl(context):
    # STEP 1: Click the dropdown to open the options
    condition_dropdown = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='condition']"))
    )
    condition_dropdown.click()

    # STEP 2: Wait for and click on the desired option (replace 'New' with your target value)
    desired_option = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//mat-option//span[text()='New']"))
    )
    desired_option.click()
    sleep(3)

@then("select model for filter option")
def step_impl(context):
    # STEP: Wait for the model input field to be visible and enter text
    model_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='model']"))
    )
    model_input.clear()
    model_input.send_keys("AX-500")  # Replace with your desired model name
    sleep(3)

@then("Add the location for filter option")
def step_impl(context):
    # STEP: Wait for the Location input field and enter a location
    location_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='location']"))
    )
    location_input.clear()
    location_input.send_keys("Mumbai")  # Replace with your desired location
    sleep(3)

@then("click on apply filter button")
def step_impl(context):
    # Locate the button by the label text "Apply Filters"
    button = context.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Apply Filters')]]")
    # Click the button
    button.click()
    sleep(3)



@then("Filter applied successfully")
def step_impl(context):

    # Set the window size to capture full page
    context.driver.set_window_size(1920, 1080)  # Example for full-screen on many monitors

    context.driver.save_screenshot("Filter_error_screenshot.png")  # Save the screenshot in the project root

    # Scroll down the page to make sure the full page is loaded
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Take a full-page screenshot
    context.driver.get_screenshot_as_file("full_screenshot.png")
    sleep(3)


@then("Reset filter")
def step_impl(context):
    filter_button1 = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[span[contains(text(), 'Filter')]]"))
    )
    filter_button1.click()
    sleep(3)

    reset_button = (context.driver.find_element(By.XPATH, "//span[text()='Reset']/ancestor::button"))
    reset_button.click()
    sleep(3)

    button1 = context.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Apply Filters')]]")
    # Click the button
    button1.click()
    sleep(3)


@then("Reset filter successfully")
def step_impl(context):
    context.driver.quit()
    pass