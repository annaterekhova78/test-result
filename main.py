# coding=utf8

tokens = (
    'NAME', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'LPAREN', 'RPAREN',
)
# Tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
    t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Недопустимый символ '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex


lexer = lex.lex()
if __name__ == "__main__":

    f = open("date.txt", "r")
    lexer.input(f.read())
    f.close()

    print("Результат выполнения сканера:")
    while True:
        tok = lexer.token()
        if not tok: break
        result_tok = tok
        print(tok)

    print("\nФайл с разрешением out:")
    result_file = open("test_result.out", "r")
    result_our = result_file.read()
    print(result_our)
    result_file.close()



