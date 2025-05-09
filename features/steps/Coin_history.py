from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from features.login_utils import perform_login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from selenium.webdriver import Keys

@given("the company is on the coin history page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    perform_login(context.driver)
    sleep(5)

@when("Click on Buy coins button")
def step_impl(context):
    # Wait for and click the "Buy Coins" button
    wait = WebDriverWait(context.driver, 10)
    buy_coins_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@routerlink='/coins/buy-coins' and .//p[normalize-space()='Buy Coins']]")
    ))

    buy_coins_btn.click()
    sleep(3)

@then("select the coin amount")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    # Wait for the radio input element to be present
    radio_input = wait.until(EC.presence_of_element_located((By.ID, "mat-radio-2-input")))

    # Use JavaScript to click if standard click fails due to hidden layers or overlays
    context.driver.execute_script("arguments[0].click();", radio_input)

    sleep(2)

@then("click on add coin button")
def step_impl(context):
    # Wait for and click the "Buy Coins" button
    wait = WebDriverWait(context.driver, 10)
    buy_coins_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class, 'button-continue')]//p[normalize-space()='Buy Coins']")
    ))
    buy_coins_button.click()
    sleep(3)

@then("click on proceed to buy coins")
def step_impl(context):
    # Wait and click the "Proceed to buy coins" button
    wait = WebDriverWait(context.driver, 10)
    proceed_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class, 'button-continue')]//p[normalize-space()='Proceed to buy coins']")
    ))
    proceed_button.click()
    sleep(5)



@then("select the card option")
def handle_razorpay_payment_popup(context):
    driver = context.driver

    # Step 1: Switch to Razorpay iframe
    iframe = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='razorpay']"))
    )
    driver.switch_to.frame(iframe)

    # Step 2: Click on the UPI option
    # Wait for and click the visible div with data-value='card'
    card_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@data-value='card'])[1]"))
    )
    card_option.click()
    sleep(3)

#def step_impl(context):
    # wait = WebDriverWait(context.driver, 15)
    #
    # # Find the span with text "Cards"
    # cards_label = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//span[contains(text(), 'Cards')]")
    # ))
    #
    # # Click its clickable parent container
    # card_option_div = cards_label.find_element(By.XPATH, "./ancestor::div[contains(@class, 'cursor-pointer')]")
    # context.driver.execute_script("arguments[0].scrollIntoView(true);", card_option_div)
    # wait.until(EC.element_to_be_clickable(card_option_div)).click()
    # sleep(2)

    # wait = WebDriverWait(context.driver, 15)
    # # Find the 'Cards' option's container using the label
    # card_section = wait.until(EC.element_to_be_clickable((
    #     By.XPATH, "//span[contains(text(), 'Cards')]/ancestor::div[contains(@class, 'cursor-pointer')]"
    # )))
    #
    # # Scroll and click
    # context.driver.execute_script("arguments[0].scrollIntoView(true);", card_section)
    # card_section.click()
    # sleep(2)

    # wait = WebDriverWait(context.driver, 15)
    #
    # # Wait and click on the "Cards" option by visible text
    # cards_option = wait.until(EC.element_to_be_clickable((
    #     By.XPATH, "//div[contains(@class, 'flex') and .//text()[contains(., 'Cards')]]"
    # )))
    # cards_option.click()


#Handle the iframe - razor pay

    # # Switch to the iframe where Razorpay form is embedded
    # iframe = context.driver.find_element(By.XPATH, "//iframe[@name='razorpay-checkout-frame']")
    # context.driver.switch_to.frame(iframe)
    #
    # # Example for entering card number, expiry, and CVV (adjust according to field locators)
    # card_number = context.driver.find_element(By.NAME, 'card_number')
    # expiry_date = context.driver.find_element(By.NAME, 'expiry_date')
    # cvv = context.driver.find_element(By.NAME, 'cvv')
    #
    # card_number.send_keys('4111111111111111')
    # expiry_date.send_keys('12/23')
    # cvv.send_keys('123')
    # sleep(3)


@then("Add the card details")
def step_impl(context):
    # Wait until the card number field is present and enter the number
    wait = WebDriverWait(context.driver, 10)
    card_number_input = wait.until(EC.presence_of_element_located((By.NAME, "card.number")))
    card_number_input.clear()
    card_number_input.send_keys("4111111111111111")  # Example VISA test number

    # Wait until the expiry field is present and send expiry date
    wait = WebDriverWait(context.driver, 10)
    expiry_input = wait.until(EC.presence_of_element_located((By.NAME, "card.expiry")))
    expiry_input.clear()
    expiry_input.send_keys("12/26")  # Example expiry date

    # Wait for the CVV field to be available and input the value
    wait = WebDriverWait(context.driver, 10)
    cvv_input = wait.until(EC.presence_of_element_located((By.NAME, "card.cvv")))
    cvv_input.clear()
    cvv_input.send_keys("123")  # Replace with desired CVV for test
    sleep(3)

    continue_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))
    )
    continue_button.click()
    sleep(3)

@then("click on secure_card_button")
def step_impl(context):
    # Wait until the button is clickable and click it
    wait = WebDriverWait(context.driver, 10)
    secure_card_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='pay_and_save_card']")))
    secure_card_button.click()
    sleep(3)

@then("click on skip button")
def step_impl(context):
    # Locate the "Skip OTP" button using its text
    wait = WebDriverWait(context.driver, 10)
    skip_otp_button = context.driver.find_element(By.XPATH, "//button[text()='Skip OTP']")

    # Click the button to skip the OTP
    skip_otp_button.click()

    sleep(3)

@then("Enter OTP")
def step_impl(context):
    # Locate the OTP input field by its name attribute
    wait = WebDriverWait(context.driver, 10)
    otp_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter OTP']")))
    #otp_input = context.driver.find_element(By.XPATH, "//input[@placeholder='Enter OTP']")

    # Enter the OTP value into the input field
    otp_input.send_keys("000000")  # Replace with the actual OTP

    # Optionally, submit the form if there's a submit button or trigger the OTP verification
    # You can submit by finding the submit button and clicking it or just pressing ENTER
    otp_input.send_keys(Keys.RETURN)
    sleep(5)

@then("submit OTP")
def step_impl(context):
    # Locate the "Continue" button by its attributes
    wait = WebDriverWait(context.driver, 20)
    # Wait for and scroll the button into view
    continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue']")))
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", continue_button)

    # Use ActionChains to safely click (prevents overlay interference)
    actions = ActionChains(context.driver)
    actions.move_to_element(continue_button).click().perform()

    # Optional: wait for OTP processing
    sleep(5)  # Keep minimal. Increase only if necessary.

# @then("the company click on the menu")
# def step_impl(context):
# # Wait until the "Edit Profile" button is visible and clickable
#     wait = WebDriverWait(context.driver, 10)
#     menu_button = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, "//mat-icon[normalize-space()='keyboard_arrow_down']")
#     ))
# # Click the button
#     menu_button.click()
#     sleep(3)
#
#
# @then("Click on Coin history button")
# def step_impl(context):
#     # Wait for and click the "Buy Coins" button
#     wait = WebDriverWait(context.driver, 10)
#     Coin_history_button = wait.until(EC.element_to_be_clickable(
#         (By.XPATH, "//button[@role='menuitem']//span[normalize-space()='Coin History']")))
#
#     Coin_history_button.click()
#     sleep(3)





