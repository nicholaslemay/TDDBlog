from django.test.testcases import TestCase
from nose.tools import istest


class Test(TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    @istest
    def ItShouldRenderTheNewBlogTemplate(self):
        self.fail()

    @istest
    def ItShouldPassABlogPostFormToTheTemplate(self):
        self.fail()
