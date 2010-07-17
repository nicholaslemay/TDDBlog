from django.core.urlresolvers import reverse


BLOG_TITLE = "//input[@id='id_title']"

BLOG_CONTENT = "//input[@id='id_content']"

CREATE_BLOG_POST_BUTTON = "//input[@id='id_create_blog_post']"


NEW_BLOG_PAGE = reverse('newBlog')

THANK_YOU_PAGE = reverse('thankYouPage')