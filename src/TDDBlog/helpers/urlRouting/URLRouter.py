from django.http import Http404, HttpResponse

class URLRouter(object):

    def __init__(self, routesMap):
        self.routesMap = routesMap

    def __getRoutesMatchingURL(self, url):
        matchingRoutes = []

        for route in self.routesMap.matchlist:
            match = route.match(url)
            if match:
                matchingRoutes.append(match)
        
        return matchingRoutes
    
    def __getRoutesMatchingHTTPmethod(self, routesMatchingURL, method = None):
        matchingRoute = None
        
        for route in routesMatchingURL:
            try:
                if route["conditions"]["method"] == method:
                    matchingRoute = route
                    break
            except KeyError:#has no conditions
                matchingRoute = route
                break
            
        return matchingRoute
    
    def __httpResponse405(self, method):
        response = HttpResponse('Method not allowed: %s' % method)
        response.status_code = 405
        return response
        
    def __prepareRoutesForMatching(self):
        #Called for of all the funky side effects it creates
        self.routesMap.match("/")
    
    
    def __getMatchingRouteBasedOnRequest(self,request):
        routesMatchingURL = self.__getRoutesMatchingURL(request.path) 
        
        if not routesMatchingURL :
            raise Http404
        
        matchingRoute = self.__getRoutesMatchingHTTPmethod(routesMatchingURL, request.method)
        
        return matchingRoute
    
    def __getControllersFunctionToCall(self, matchingRoute):
        controller = matchingRoute.pop("controller")
        actionName = matchingRoute.pop("action")
        controllersFunctionToCall = getattr(controller, actionName)
        return controllersFunctionToCall
    
    def __getParametersToPassToTheControllerFunction(self, route, kwargs):
        parameters = {}
        
        try:
            route.pop("conditions")
        except KeyError:
            pass
        
        for key in route.keys():
            parameters[key] = route[key]
        
        for key in kwargs.keys():
            parameters[key] = kwargs[key]
        
        return parameters
            
    def routeRequestToProperController(self, request, *args, **kwargs):   
        self.__prepareRoutesForMatching()
        
        matchingRoute = self.__getMatchingRouteBasedOnRequest(request)
        
        if matchingRoute is None : 
            return self.__httpResponse405(request.method)
        
        properControllerFunctionToCall = self.__getControllersFunctionToCall(matchingRoute)
        
        parameters = self.__getParametersToPassToTheControllerFunction(matchingRoute,kwargs)
        
        return properControllerFunctionToCall(request, *args, **parameters)