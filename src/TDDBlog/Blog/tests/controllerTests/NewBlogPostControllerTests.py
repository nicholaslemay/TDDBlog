from django.test.testcases import TestCase
from nose.tools import istest
from django.test.client import Client
from django.core.urlresolvers import reverse
import TDDBlog.testSettings

class NewBlogPostControllerTests(TestCase):

    def setUp(self):
        client = Client()
        self.GET = client.get
        self.POST = client.post

    def tearDown(self):
        pass

    @istest
    def ItShouldReturnA200WhenCalledWithGET(self):
        response = self.GET(reverse("newBlog"))
        self.assertEquals(200, response.status_code)
    
    @istest
    def ItShouldRenderTheNewBlogTemplate(self):
        response = self.GET(reverse("newBlog"))
        self.assertTemplateUsed(response, "newBlog.html")
    
    @istest
    def ItShouldRedirectToTheThankYouPageWhenCalledWithPOST(self):
        response = self.POST(reverse("newBlog"))
        self.assertRedirects(response, reverse("thankYou"))