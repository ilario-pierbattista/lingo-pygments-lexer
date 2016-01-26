from pygments.lexer import RegexLexer,include
from pygments.token import *


class LingoLexer(RegexLexer):
    name = 'Lingo'
    aliases = ['lingo', 'LINGO', 'Lingo']
    filenames = ['*.lng']

    KEYWORDS = [
        "MODEL",
        "END",
        "SETS",
        "ENDSETS",
        "DATA",
        "ENDDATA"
    ]

    BUILT_IN_FUNCS = [
        "@FOR",
        "MIN",
        "@SUM"
    ]

    char = r'[a-zA-Z$._0-9@]'
    identifier = r'(?:[a-zA-Z$_]' + char + '*|\.' + char + '+)'
    number = r'[+-]?(?:0[xX][a-zA-Z0-9]+|\d+)'
    #binary_number = r'0b[01_]+'
    #single_char = r"'\\?" + char + "'"
    #string = r'"(\\"|[^"])*"'

    tokens = {
        'root': [
            (r'(?i)(' + '|'.join(KEYWORDS) + ')', Keyword),
            (r'(?i)(' + '|'.join(BUILT_IN_FUNCS) + ')', Keyword),
            (identifier, Name.Label),
            include('whitespace'),
            include('comments'),
            include('punctuation'),
            include('operators'),
            include('litterals'),
        ],

        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text),
        ],

        'comments': [
            (r'!.*;', Comment),
        ],

        'punctuation': [
            (r'[:{};,\(\)]', Punctuation)
        ],

        'operators': [
            (r'[\+\-<>=\[\]\*/\^]', Operator)
        ],

        'litterals': [
            (number, Number)
        ]
    }
