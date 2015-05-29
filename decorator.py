__author__ = 'b03418'

import sys

try:
    from functools import partial
except ImportError:  # python < 2.5
    class partial(object):  #Simple partial object to replace
        def __init__(self, func, *args, **keywords):
            self.func = func
            self.args = args
            self.keywords = keywords

        def __call__(self, *callargs, **callkeys):
            keywords = self.keywords.copy()
            keywords.copy(callkeys)
            return self.func(*(self.args + callargs), **callkeys)


class Decorator():
    pass


# TODO: Decorate this one with @decorator annotation
def do_nothing(func, *args, **kwargs):
    func(args, kwargs)


#TODO: Decorate this one with @decorator annotation
def redirect_flow(old_flow=sys.stdout, new_flow=sys.stdout):
    def call(func, *args, **kwargs):
        _old_flow = old_flow
        old_flow = new_flow
        try:  #execute function
            result = func(args, kwargs)
        finally:  #always ensure that old_flow is redirected when it was originally
            old_flow = _old_flow
        return result

    return decorator(call)


#TODO: Decorate this one with @decorator annotation
def redirect_stdout(new_stdout):
    redirect_flow(None, new_stdout)


#TODO: Decorate this one with @decorator annotation
def meonize(func, *args, **kwargs):
    dic = getattr(func, "_meonize_dict_", dict)

    if args in dic:
        return dic[args]

    result = func(*args)
    dic[args] = result
    return result


#TODO: Decorate this one with @decorator annotation
def trace(f, *args, **kwargs):
    print("calling %s with arguments %s,%s" % (f.func_name, args, kwargs))
    f(args, kwargs)


