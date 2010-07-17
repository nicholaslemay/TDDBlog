from nose.tools import istest
from hamcrest.core.core.is_ import is_
from helpers.tests.HamcrestMatchers.ContainsALinkTowardsDestination import containingALinkTowards
from hamcrest.core.matcher_assert import assert_that
import unittest


class ContainsALinkTowardsDestinationTests(unittest.TestCase):
        
    @istest
    def ItShouldRaiseAnExceptionWhenLinkIsNotFound(self):
        try:
            assert_that( "<a href='/rotato'></a>", is_(containingALinkTowards("/potato")))
            raise Exception
        except (AssertionError, ), e:
            pass
        
    @istest
    def ItShouldNotRaiseAnExceptionWhenLinkIsFound(self):
        assert_that( "<a href='/potato'></a>", is_(containingALinkTowards("/potato")))
