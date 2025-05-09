from behave import given, when, then

@given("the company is logged in")
def step_impl(context):
    pass

@given("the company is on the message section")
def step_impl(context):
    pass

@given("the company is viewing received messages")
def step_impl(context):
    pass

@when("the company navigates to the message section")
def step_impl(context):
    pass

@when('the company clicks on "Start Chat"')
def step_impl(context):
    pass

@when("the company selects a contact to start chat")
def step_impl(context):
    pass

@when("the company composes and sends the first message")
def step_impl(context):
    pass

@when("the company navigates to the Pending tab")
def step_impl(context):
    pass

@when("the company navigates to the Received tab")
def step_impl(context):
    pass

@when("the company marks a message as read or unread")
def step_impl(context):
    pass

@then("the company should see a list of all message contacts")
def step_impl(context):
    pass

@then("each contact should display the name, profile picture, and latest message snippet")
def step_impl(context):
    pass

@then("the message should be sent successfully")
def step_impl(context):
    pass

@then("the chat should be initiated with the selected contact")
def step_impl(context):
    pass

@then("the company should see all pending messages")
def step_impl(context):
    pass

@then("the messages should require a response or action")
def step_impl(context):
    pass

@then("the company should see all received messages")
def step_impl(context):
    pass

@then("the messages should display the sender's name, profile picture, and message status")
def step_impl(context):
    pass

@then("the message status should be updated accordingly")
def step_impl(context):
    pass
