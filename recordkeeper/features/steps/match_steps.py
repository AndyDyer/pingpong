from behave import given, when, then, step
from hamcrest import assert_that, equal_to
from match import Match


@given('there are no winners determined')
def step_impl(context):
    context.match = Match(games=['11:4'], player1_id='1', player2_id='2')


@then('it should determine a winner')
def step_impl(context):
    assert_that(context.match.winner, equal_to('1'))


@given('there is a winner on file')
def step_impl(context):
    context.match = Match(games=['11:4'], winner='2', loser='1')


@then('it should not determine anything')
def step_impl(context):
    assert_that(context.match.winner, equal_to('2'))


@given('there are all required fields for a match')
def step_impl(context):
    context.match = Match(games=['11:4'], winner='2', loser='1')


@then('it should return the match in a sheet friendly format')
def step_impl(context):
    assert_that(type(context.match.toRow()), equal_to(type([])))
    assert_that(len(context.match.toRow()), equal_to(3))


@then('it should return the match in an app friendly format')
def step_impl(context):
    assert_that(type(context.match.toDict()), equal_to(type({})))
