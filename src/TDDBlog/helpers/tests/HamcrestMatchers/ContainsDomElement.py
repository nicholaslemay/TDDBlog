from pyquery.pyquery import PyQuery
from hamcrest.core.base_matcher import BaseMatcher

class ContainsDomElement(BaseMatcher):
    """Is the value equal to another value?"""
    
    def __init__(self, elementtoSearchFor):
        self.elementtoSearchFor = elementtoSearchFor

    def _matches(self, page):
        pyQuery = PyQuery(page)
        results = pyQuery(self.elementtoSearchFor)
        return len(results) != 0

    def describe_to(self, description):
        description.append_text('ContainsDomObject')


"""Is the value equal to another value?"""
containining_dom_object = ContainsDomElement