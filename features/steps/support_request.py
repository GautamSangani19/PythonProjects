from behave import given, when, then

@given("the company is logged in and on the dashboard")
def step_impl(context):
    # Navigate to dashboard after login
    pass

@when("the company clicks on the Support section")
def step_impl(context):
    # Click on the Support option from the dashboard menu
    pass

@when("the company adds a subject and description")
def step_impl(context):
    # Fill in subject and description fields in the support form
    pass

@when("the company uploads a screenshot")
def step_impl(context):
    # Simulate file upload (screenshot) using file input element
    pass

@when("the company clicks the Submit button")
def step_impl(context):
    # Click the Submit button on the support form
    pass

@then("the support request should be submitted successfully")
def step_impl(context):
    # Validate success message or redirection
    pass
