import html4Symbols

def diff(a, b):
    b = set(b)
    return [aa for aa in a if aa not in b]

REMOVED_SYMBOLS = ['acronym','applet','basefont','big','center','dir','font','frame','frameset','noframes','strike','tt']

NEW_ELEMENTS = [
'canvas',
'audio'    ,
'video',
'source',
'embed',
'track',
'datalist',	#Specifies a list of pre-defined options for input controls
'keygen',	#Defines a key-pair generator field (for forms)
'output',	#Defines the result of a calculation
'article', #Defines an article
'aside',#Defines content aside from the page content
'bdi',#Isolates a part of text that might be formatted in a different direction from other text outside it
'command',#Defines a command button that a user can invoke
'details',#Defines additional details that the user can view or hide
'dialog',#Defines a dialog box or window
'summary',#Defines a visible heading for a 'details' element
'figure',#Specifies self-contained content, like illustrations, diagrams, photos, code listings, etc.
'figcaption',#Defines a caption for a 'figure' element
'footer',#Defines a footer for a document or section
'header',#Defines a header for a document or section
'mark',#Defines marked/highlighted text
'meter',#Defines a scalar measurement within a known range (a gauge)
'nav',#Defines navigation links
'progress',#Represents the progress of a task
'ruby',#Defines a ruby annotation (for East Asian typography)
'rt',#Defines an explanation/pronunciation of characters (for East Asian typography)
'rp',#Defines what to show in browsers that do not support ruby annotations
'section',#Defines a section in a document
'time',#Defines a date/time
'wbr'#Defines a possible line-break
]

CLOSING_TAGS = diff(html4Symbols.CLOSING_TAGS,REMOVED_SYMBOLS) + NEW_ELEMENTS
LINE_BREAK_AFTER = diff(html4Symbols.LINE_BREAK_AFTER,REMOVED_SYMBOLS) + NEW_ELEMENTS
NON_CLOSING_TAGS = diff(html4Symbols.NON_CLOSING_TAGS,REMOVED_SYMBOLS)
ONE_LINE = diff(html4Symbols.ONE_LINE,REMOVED_SYMBOLS)