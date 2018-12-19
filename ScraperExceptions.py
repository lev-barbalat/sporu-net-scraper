# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class InvalidResponse(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass