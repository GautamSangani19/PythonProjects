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


@given("the company is logged in and on the menu for add machinery")
def step_impl(context):
    perform_login(context.driver)
    sleep(5)

@when("the company is logged in and on the menu for add machinery")
def step_impl(context):
    # Wait until the "Add Machinery" button is clickable
    add_machinery_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[normalize-space(text())='Add Machinery']/ancestor::button"))
    )

    # Click the button
    add_machinery_button.click()
    sleep(3)

@then("Add the machine image")
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


@then("Add the machinery name")
def step_impl(context):
    # Wait until the label is visible
    label = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//mat-label[text()='Machinery Name']"))
    )

    # Locate the input following the label (adjust based on actual DOM structure)
    input_field = context.driver.find_element(By.XPATH, "//mat-label[text()='Machinery Name']/ancestor::mat-form-field//input")

    # Scroll into view and enter value
    actions = ActionChains(context.driver)
    actions.move_to_element(input_field).click().send_keys("Test Machinery").perform()
    sleep(3)

@then("Add the machinery type")
def step_impl(context):
    # Wait and click the chip button that contains "CNC"
    cnc_chip = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@role='option' and contains(., 'CNC')]"))
    )
    cnc_chip.click()
    sleep(3)


@then("Add the brand name")
def step_impl(context):
    # Wait for the input field to be visible and interactable
    brand_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='brand']"))
    )
    # Clear and enter text into the input
    brand_input.clear()
    brand_input.send_keys("Bosch")  # Replace with the desired brand name
    sleep(3)

@then("Add the model name")
def step_impl(context):
    # Wait until the model input field is visible and interactable
    model_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='model']"))
    )

    # Clear any pre-filled data and send the model name
    model_input.clear()
    model_input.send_keys("AX-500")  # Replace with your actual model
    sleep(3)

@then("Enter year of manufracture")
def step_impl(context):
    year_input = context.driver.find_element(By.XPATH, "//input[@formcontrolname='year_of_manufacture']")
    year_input.send_keys("2020")
    sleep(3)

@then("Select the condition")
def step_impl(context):
    # Wait for the chip with text 'New' and click it
    new_chip = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'New')]]"))
    )
    new_chip.click()
    sleep(3)

@then("Add the price")
def step_impl(context):
    # Wait for the input field to be visible
    price_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='price']"))
    )

    # Clear any existing value and send new price
    price_input.clear()
    price_input.send_keys("25000")  # Replace with your desired price
    sleep(3)


@then("Add the location")
def step_impl(context):
    # Wait until the location input is visible
    location_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='location']"))
    )

    # Clear and enter the desired location
    location_input.send_keys("Mumbai")  # Replace with your actual location
    sleep(3)

@then("Add the description")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    editor_div = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR,
        "div.ck-editor__editable[contenteditable='true']"
    )))
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


@then("Add the contact number")
def step_impl(context):
    # Wait for the contact input field to be visible
    contact_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='contact_details']"))
    )

    # Clear and input contact number
    contact_input.clear()
    contact_input.send_keys("9876543210")  # Replace with your actual number
    sleep(3)

@then("save the details")
def step_impl(context):
    # Wait for the "Save" button to be clickable
    save_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='Save']]"))
    )

    # Click the "Save" button
    save_button.click()
    sleep(3)

@then("Machine details added successfully")
def step_impl(context):
    pass
    sleep(3)

@then("All added machine list")
def step_impl(context):
    # Wait until the Machinery tab is clickable and click it
    machinery_tab = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='tab' and .//span[text()='Machinery']]"))
    )
    machinery_tab.click()
    sleep(3)

@then("Machine details screen")
def step_impl(context):
    more_details = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()=' More Details ']"))
    )
    more_details.click()
    sleep(3)
    context.driver.save_screenshot("Machine_error_screenshot.png")  # Save the screenshot in the project root


