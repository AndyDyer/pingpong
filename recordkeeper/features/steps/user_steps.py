from behave import given, when, then, step
from hamcrest import assert_that, equal_to
from user import User


@given('there are all required fields for a user')
def step_impl(context):
    context.user = User('123', 'andy', 1005, 5, 2)

@then('it should return the user in a sheet friendly format')
def step_impl(context):
    assert_that(type(context.user.toRow()), equal_to(type([])))
    assert_that(len(context.user.toRow()), equal_to(5))


@then('it should return the user in an app friendly format')
def step_impl(context):
    assert_that(type(context.user.toDict()), equal_to(type({})))
