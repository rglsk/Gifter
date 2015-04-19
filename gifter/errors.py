#!/usr/bin/env python
import logging


class BaseException(Exception):
    """ Base exception class. """

    def __init__(self, message=None):
        self.message = message
        logging.error('%s: %s', self.__class__.__name__, self.message)
        super(BaseException, self).__init__(self.message)


class NoAccesTokenError(BaseException):
    """Exception error class for non-existent access token"""


class FacebookApiError(BaseException):
    """Exception error class for facebook-sdk API"""


class CategoryNotFoundError(BaseException):
    """Exception error class for not found category id"""


class ItemsNotFoundError(BaseException):
    """Exception error class for not found items"""
