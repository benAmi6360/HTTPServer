class UnknownRequestError(Exception):
    """This is an exception raised when not using a known request"""
    pass

class HandlePostRequest(Exception):
    """This is an exception raised when a post request is proccessed"""
    pass