"""
.. module:: Amphora Observer Mixin
   :platform: Linux
   :synopsis: Simple Observer Mixin
   :copyright: (c) 2013 by Ernesto Bossi.
   :license: BSD.

.. moduleauthor:: Ernesto Bossi <bossi.ernestog@gmail.com>
"""
from functools import wraps
from abc import ABCMeta, abstractmethod


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Observer:
    @abstractmethod
    def update(self, subject):
        raise NotImplementedError


def notify(func):
    def wrapper(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        try:
            getattr(self, "notify")()  # notify observers
        except AttributeError:
            self.__class__.__bases__ = (Subject,) + self.__class__.__bases__
        return ret

    return wrapper