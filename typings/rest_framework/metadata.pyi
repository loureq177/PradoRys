"""
This type stub file was generated by pyright.
"""

"""
The metadata API is used to allow customization of how `OPTIONS` requests
are handled. We currently provide a single default implementation that returns
some fairly ad-hoc information about the view.

Future implementations might use JSON schema or other definitions in order
to return this information in a more standardized way.
"""
class BaseMetadata:
    def determine_metadata(self, request, view):
        """
        Return a dictionary of metadata about the view.
        Used to return responses for OPTIONS requests.
        """
        ...
    


class SimpleMetadata(BaseMetadata):
    """
    This is the default metadata implementation.
    It returns an ad-hoc set of information about the view.
    There are not any formalized standards for `OPTIONS` responses
    for us to base this on.
    """
    label_lookup = ...
    def determine_metadata(self, request, view): # -> dict[str, Any | list[Any]]:
        ...
    
    def determine_actions(self, request, view): # -> dict[Any, Any]:
        """
        For generic class based views we return information about
        the fields that are accepted for 'PUT' and 'POST' methods.
        """
        ...
    
    def get_serializer_info(self, serializer): # -> dict[Any, dict[str, Any | bool]]:
        """
        Given an instance of a serializer, return a dictionary of metadata
        about its fields.
        """
        ...
    
    def get_field_info(self, field): # -> dict[str, Any | bool]:
        """
        Given an instance of a serializer field, return a dictionary
        of metadata about it.
        """
        ...
    


