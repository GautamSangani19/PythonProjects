import allure
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument("--disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

#driver = context.driver.Chrome(options=options)
@allure.title("Test Login Functionality")
@allure.description("This test checks successful login with valid credentials.")
@given("the company is on the login page")
def perform_login(context):
    #river.get("https://devrecruiter.foodismconnect.com/auth/login")
    context.driver.get("https://dev-polypackrecruiter.foodismconnect.com/")
    sleep(2)
    mobile_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@formcontrolname='mobileNumber']"))
    )
    #mobile_input.send_keys("8000505310")
    #mobile_input.send_keys("8320373338")
    #mobile_input.send_keys("8155868675")
    mobile_input.send_keys("9909274230")

    sleep(2)

    login_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "login-btn"))
    )
    login_button.click()
    sleep(2)

    # Wait for OTP input field to appear and interact
    otp_input = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@autocomplete='one-time-code']"))
    )
    sleep(2)
    otp_input.send_keys("000000")  # Replace with your actual OTP if known or mock value
    sleep(2)

@when("the company enters a valid 10-digit mobile number")
def step_impl(context):
    pass

@when("the company clicks on the Send OTP button")
def step_impl(context):
    pass

@then("a 6-digit OTP should be sent to the registered mobile number")
def step_impl(context):
    sleep(2)
    pass

@when("the company enters the correct OTP within 30 seconds")
def step_impl(context):
    pass

@when("the company clicks on the Verify OTP button")
def step_impl(context):
    pass

@then("the company should be redirected to the Add Profile Details screen")
def step_impl(context):
    sleep(5)
    pass

# @when("the OTP is not received within 30 seconds")
# def step_impl(context):
#     pass
#
# @when("the company clicks on the 'Resend OTP' button")
# def step_impl(context):
#     pass
#
# @then("a new OTP should be sent to the registered mobile number")
# def step_impl(context):
#     pass
#
# @when("the company enters an incorrect OTP")
# def step_impl(context):
#     pass
#
# @then("an error message 'Invalid OTP. Please try again.' should be displayed")
# def step_impl(context):
#     pass
#
# @when("the company selects the 'Continue with Google' option")
# def step_impl(context):
#     pass
#
# @when("the company completes Google authentication successfully")
# def step_impl(context):
#     pass
#
# @then("the company should be prompted to enter a mobile number")
# def step_impl(context):
#     pass
