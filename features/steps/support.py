import os

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


# Windows-style image path (escaped)
image_path = r"C:\Users\admin\Downloads\test.jpg"

@given("the company is logged in and on the settings page for support")
def step_impl(context):
    perform_login(context.driver)
    sleep(3)

@when("the company is logged in and on the settings page for support")
def step_impl(context):
    # Wait until the "Edit Profile" button is visible and clickable
    wait = WebDriverWait(context.driver, 10)
    menu_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//mat-icon[normalize-space()='keyboard_arrow_down']")
    ))
    # Click the button
    menu_button.click()
    sleep(3)

    # Wait until the 'Support' menu item is clickable
    wait = WebDriverWait(context.driver, 10)
    support_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@role='menuitem']//span[text()='Support']")
    ))

    # Click the 'Support' button
    support_button.click()
    sleep(3)

@then("the company add subject for support form")
def step_impl(context):
    # Wait until the Subject input is visible
    wait = WebDriverWait(context.driver, 10)
    subject_input = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Subject']")
    ))

    # Enter a subject into the input field
    subject_input.send_keys("Test automation subject")
    sleep(3)

@then("the company add the description for the support form")
def step_impl(context):
    # Wait for the Description field to be visible
    wait = WebDriverWait(context.driver, 10)
    description_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@formcontrolname='description']")
    ))
    description_input.send_keys("This is a test description for the support form.")

@then("the company add the image")
def step_impl(context):
    # Wait for camera icon to be clickable and click it
    wait = WebDriverWait(context.driver, 10)
    # camera_icon = wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//img[contains(@src, 'camera_support.png')]")
    # ))
    # camera_icon.click()
    # Locate the hidden file input element and upload the image
    file_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@type='file']")
    ))
    file_input.send_keys(image_path)
    sleep(3)

@then("submit the support form")
def step_impl(context):
    # Click the Submit button
    wait = WebDriverWait(context.driver, 10)
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.//span[text()='Submit']]")
    ))
    submit_button.click()

