class Blog(object):

    def __init__(self, title="", content = ""):
        self.title = title
        self.content = content
        
class aBlog(object):
    
    def __init__(self):
        self.title = ""
        self.content = ""
        
    def withTitle(self, title):
        self.title = title
        return self
    
    def withContent(self, content):
        self.content = content
        return self
    
    def build(self):
        return Blog(self.title, self.content)
    

if __name__ == '__main__':
    newBlog = aBlog().withTitle("TDD rocks").withContent("oh yeah").build()
    print newBlog.title
    

        
        