from django.conf.urls.defaults import *
from TDDBlog.Blog.controllers.NewBlogController import BlogPostController

urlpatterns = patterns('',
                       url(r'^new/', BlogPostController(), name="newBlog"),
                       url(r'^thankyou/', "django.views.generic.simple.direct_to_template",{'template': 'thankYou.html'},name="thankYou")
                       )