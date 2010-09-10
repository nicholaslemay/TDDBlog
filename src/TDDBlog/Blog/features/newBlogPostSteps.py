from TDDBlog.Blog.tests.acceptanceTests import BlogLocators
from TDDBlog.testSettings import SELENIUM_HOST, SELENIUM_PORT, \
    SELENIUM_BROWSER_START_COMMAND, TEST_HOST
from TDDBlog.externalLibraries.FluentSelenium.SeleniumDrivenUser import \
    SeleniumDrivenUser
from TDDBlog.externalLibraries.FluentSelenium.SharedSeleniumExecutionContext import \
    SharedSeleniumExecutionContext
from lettuce import *


seleniumExecutionContext = SharedSeleniumExecutionContext(SELENIUM_HOST, SELENIUM_PORT, SELENIUM_BROWSER_START_COMMAND, TEST_HOST)
user = SeleniumDrivenUser(seleniumExecutionContext)

@after.all
def tearDown(total):
    seleniumExecutionContext.destroy()

@step("I go to the blog creation page")
def userGoesToTheNewBlogPage(step):
    user.goesTo(BlogLocators.NEW_BLOG_PAGE)
    
@step('I fill the blogs title with "([^\"]*)"')
def userFillsTitle(step, title):
    user.fillsOut(BlogLocators.BLOG_TITLE).withThis(title)
    
@step('I fill the blogs content with "([^\"]*)"')
def userFillsContent(step, content):
    user.fillsOut(BlogLocators.BLOG_CONTENT).withThis("It can be done")
  
@step("I submit my blog")
def userSubmitsHisBlog(step):
    user.clicks(BlogLocators.CREATE_BLOG_POST_BUTTON).andThen().waitsForPageToLoad()
 
@step("Then I should see a thank you page")
def userShouldBeOnTheThankYouPage(step):
    user.shouldBeOnPage(BlogLocators.THANK_YOU_PAGE)
    