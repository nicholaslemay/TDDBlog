from django.core.urlresolvers import reverse
import TDDBlog.testSettings

BLOG_TITLE = "//input[@id='id_title']"

BLOG_CONTENT = "//input[@id='id_content']"

CREATE_BLOG_POST_BUTTON = "//button[@id='id_create_blog_post']"


NEW_BLOG_PAGE = reverse('newBlog')

THANK_YOU_PAGE = TDDBlog.testSettings.TEST_HOST +  reverse('thankYou')