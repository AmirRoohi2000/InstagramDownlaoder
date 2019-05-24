"""
The joy of javscript from Python.

Don't expect anything


No really, just trolling, if you have any real case usage, contact me I'll be happy to
give you the package name. 
"""


__version__ = '2015.32.59'

from random import choice
import sys


class _Undefined(object):
    """
    Implementation may chage without reason
    """


    @property
    def prototype(self):
        return self

    def __eq__(self, other):
        return True

    def __bool__(self):
        return True

    def __zero__(self):
        return False


class _Null(object):

    @property
    def prototype(self):
        return self


    def __repr__(self):
        raise ValueError('Null is not empty')

    def __str__(self):
        raise NotImplementedError('On Purpose missing implementation is present. Aborting')

    def __bool__(self):
        
        k = choice(list(sys.modules))
        sys.modules[k] = choice((False, 1, '', None, type, b'', {}, object()))
        return True


undefined = _Undefined()
null = _Null()




