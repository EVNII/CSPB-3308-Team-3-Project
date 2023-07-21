"""
`Singleton()` Meta type

Author: Yuzhou Shen

Last Edit: UTC+8 2023/7/21 21:25
"""


from threading import Lock

class Singleton(type):
    """
    Singleton: a design pattern, only allow one instance for one type of class
    """

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]