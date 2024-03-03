from enum import Enum

# Importing macros from parser_macro.py
from parser_macro import *

class TokenType(Enum):
    EWHITESPACE = 0
    ENAME = 1
    ERATIONAL = 2
    EIMAGINARY = 3
    EDELIMITER = 4
    ESYMBOL = 5
    EEXPRESSION = 6
    EEMPTY = 7

class Tokenizer:
    def __init__(self, raw):
        self._raw = raw
        self._current_pos = 0

    def __del__(self):
        pass

    # Main function
    def scan_token(self, holder):
        pass

    # Exception classes
    class BadFormat(Exception):
        def __str__(self):
            return "Input has bad format"

    class EmptyInput(Exception):
        def __str__(self):
            return "Input is empty"

    # Parsing utils
    def _find(self, charset):
        pass

    def _find_not_of(self, charset, pos=None):
        pass

    def _update_token(self, next_pos):
        pass
