from time import sleep
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from features.login_utils import perform_login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from selenium.webdriver import Keys

@given("the company is on the draft page")
def step_impl(context):
    perform_login(context.driver)
    sleep(5)

@when("the user is in the home screen for draft a job")
def step_impl(context):
    pass

@then("the user is on the Post a Job page for draft")
def step_impl(context):
    # Wait for the button and click it
    post_job_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Post a Job')]"))
    )
    post_job_button.click()

@then("the user add the job title")
def step_impl(context):
    # Wait until the job title input field is visible
    job_title_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='jobTitle']"))
    )
    # Send value to the field
    job_title_input.send_keys("Senior QA Engineer")

@then("the company selects the type of job")
def step_impl(context):

    wait = WebDriverWait(context.driver, 20)
    # 1. Click on the mat-select dropdown by stable attribute
    dropdown = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//mat-select[@formcontrolname='type']"))
    )
    dropdown.click()

    # 2. Select the desired option from the dropdown
    # Replace 'Full-Time' with the actual visible text you want to select
    option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//input[@type='radio'])[2]"))
    )
    option.click()
    sleep(2)

@then("click on back button")
def step_impl(context):
# Go back to the previous page in browser history
    context.driver.back()
    sleep(2)

@then("click on save as draft button")
def step_impl(context):
    # Wait for and click the "Save as draft" button
    wait = WebDriverWait(context.driver, 10)
    save_draft_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.//p[normalize-space()='Save as draft']]")
    ))

    save_draft_button.click()
    sleep(2)

@then("the company is on the Homepage for draft job")
def step_impl(context):
# Wait until the "Edit Profile" button is visible and clickable
    wait = WebDriverWait(context.driver, 10)
    edit_profile_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//mat-icon[normalize-space()='keyboard_arrow_down']")
    ))

# Click the button
    edit_profile_button.click()
    sleep(2)

@then("the company is on the draft job section")
def step_impl(context):
    # Wait for and click the "My Drafts" menu item
    wait = WebDriverWait(context.driver, 10)
    my_drafts = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@role='menuitem']//span[normalize-space()='My Drafts']")
    ))
    my_drafts.click()
    sleep(3)

@then("the company clicks on the edit draft job")
def step_impl(context):
    # Wait for and click the edit icon image
    wait = WebDriverWait(context.driver, 10)
    edit_icon = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//img[contains(@src, 'carbon_edit.png')]")
    ))
    edit_icon.click()
    sleep(3)