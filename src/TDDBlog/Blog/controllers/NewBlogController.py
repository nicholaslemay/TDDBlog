from TDDBlog.Helpers.Controller import Controller
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.template.context import RequestContext

class NewBlogPostController(Controller):
    
    @staticmethod
    def GET(request):
        return render_to_response("newBlog.html", context_instance=RequestContext(request))
    
    @staticmethod
    def POST(request):
        return redirect(reverse("thankYou"), context_instance=RequestContext(request))