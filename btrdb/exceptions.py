# btrdb.exceptions
# Module for custom exceptions
#
# Author:   PingThings
# Created:  Tue Dec 18 14:50:05 2018 -0500
#
# For license information, see LICENSE.txt
# ID: exceptions.py [] allen@pingthings.io $

"""
Module for custom exceptions
"""


class BTrDBError(Exception):
    """
    The root exception for all package related errors.
    """
    def __init__(self, code, msg, mash):
        self.code = code
        self.msg = msg
        self.mash = mash

    @staticmethod
    def fromProtoStat(protoStatus):
        return BTrDBError(protoStatus.code, protoStatus.msg, protoStatus.mash)

    @staticmethod
    def checkProtoStat(protoStatus):
        stat = BTrDBError.fromProtoStat(protoStatus)
        if stat.isError():
            raise stat

    def isError(self):
        return self.code != 0

    def __repr__(self):
        return "{4}({0}, {1}, {2})".format(repr(self.code), repr(self.msg), repr(self.mash), self.__class__.__name__)

    def __str__(self):
        if self.isError():
            return "[{0}] {1}".format(self.code, self.msg)
        else:
            return "<success>"


class ConnectionError(Exception):
    """
    A problem interacting with the BTrDB server.
    """
    pass

class InvalidOperation(Exception):
    """
    An invalid BTrDB operation has been requested.
    """
    pass

class NotFound(Exception):
    """
    A problem interacting with the BTrDB server.
    """
    pass

class BTRDBValueError(ValueError):
    """
    A problem interacting with the BTrDB server.
    """
    pass

class BTRDBTypeError(TypeError):
    """
    A problem interacting with the BTrDB server.
    """
    pass
