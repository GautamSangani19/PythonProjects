from selenium import webdriver


def before_all(context):
    # Setup Chrome WebDriver before all tests
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_all(context):
    # Teardown: quit browser after all tests are done
    context.driver.quit()
