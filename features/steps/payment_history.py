from time import sleep
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from features.login_utils import perform_login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from selenium.webdriver import Keys, ActionChains


@given("the company is on the Home page for Payment History")
def step_impl(context):
    context.driver = webdriver.Chrome()
    perform_login(context.driver)
    sleep(5)


@when("the company is on the Homepage for Payment history")
def step_impl(context):
# Wait until the "Edit Profile" button is visible and clickable
    wait = WebDriverWait(context.driver, 10)
    menu_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//mat-icon[normalize-space()='keyboard_arrow_down']")
    ))
# Click the button
    menu_button.click()


@then("Click on Payment history button")
def step_impl(context):
    # Wait for the "Payment History" menu item to be clickable and click it
    payment_history_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@role='menuitem']//span[text()='Payment History']"))
    )
    payment_history_button.click()
    sleep(3)

@then("Download the payment history")
def step_impl(context):
    # Wait for the image to be clickable using the class
    download_icon = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//img[contains(@src, 'material-symbols_download.png') and contains(@class, 'cursor')]"))
    )
    download_icon.click()

@then("Select the calendar for the payment history")
def step_impl(context):
    # Click the calendar icon to open datepicker
    calendar_icon = context.driver.find_element(By.XPATH, "//button[@aria-label='Open calendar']")
    calendar_icon.click()

    # Wait and select the start date
    start_date = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//td[normalize-space()='1']")  # Adjust based on calendar structure
    ))
    start_date.click()

    # Select the end date
    end_date = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//td[normalize-space()='8']")  # Adjust as needed
    ))
    end_date.click()
    sleep(3)

@then("click on save button on calendar for the payment history")
def step_impl(context):
    # Wait until the image is present and clickable
    wait = WebDriverWait(context.driver, 20)
    # Wait until the button is clickable and click it
    download_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.//p[normalize-space()='Download']]")
    ))
    download_button.click()
    sleep(3)

