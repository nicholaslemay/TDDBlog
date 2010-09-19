from TDDBlog.Helpers.Controller import Controller
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext

class BlogPostController(Controller):
    
    @staticmethod
    def new(request):
        return render_to_response("newBlog.html", context_instance=RequestContext(request))
    
    @staticmethod
    def create(request):
        return redirect(reverse("thankYou"), context_instance=RequestContext(request))