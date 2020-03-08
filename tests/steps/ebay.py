from behave import given, when, then
from framework.webapp import webapp
from pages.ebay import ebayPage


@given(u'I load the ebay website')
def step_impl(context):
    webapp.load_website()
    ebayPage.verify_page_title()


@when('I enter the "{value}" on search window')
def step_impl(context, value):
    ebayPage.enter_search_value(value)
    print('Search value {}'.format(value))


@when('I select the "{categories}"')
def step_impl(context, categories):
    ebayPage.select_categories(categories)
    print('Search categories {}'.format(categories))


@then("I click the search button")
def step_impl(context):
    ebayPage.click_search_button()
    print('Click search button')


@then('I expect search results display "{value}"')
def step_impl(context, value):
    ebayPage.search_result_match_search_value(value)
    print('Search result display')


@then("I collect the item_name and item_price")
def step_impl(context):
    ebayPage.write_search_results()
    print("collect the item_name and item_price")
