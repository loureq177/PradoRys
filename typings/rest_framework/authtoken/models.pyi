"""
This type stub file was generated by pyright.
"""

from django.db import models

class Token(models.Model):
    """
    The default authorization token model.
    """
    key = ...
    user = ...
    created = ...
    class Meta:
        abstract = ...
        verbose_name = ...
        verbose_name_plural = ...
    
    
    def save(self, *args, **kwargs): # -> None:
        ...
    
    @classmethod
    def generate_key(cls): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    


class TokenProxy(Token):
    """
    Proxy mapping pk to user pk for use in admin.
    """
    @property
    def pk(self):
        ...
    
    class Meta:
        proxy = ...
        abstract = ...
        verbose_name = ...
        verbose_name_plural = ...
    
    


