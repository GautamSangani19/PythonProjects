from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from time import sleep
from features.login_utils import perform_login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from selenium.webdriver import Keys, ActionChains

image_path = r"C:\Users\admin\Downloads\test.jpg"


@given("the company is logged in and on the menu for like a job")
def step_impl(context):
    perform_login(context.driver)
    sleep(5)

@when("the company is logged in and on the menu for like a job")
def step_impl(context):
    # Wait until the "Add Machinery" button is clickable
    add_machinery_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='tab' and .//span[text()='Machinery']]"))
    )
    # Click the button
    add_machinery_button.click()
    sleep(3)

@then("the company is liked a job using the like icon")
def step_impl(context):
    Like_buttom = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//mat-icon[normalize-space(text())='thumb_up_off_alt']"))
    )
    # Click the button
    Like_buttom.click()
    sleep(3)

@then("the company is click on the add comment icon")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    comment_icon = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//mat-icon[normalize-space(text())='comment']")
    ))
    # Click the comment icon
    comment_icon.click()
    # Clear existing content
    sleep(3)

@then("the company add the text")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    textarea = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//textarea[@formcontrolname='text']")
    ))

    # Add new text with motion (simulating typing with delays)
    text_to_type = "This is a test description written via Selenium."
    for char in text_to_type:
        textarea.send_keys(char)
        time.sleep(0.1)  # Delay between each character to simulate typing
    sleep(3)

@then("click on post comment button")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    post_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.//span[contains(text(),'Post Comment')]]")
    ))
    post_button.click()
    sleep(5)
