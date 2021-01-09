class RiordinatoError(Exception):
    """Riordinato base exception"""

class DirNotExitsError(RiordinatoError):
    """Riordinato not found dir"""
