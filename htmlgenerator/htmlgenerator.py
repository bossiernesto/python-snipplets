"""Classes to generate HTML in Python

The HTMLTags module defines a class for all the valid HTML tags, written in
uppercase letters. To create a piece of HTML, the general syntax is :
    t = TAG(inner_HTML, key1=val1,key2=val2,...)

so that "print t" results in :
    <TAG key1="val1" key2="val2" ...>inner_HTML</TAG>

For instance :
    print A('bar', href="foo") ==> <A href="foo">bar</A>

To generate HTML attributes without value, give them the value True :
    print OPTION('foo',SELECTED=True,value=5) ==> 
            <OPTION value="5" SELECTED>

The inner_HTML argument can be an instance of an HTML class, so that 
you can nest tags, like this :
    print B(I('foo')) ==> <B><I>foo</I></B>

TAG instances support addition :
    print B('bar')+INPUT(name="bar") ==> <B>bar</B><INPUT name="bar">

and repetition :
    print TH('&nbsp')*3 ==> <TD>&nbsp;</TD><TD>&nbsp;</TD><TD>&nbsp;</TD>

For complex expressions, a tag can be nested in another using the operator <= 
Considering the HTML document as a tree, this means "add child" :

    form = FORM(action="foo")
    form <= INPUT(name="bar")
    form <= INPUT(Type="submit",value="Ok")

If you have a list (or any iterable) of instances, you can't concatenate the 
items with sum(instance_list) because sum takes only numbers as arguments. So 
there is a function called Sum() which will do the same :

    Sum( TR(TD(i)+TD(i*i)) for i in range(100) )

generates the rows of a table showing the squares of integers from 0 to 99

A simple document can be produced by :
    print HTML( HEAD(TITLE('Test document')) +
        BODY(H1('This is a test document')+
             'First line'+BR()+
             'Second line'))

This will be rendered as :
    <HTML>
    <HEAD>
    <TITLE>Test document</TITLE>
    </HEAD>
    <BODY>
    <H1>This is a test document</H1>
    First line
    <BR>
    Second line
    </BODY>
    </HTML>

If the document is more complex it is more readable to create the elements 
first, then to print the whole result in one instruction. For example :

head = HEAD()
head <= TITLE('Record collection')
head <= LINK(rel="Stylesheet",href="doc.css")

title = H1('My record collection')
table = TABLE()
table <= TR(TH('Title')+TH('Artist'))
for rec in records:
    row = TR()
    # note the attribute key Class with leading uppercase 
    # because "class" is a Python keyword
    row <= TD(rec.title,Class="title")+TD(rec.artist,Class="artist")
    table <= row

print HTML(head+BODY(title+table))
"""
import cStringIO
from html4Symbols import *
import keyword

class Tag:
    """Generic class for tags"""
    def __init__(self, inner_HTML="", **attrs):
        self.tag = self.__class__.__name__.replace('Tag','') if 'Tag' in self.__class__.__name__ else self.__class__.__name__
        self.inner_HTML = inner_HTML
        self.attrs = attrs
        self.children = []
        self.brothers = []
    
    def __str__(self):
        res=cStringIO.StringIO()
        w=res.write
        if self.tag != "Text":
            w("<%s" %self.tag)
            # attributes which will produce arg = "val"
            attr1 = [ k for k in self.attrs 
                if not isinstance(self.attrs[k],bool) ]
            w("".join([' %s="%s"' 
                %(k.replace('_','-'),self.attrs[k]) for k in attr1]))
            # attributes with no argument
            # if value is False, don't generate anything
            attr2 = [ k for k in self.attrs if self.attrs[k] is True ]
            w("".join([' %s' %k for k in attr2]))
            w(">")
        if self.tag in ONE_LINE:
            w('\n')
        w(str(self.inner_HTML))
        for child in self.children:
            w(str(child))
        if self.tag in CLOSING_TAGS:
            w("</%s>" %self.tag)
        if self.tag in LINE_BREAK_AFTER:
            w('\n')
        if hasattr(self,"brothers"):
            for brother in self.brothers:
                w(str(brother))
        return res.getvalue()

    def __le__(self,other):
        """Add a child"""
        if isinstance(other,str):
            other = text(other)
        self.children.append(other)
        other.parent = self
        return self

    def __add__(self,other):
        """Return a new instance : concatenation of self and another tag"""
        res = Tag()
        res.tag = self.tag
        res.inner_HTML = self.inner_HTML
        res.attrs = self.attrs
        res.children = self.children
        res.brothers = self.brothers + [other]
        return res

    def __radd__(self,other):
        """Used to add a tag to a string"""
        if isinstance(other,str):
            return text(other)+self
        else:
            raise ValueError,"Can't concatenate %s and instance" %other

    def __mul__(self,n):
        """Replicate self n times, with tag first : TAG * n"""
        res = Tag()
        res.tag = self.tag
        res.inner_HTML = self.inner_HTML
        res.attrs = self.attrs
        for i in range(n-1):
            res += self
        return res

    def __rmul__(self,n):
        """Replicate self n times, with n first : n * TAG"""
        return self*n

# create the classes
for tag in CLOSING_TAGS + NON_CLOSING_TAGS + ['text']:
    if keyword.iskeyword(tag):
        tag = 'Tag' + tag
    exec("class %s(Tag): pass" %tag)
    
def Sum(iterable):
    """Return the concatenation of the instances in the iterable
    Can't use the built-in sum() on non-integers"""
    it = [ item for item in iterable ]
    if it:
        return reduce(lambda x,y:x+y, it)
    else:
        return ''

if __name__ == '__main__':
    head = head(title('Test document'))
    body = body()
    body <= h1('This is a test document')
    body <= 'First line' + br() + 'Second line'
    body <= Tagdel("d")
    print html(head + body)