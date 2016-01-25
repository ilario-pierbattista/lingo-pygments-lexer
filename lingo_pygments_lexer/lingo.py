from pygments.lexer import RegexLexer,include
from pygments.token import *


class LingoLexer(RegexLexer):
    name = 'Lingo'
    aliases = ['lingo', 'LINGO', 'Lingo']
    filenames = ['lng']

    char = r'[a-zA-Z$._0-9@]'
    identifier = r'(?:[a-zA-Z$_]' + char + '*|\.' + char + '+)'
    number = r'[+-]?(?:0[xX][a-zA-Z0-9]+|\d+)'
    binary_number = r'0b[01_]+'
    single_char = r"'\\?" + char + "'"
    string = r'"(\\"|[^"])*"'

    tokens = {
        'root': [
            include('whitespace'),
            (r'!.*;', Comment),
        ],

        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text),
            (r';', Text)
        ]
    }
