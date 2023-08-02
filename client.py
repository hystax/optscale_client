from arcee.client import Client as ArceeCl
from rest_api.client import Client as RestClv1
from rest_api.client import Client as RestClv2
from insider.client import Client as InsiderCl


class NoAssociatedClientException(Exception):
    pass


class Client:

    cl_map = {
        'arcee': ArceeCl,
        'rest_v1': RestClv1,
        'rest_v2': RestClv2,
        'insider': InsiderCl,
    }

    def __init__(self, cls_t, *args, **kwargs):
        cls = self.__class__.cl_map.get(cls_t)
        if not cls:
            raise NoAssociatedClientException("No associated client")
        self._inner = cls(*args, **kwargs)

    def __getattr__(self, name):
        def _missing(*args, **kwargs):
            method = getattr(self._inner, name)
            return method(*args, **kwargs)
        return _missing
