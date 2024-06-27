"""
This type stub file was generated by pyright.
"""

"""
Provides various throttling policies.
"""
class BaseThrottle:
    """
    Rate throttling of requests.
    """
    def allow_request(self, request, view):
        """
        Return `True` if the request should be allowed, `False` otherwise.
        """
        ...
    
    def get_ident(self, request): # -> str:
        """
        Identify the machine making the request by parsing HTTP_X_FORWARDED_FOR
        if present and number of proxies is > 0. If not use all of
        HTTP_X_FORWARDED_FOR if it is available, if not use REMOTE_ADDR.
        """
        ...
    
    def wait(self): # -> None:
        """
        Optionally, return a recommended number of seconds to wait before
        the next request.
        """
        ...
    


class SimpleRateThrottle(BaseThrottle):
    """
    A simple cache implementation, that only requires `.get_cache_key()`
    to be overridden.

    The rate (requests / seconds) is set by a `rate` attribute on the Throttle
    class.  The attribute is a string of the form 'number_of_requests/period'.

    Period should be one of: ('s', 'sec', 'm', 'min', 'h', 'hour', 'd', 'day')

    Previous request information used for throttling is stored in the cache.
    """
    cache = ...
    timer = ...
    cache_format = ...
    scope = ...
    THROTTLE_RATES = ...
    def __init__(self) -> None:
        ...
    
    def get_cache_key(self, request, view):
        """
        Should return a unique cache-key which can be used for throttling.
        Must be overridden.

        May return `None` if the request should not be throttled.
        """
        ...
    
    def get_rate(self): # -> Any | str | None:
        """
        Determine the string representation of the allowed request rate.
        """
        ...
    
    def parse_rate(self, rate): # -> tuple[None, None] | tuple[int, int]:
        """
        Given the request rate string, return a two tuple of:
        <allowed number of requests>, <period of time in seconds>
        """
        ...
    
    def allow_request(self, request, view): # -> bool:
        """
        Implement the check to see if the request should be throttled.

        On success calls `throttle_success`.
        On failure calls `throttle_failure`.
        """
        ...
    
    def throttle_success(self): # -> Literal[True]:
        """
        Inserts the current request's timestamp along with the key
        into the cache.
        """
        ...
    
    def throttle_failure(self): # -> Literal[False]:
        """
        Called when a request to the API has failed due to throttling.
        """
        ...
    
    def wait(self): # -> None:
        """
        Returns the recommended next request time in seconds.
        """
        ...
    


class AnonRateThrottle(SimpleRateThrottle):
    """
    Limits the rate of API calls that may be made by a anonymous users.

    The IP address of the request will be used as the unique cache key.
    """
    scope = ...
    def get_cache_key(self, request, view): # -> str | None:
        ...
    


class UserRateThrottle(SimpleRateThrottle):
    """
    Limits the rate of API calls that may be made by a given user.

    The user id will be used as a unique cache key if the user is
    authenticated.  For anonymous requests, the IP address of the request will
    be used.
    """
    scope = ...
    def get_cache_key(self, request, view): # -> str:
        ...
    


class ScopedRateThrottle(SimpleRateThrottle):
    """
    Limits the rate of API calls by different amounts for various parts of
    the API.  Any view that has the `throttle_scope` property set will be
    throttled.  The unique cache key will be generated by concatenating the
    user id of the request, and the scope of the view being accessed.
    """
    scope_attr = ...
    def __init__(self) -> None:
        ...
    
    def allow_request(self, request, view): # -> bool:
        ...
    
    def get_cache_key(self, request, view): # -> str:
        """
        If `view.throttle_scope` is not set, don't apply this throttle.

        Otherwise generate the unique cache key by concatenating the user id
        with the `.throttle_scope` property of the view.
        """
        ...
    


