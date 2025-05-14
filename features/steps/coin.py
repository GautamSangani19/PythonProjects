from time import sleep
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from features.login_utils import perform_login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from selenium.webdriver import Keys, ActionChains


@given("the company is on the Home page")
def step_impl(context):
    perform_login(context)
    sleep(5)


@when("the company is on the Homepage for coin history")
def step_impl(context):
# Wait until the "Edit Profile" button is visible and clickable
    wait = WebDriverWait(context.driver, 10)
    edit_profile_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//mat-icon[normalize-space()='keyboard_arrow_down']")
    ))
# Click the button
    edit_profile_button.click()

@then("Click on Coin history button")
def step_impl(context):
    # Wait for and click the "Buy Coins" button
    wait = WebDriverWait(context.driver, 10)
    Coin_history_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@role='menuitem']//span[normalize-space()='Coin History']")))

    Coin_history_button.click()
    sleep(3)

@then("download history")
def step_impl(context):
    # Wait until the image is present and clickable
    wait = WebDriverWait(context.driver, 20)
    download_icon = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//img[contains(@src, 'material-symbols_download.png')]")
    ))

    # Click the download icon
    download_icon.click()
    sleep(3)

@then("Select the calendar")
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

@then("click on save button on calendar")
def step_impl(context):
    # Wait until the image is present and clickable
    wait = WebDriverWait(context.driver, 20)
    # Wait until the button is clickable and click it
    download_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.//p[normalize-space()='Download']]")
    ))
    download_button.click()
    sleep(3)

@then("click on filter icon")
def step_impl(context):
    # Wait for the filter icon to be visible and clickable
    filter_icon = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//img[contains(@src, 'mdi_filter-outline.png')]")
    ))

    filter_icon.click()
    sleep(3)

@then("select the start date")
def step_impl(context):
    # Click the calendar icon to open datepicker
    calendar_icon = context.driver.find_element(By.XPATH, "//button[@aria-label='Open calendar']")
    calendar_icon.click()

    # Wait and select the start date
    start_date = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//td[normalize-space()='7']")  # Adjust based on calendar structure
    ))
    start_date.click()
    sleep(4)
    start_date.click()


@then("select the end date")
def step_impl(context):
    # Click the calendar icon to open datepicker
    # calendar_icon1 = context.driver.find_element(By.CLASS_NAME, "mat-mdc-button-touch-target")
    # calendar_icon1.click()
    # # Select the end date
    # end_date1 = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
    #     (By.XPATH, "//td[normalize-space()='8']")  # Adjust as needed
    # ))
    # end_date1.click()
    # sleep(3)

    # Locate the input field using its ID or other attribute
    # date_input = context.driver.find_element(By.ID, "mat-input-19")
    #
    # # Clear any existing text and enter the desired date (format must match the app's expected format)
    # date_input.clear()
    # date_input.send_keys("15/07/2025")  # Or "2025-07-15" depending on expected format
    #
    # # Optionally, trigger blur or tab away if necessary
    # date_input.send_keys("\t")  # Tab to trigger change events if needed
    # sleep(2)

    # # Click on the calendar icon (toggle)
    # calendar_icon = WebDriverWait(context.driver, 10).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, "mat-datepicker-toggle-default-icon"))
    # )
    # calendar_icon.click()
    #
    # # Wait for calendar to appear and click a date (change aria-label as needed)
    # target_date = WebDriverWait(context.driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='15 July 2025']"))
    # )
    # target_date.click()

    # Step 1: Click on the calendar toggle (SVG icon)
    # Select the end date
    # end_date = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(
    #     (By.XPATH, "//td[normalize-space()='8']")  # Adjust as needed
    # ))
    # end_date.click()
    # sleep(3)

    # Open End Date calendar (second button)
    end_calendar_icon = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Open calendar'])[2]"))
    )
    end_calendar_icon.click()

    # Wait and click date (e.g., "15")
    end_date = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[normalize-space()='14']"))
    )
    end_date.click()
    sleep(2)
    end_date.click()



@then("click on type selection")
def step_impl(context):
    # Wait for the checkbox to be present
    checkbox_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".mdc-checkbox"))
    )
    checkbox_input.click()

    # Check if it's selected
    if checkbox_input.is_selected():
        print("Checkbox is selected.")
    else:
        print("Checkbox is not selected.")

    sleep(3)

@then("select the amount")
def step_impl(context):
    # Locate the slider handle element
    slider_handle = context.driver.find_element(By.CSS_SELECTOR, 'span.ngx-slider-pointer')

    # Get the current position of the slider handle (aria-valuenow)
    current_value = int(slider_handle.get_attribute("aria-valuenow"))

    # Define the desired value to set the slider to
    desired_value = 500  # For example, move the slider to value 500

    # Get the slider's min and max values from the element attributes
    min_value = int(slider_handle.get_attribute("aria-valuemin"))
    max_value = int(slider_handle.get_attribute("aria-valuemax"))

    # Calculate the desired position on the slider based on the ratio between current, min, and max
    slider_length = slider_handle.size['width']  # Width of the slider handle
    desired_position = ((desired_value - min_value) / (max_value - min_value)) * slider_length

    # Create an ActionChains object to perform the drag action
    action = ActionChains(context.driver)

    # Perform the drag action: drag the slider handle to the calculated position
    action.click_and_hold(slider_handle).move_by_offset(desired_position - current_value, 0).release().perform()

    # Optional: Verify the new value after dragging
    new_value = int(slider_handle.get_attribute("aria-valuenow"))
    print(f"Slider moved to value: {new_value}")

    sleep(3)

@then("click on apply button")
def step_impl(context):
    # Wait until the "Apply" button is clickable and then click it
    apply_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Apply')]"))
    )
    apply_button.click()
    sleep(3)

    # Close the WebDriver
    context.driver.quit()