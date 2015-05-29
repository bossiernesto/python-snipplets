# list of tags, from the HTML 4.01 specification

CLOSING_TAGS =  ['a', 'abbr', 'acronym', 'address', 'applet',
                 'b', 'bdo', 'big', 'blockquote', 'button',
                 'caption', 'center', 'cite', 'code',
                 'del', 'dfn', 'dir', 'div', 'dl',
                 'em', 'fieldset', 'font', 'form', 'frameset',
                 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                 'i', 'iframe', 'ins', 'kbd', 'label', 'legend',
                 'map', 'menu', 'noframes', 'noscript', 'object',
                 'ol', 'optgroup', 'pre', 'q', 's', 'samp',
                 'script', 'select', 'small', 'span', 'strike',
                 'strong', 'style', 'sub', 'sup', 'table',
                 'textarea', 'title', 'tt', 'u', 'ul',
                 'var', 'body', 'colgroup', 'dd', 'dt', 'head',
                 'html', 'li', 'p', 'tbody','option',
                 'td', 'tfoot', 'th', 'thead', 'tr']

NON_CLOSING_TAGS = ['area', 'base', 'basefont', 'br', 'col', 'frame',
                    'hr', 'img', 'input', 'isindex', 'link',
                    'meta', 'param']

# whitespace-insensitive tags, determines pretty-print rendering
LINE_BREAK_AFTER = NON_CLOSING_TAGS + ['html','head','body',
                                       'frameset','frame',
                                       'title','script',
                                       'table','tr','td','th','select','option',
                                       'form',
                                       'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                                       ]
# tags whose opening tag should be alone in its line
ONE_LINE = ['html','head','body',
            'frameset'
            'script',
            'table','tr','td','th','select','option',
            'form',
            ]