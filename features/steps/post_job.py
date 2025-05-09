import allure
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from features.login_utils import perform_login
from time import sleep

@given("the company is on the login page for add job")
@allure.step("the company is on the login page for add job")
def step_impl(context):
    perform_login(context.driver)
    sleep(2)

@when("the user is on the Post a Job page")
@allure.step("the user is on the Post a Job page")
def step_impl(context):
    # Wait for the button and click it
    post_job_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Post a Job')]"))
    )
    post_job_button.click()

@then("the user fills out the job form with valid data")
@allure.step("the user fills out the job form with valid data")
def step_impl(context):
    # Wait until the job title input field is visible
    job_title_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='jobTitle']"))
    )
    # Send value to the field
    job_title_input.send_keys("Senior QA Engineer")

@then("the company selects the Looking For option")
@allure.step("the company selects the Looking For option")
def step_impl(context):

    wait = WebDriverWait(context.driver, 20)

    # Debug screenshot
    # context.driver.save_screenshot("before_select_click.png")
    #
    # try:
    #     # Use broader selector first
    #     #dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='mat-mdc-select-placeholder mat-mdc-select-min-line ng-tns-c1771602899-8 ng-star-inserted'])[1]")))
    #     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='mat-select-value-19'])[1]")))
    #     dropdown.click()
    #
    #     # Then select option
    #     option = wait.until(
    #         EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[2]"))
    #     )
    #     option.click()
    # except Exception as e:
    #     print("Dropdown interaction failed:", str(e))
    #     context.driver.save_screenshot("dropdown_error.png")
    #     raise

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


@then("the company selects the job duration option")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Step 1: Open the dropdown (Assuming you're clicking a select to open this panel)
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='hiring']")))
    dropdown.click()

    # Step 2: Select the desired option - "1-4 years"
    option = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[3]")))
    option.click()

    sleep(2)

@then("the company adds the minimum salary")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    try:
        # Locate the input field by its ID (this ID should match the input element)
        input_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//input[@id='mat-input-2'])[1]")  # This matches the ID referenced in the label
        ))

        # Clear any existing value and enter a new salary
        input_field.send_keys("10000")  # Example salary

    except Exception as e:
        print(f"Error entering minimum salary: {e}")
        context.driver.save_screenshot("minimum_salary_input_error.png")
        raise
    sleep(2)

@then("the company adds the maximum salary")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    try:
        # Locate the input field by its ID (this ID should match the input element)
        input_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//input[@id='mat-input-3'])[1]")  # This matches the ID referenced in the label
        ))
        # Clear any existing value and enter a new salary
        input_field.send_keys("50000")  # Example salary

    except Exception as e:
        print(f"Error entering minimum salary: {e}")
        context.driver.save_screenshot("minimum_salary_input_error.png")
        raise
    sleep(2)

@then("the company selects the skills")
def step_impl(context):
    # Wait until the chip button is present
    wait = WebDriverWait(context.driver, 10)
    #chip_button = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'Tool Handling')])[1]")))
    #chip_button.click()
    # Click on the "Tool Handling" chip
    chip = context.driver.find_element(By.XPATH, "//mat-chip-option[.//span[contains(text(), 'Tool Handling')]]")
    chip.click()

@then("the company selects the experience")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Step 1: Open the dropdown (Assuming you're clicking a select to open this panel)
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH,"//mat-select[@formcontrolname='experience']")))
    dropdown.click()

    # Step 2: Select the desired option - "1-4 years"
    option = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[2]")))
    option.click()

    sleep(2)

@then("the company adds the location")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # location_input = wait.until(EC.presence_of_element_located((By.ID, "mat-input-10")))
    # location_input.send_keys("Mumbai")

    # wait = WebDriverWait(context.driver, 10)
    # # Step 1: Open the dropdown (Assuming you're clicking a select to open this panel)
    # input = wait.until(EC.element_to_be_clickable((By.ID,"mat-input-26")))
    # input.click()
    # input.send_keys("Mumbai")
    #
    # # Step 2: Select the desired option - "1-4 years"
    # option = wait.until(EC.element_to_be_clickable((By.XPATH, "(//mat-option[@id='mat-option-316'])[1]")))
    # option.click()
    #
    # sleep(2)

    # Step 1: Type partial text in the location input field
    location_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@formcontrolname='location']")))
    location_input.clear()
    location_input.send_keys("mum")
    sleep(2)
    # Step 2: Wait for suggestions to appear
    suggestion_xpath = "//mat-option//span[contains(text(), 'Mumbai, Maharashtra')]"
    suggestion = wait.until(EC.element_to_be_clickable((By.XPATH, suggestion_xpath)))
    suggestion.click()
    sleep(2)
@then("the company adds the Supplemental Pay")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    severance_chip = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.//span[text()[contains(., 'Severance Pay')]]]")))
    severance_chip.click()
    sleep(2)
@then("the company adds the Benefits")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    education_chip = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'Education and Self Growth Opportunities')]")
    ))
    education_chip.click()
    sleep(2)
@then("the company adds the Job Description")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    editor_div = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR,
        "div.ck-editor__editable[contenteditable='true']"
    )))
    editor_div.click()
    editor_div.send_keys("This is a test description written via Selenium.")
    editor_div.send_keys(Keys.ENTER)


    sleep(2)

@then("the company selects the Job Availability Duration")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Step 2: Click on the mat-select to open dropdown
    timeline_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='timeline']")))
    timeline_dropdown.click()

    # Step 3: Wait and select the option (e.g. "1 to 3 Days")
    option = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[1]")))
    option.click()
    sleep(2)

@then("the company selects the open position")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Step 1: Click the numberOfHires mat-select dropdown
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='numberOfHires']")))
    dropdown.click()

    option = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='radio'])[1]")))
    option.click()
    sleep(2)

# @then("the company adds the email")
# def step_impl(context):
#     email_input = context.driver.find_element(By.ID, "mat-input-11")
#     context.driver.execute_script("arguments[0].removeAttribute('readonly')", email_input)
#     email_address = "testuser@example.com"
#     context.driver.execute_script("arguments[0].value = arguments[1]", email_input, email_address)

@then("the company selects send an individual email when someone applies")
def step_impl(context):
    # Locate checkbox by ID / XPath / CSS Selector
    # checkbox = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @formcontrolname='yourControlName']")))
    # checkbox.click()

    # # Wait for and click the checkbox input by its ID
    # checkbox = context.wait.until(EC.element_to_be_clickable((By.ID, "sendEmailWhenApplied")))
    # checkbox.click()

    checkbox = context.driver.find_element(By.ID, "sendEmailWhenApplied")
    checkbox.click()
    # if checkbox.is_selected():
    #     print("Checkbox is selected ✅")
    # else:
    #     print("Checkbox is not selected ❌")

    sleep(5)


@then("select Send WhatsApp updates")
def step_impl(context):
    whatsapp_checkbox = context.driver.find_element(By.ID, "sendWhatsappUpdates")
    whatsapp_checkbox.click()

@then("clicks on Save")
def step_impl(context):
    save_button = context.driver.find_element(By.XPATH, "//button[span//p[text()='Save']]")
    save_button.click()
    sleep(5)

@then("the job preview screen should appear with all filled details")
def step_impl(context):
    pass
    sleep(5)

@then("the Job post successfully")
def step_impl(context):
    continue_button = context.driver.find_element(By.XPATH, "//button[span//p[text()='Continue']]")
    continue_button.click()
    sleep(5)


def after_step(context, step):
    if step.status == "failed":
        screenshot_path = f"screenshots/{step.name}.png"
        context.driver.save_screenshot(screenshot_path)