class MetaSingleton(type):
    instance = None
    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(MetaSingleton, cls).__call__(*args, **kw)
        return cls.instance


class Bar(object):
    __metaclass__=MetaSingleton

import unittest

class testMetaSingleton(unittest.TestCase):

    def setUp(self):
        self.bar=Bar()
        self.foo=Bar()

    def testSingleton(self):
        self.assertEqual(self.bar,self.foo)

if __name__ == '__main__':
    unittest.main()