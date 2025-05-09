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


@given("the company is logged in and on the homepage for search")
def step_impl(context):
    perform_login(context.driver)
    sleep(5)

@when("the company clicks on the search bar")
def step_impl(context):
    pass

@when("the company leaves the input empty and triggers the search")
def step_impl(context):
    pass
    # Wait for the input field to become visible
    # search_input = WebDriverWait(context.driver, 10).until(
    #     EC.visibility_of_element_located((By.XPATH, "//input[@type='text' or contains(@class, 'search')]"))
    # )
    # # Enter your search text
    # search_input.send_keys("Leave Request")
    # sleep(5)

@then("the platform should prompt to enter a valid search term")
def step_impl(context):
    # Assert error or validation message is displayed
    pass

@when("the company starts typing a search term")
def step_impl(context):
    # Enter partial text to trigger autocomplete
    pass

@then("relevant autocomplete suggestions should appear")
def step_impl(context):
    # Assert autocomplete suggestion box is visible with entries
    pass

@when("the company enters a search term in the search bar")
def step_impl(context):
    # Input a valid search term
    pass

@when("the company clicks on the Clear icon")
def step_impl(context):
    # Click the 'X' icon to clear search
    pass

@then("the search bar should be cleared")
def step_impl(context):
    # 1. Click the search icon
    search_icon = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'search')]"))
    )
    search_icon.click()
    sleep(2)

    # 2. Locate the search input field
    search_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='search']"))
    )

    # 3. Enter search text (e.g., "Leave Request")
    search_input.send_keys("Aatman")

    # 4. Optional: Press Enter to trigger search
    search_input.send_keys(Keys.ENTER)
    sleep(2)
    search_input.clear()
