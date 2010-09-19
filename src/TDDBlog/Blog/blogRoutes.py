from routes.route import Route
from TDDBlog.Blog.controllers.NewBlogController import BlogPostController

blogRoutes = [ Route("newBlog", "/blog/new/", controller=BlogPostController, action="new",  conditions=dict(method=["GET"])),
               Route("createBlog", "/blog/new/", controller=BlogPostController, action="create",  conditions=dict(method=["POST"])),
             ]