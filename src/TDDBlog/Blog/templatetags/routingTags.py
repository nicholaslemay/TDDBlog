from django.template import Node, TemplateSyntaxError, Library
from routes.util import url_for
from django.utils.encoding import smart_str

register = Library()

class URLForNode(Node):
    def __init__(self, view_name, args, kwargs):
        self.view_name = view_name
        self.args = args
        self.kwargs = kwargs

    def render(self, context):
        args = [arg.resolve(context) for arg in self.args]
        kwargs = dict([(smart_str(k,'ascii'), v.resolve(context))
                       for k, v in self.kwargs.items()])
        print self.view_name
        return url_for(self.view_name,**kwargs)
    
    
def get_url_for(parser, token):
    bits = token.contents.split(' ', 2)
    if len(bits) < 2:
        raise TemplateSyntaxError, "'%s' takes at least one argument (path to a view)" % bits[0]
    args = []
    kwargs = {}
    if len(bits) > 2:
        for arg in bits[2].split(','):
            if '=' in arg:
                k, v = arg.split('=', 1)
                kwargs[k] = parser.compile_filter(v)
            else:
                args.append(parser.compile_filter(arg))
    return URLForNode(bits[1], args, kwargs)

get_url_for = register.tag(get_url_for)
