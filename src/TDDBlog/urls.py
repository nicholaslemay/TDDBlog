from django.conf.urls.defaults import patterns

from routes.mapper import Mapper
from TDDBlog.Blog.blogRoutes import blogRoutes
from TDDBlog.helpers.urlRouting.URLRouter import URLRouter
from routes import request_config



map = Mapper()
map.extend(blogRoutes)

urlRouter = URLRouter(map)

urlpatterns = patterns('',
                         (r'.*', urlRouter.routeRequestToProperController )
                       )
