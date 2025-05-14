from time import sleep
import time
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from features.login_utils import perform_login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from selenium.webdriver import Keys, ActionChains

@given("the company is logged in for edit job detail")
def step_impl(context):
    perform_login(context)
    sleep(3)

@when("click on the more details button")
def step_impl(context):
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//p[@class='font-weight-600 font-size-14 color-font-third cursor'][normalize-space()='More Details'])[1]"))
    )
    element.click()
    sleep(3)

@then("click on edit icon")
def step_impl(context):
    edit_icon = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'carbon_edit-white.png')]"))
    )
    edit_icon.click()
    sleep(3)

@then("the company edit the Job Description")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    editor_div = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR,
        "div.ck-editor__editable[contenteditable='true']"
    )))
    # Clear existing content
    editor_div.click()
    editor_div.send_keys(Keys.CONTROL + "a")  # Select all text
    editor_div.send_keys(Keys.DELETE)  # Delete the selected text
    sleep(3)

    # Add new text with motion (simulating typing with delays)
    text_to_type = "This is a test description written via Selenium."
    for char in text_to_type:
        editor_div.send_keys(char)
        time.sleep(0.1)  # Delay between each character to simulate typing
    sleep(3)

@then("the company edit the Job Availability Duration")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Step 2: Click on the mat-select to open dropdown
    timeline_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='timeline']")))
    timeline_dropdown.click()

    # Step 3: Wait and select the option (e.g. "1 to 3 Days")
    option = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[2]")))
    option.click()
    sleep(2)

@then("the company edit the details successfully")
def step_impl(context):
    pass

@then("the Job successfully edited")
def step_impl(context):
    save_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='Save']]"))
    )
    save_button.click()
    sleep(2)
    continue_button = context.driver.find_element(By.XPATH, "//button[span//p[text()='Continue']]")
    continue_button.click()
    sleep(5)

