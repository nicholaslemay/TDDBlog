from nose.tools import istest
from django.test.testcases import TestCase
from externalLibraries.FluentSelenium.SharedSeleniumExecutionContext import SharedSeleniumExecutionContext
from externalLibraries.FluentSelenium.SeleniumDrivenUser import SeleniumDrivenUser
from TDDBlog.testSettings import SELENIUM_HOST, SELENIUM_PORT,\
    SELENIUM_BROWSER_START_COMMAND, TEST_HOST
from TDDBlog.Blog.tests.acceptanceTests import BlogLocators

class NewBlogPostAcceptanceTests(TestCase):

    def setUp(self):
        self.seleniumExecutionContext = SharedSeleniumExecutionContext(SELENIUM_HOST, SELENIUM_PORT, SELENIUM_BROWSER_START_COMMAND, TEST_HOST)
        self.user = SeleniumDrivenUser(self.seleniumExecutionContext)   
    
    @istest
    def ItShouldAllowTheUserToCreateABlogPosAndRedirectHimToAThankYouPage(self):
        self.user.goesTo(BlogLocators.NEW_BLOG_PAGE)\
                 .andThen().fillsOut(BlogLocators.BLOG_TITLE).withThis("Test Driving A Django Application")\
                 .andThen().fillsOut(BlogLocators.BLOG_CONTENT).withThis("It can be done")\
                 .andThen().clicks(BlogLocators.CREATE_BLOG_POST_BUTTON)\
                 .andThen().waitsForPageToLoad()\
                 .andThen().shouldBeOnPage(BlogLocators.THANK_YOU_PAGE)
                 
                