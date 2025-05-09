# features/environment.py

from selenium import webdriver

def before_all(context):
    """Called once before all tests."""
    context.driver = webdriver.Chrome()  # Initialize Chrome driver
    context.driver.maximize_window()  # Maximize the browser window

def after_all(context):
    """Called once after all tests."""
    context.driver.quit()  # Close the browser after tests

