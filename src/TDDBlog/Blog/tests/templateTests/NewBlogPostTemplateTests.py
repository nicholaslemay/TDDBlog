from TDDBlog.helpers.tests.HamcrestMatchers.ContainsDomElement import \
    containining_dom_object
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.test.testcases import TestCase
from hamcrest.core.core.is_ import is_
from hamcrest.core.matcher_assert import assert_that
from mockito.mock import Mock
from nose.tools import istest
from pyquery.pyquery import PyQuery
import TDDBlog.testSettings



class NewBlogPostTemplateTests(TestCase):

    def setUp(self):
        pass

    def __getNewBlogPostPage(self):
        return PyQuery(render_to_string("newBlog.html",{}))
#===============================================================================
#    def __getNewBlogPostTemplateRendered(self):
#        newBlogPostForm = Mock()
#        newBlogPostForm.title = "<input id='id_title'></input>"
#        newBlogPostForm.content = "<input id='id_content'></input>"       
#        return render_to_string("newBlogPost.html",{"newBlogPostForm":newBlogPostForm})
#         
#    @istest
#    def ItShouldContainTheTitleInputField(self):
#        print self.__getNewBlogPostTemplateRendered()
#        assert_that(self.__getNewBlogPostTemplateRendered(), containining_dom_object("#id_title"))
# 
#    @istest
#    def ItShouldContainTheContentInputField(self):
#        assert_that(self.__getNewBlogPostTemplateRendered(), is_(containining_dom_object("#id_content")))
#        
#    @istest
#    def ItShouldContainTheSubmitBlogPostButton(self):
#        assert_that(self.__getNewBlogPostTemplateRendered(), is_(containining_dom_object("#id_create_blog_post")))
#    
#===============================================================================
    @istest
    def ItShouldContainAFormWithTheNewBlogPostUrlAsItsAction(self):
        newBlogPostPage = self.__getNewBlogPostPage()
        assert_that(newBlogPostPage, is_(containining_dom_object("form[action='%s'] " %(reverse("newBlog") ) ) ) )