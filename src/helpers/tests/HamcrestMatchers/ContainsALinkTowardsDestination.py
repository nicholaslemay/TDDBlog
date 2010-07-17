from hamcrest.core.base_matcher import BaseMatcher
from pyquery.pyquery import PyQuery



class ContainsALinkTowardsDestination(BaseMatcher):
    """Is the value equal to another value?"""
    
    def __init__(self, destination):
        self.destination = destination

    def _matches(self, page):
        pyQuery = PyQuery(page)
        results = pyQuery("a[href='%s']" %self.destination)
        return results != []

    def describe_to(self, description):
        description.append_text('ContainsALinkTowardsDestination')


"""Is the value equal to another value?"""
containingALinkTowards = ContainsALinkTowardsDestination