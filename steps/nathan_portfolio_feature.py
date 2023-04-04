from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('the user is on the about section')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://nathan-fleet.com")
    time.sleep(5)

    # Find about section
    about_section = context.driver.find_element(By.ID, 'about')

    assert about_section.is_displayed()

@when('the user clicks on the GitHub icon')
def step_impl(context):
    about_section = context.driver.find_element(By.ID, 'about')
    github_icon = about_section.find_element(By.XPATH, '//img[@alt="GitHub"]')
    github_icon.click()

@then('the user should be taken to "https://github.com/nathanfleet"')
def step_impl(context):
    time.sleep(5)
    # Switch to the new tab
    context.driver.switch_to.window(context.driver.window_handles[1])

    assert "github.com/nathanfleet" in context.driver.current_url
    context.driver.quit()
