import os


class Globals(object):
    # Line ending constants as text strings.
    C_CR = '\r'
    C_LF = '\n'
    C_CRLF = '\r\n'
    C_SYS = os.linesep
    C_LE = [C_CR, C_LF, C_CRLF, C_SYS]

    # Line ending constants as binary, encoded text strings.
    B_CR = '\r'.encode(encoding='utf-8')
    B_LF = '\n'.encode(encoding='utf-8')
    B_CRLF = '\r\n'.encode(encoding='utf-8')
    B_SYS = os.linesep.encode(encoding='utf-8')
    B_LE = [B_CR, B_LF, B_CRLF, B_SYS]
