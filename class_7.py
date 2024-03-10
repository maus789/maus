print(f"NameError {type (NameError)}-{issubclass (NameError, BaseException)}")


a = 1
b = 0
try:
    a/b
except ZeroDivisionError:
    print("Не можна ділити на нуль")


try:
    f = open("file.txt", "r")
except FileNotFoundError:
    print("Файл не знайдено")


try:
    a = 1
    b = 0
    a / b
except ZeroDivisionError:
    print("Не можна ділити на нуль")


try:
    f = open("file.txt", "r")
except FileNotFoundError:
    print("Файл не знайдено")


import warnings

warnings.warn(message: "Warning, no code here", SyntaxWarning)


import warnings

warnings.simplefilter( action: "ignore", SyntaxWarning)
warnings.simplefilter(action: "always", ImportWarning)

warnings.warn(message: "Warning, no code here", SyntaxWarning)
warnings.warn(message: "Warning, module not import", ImportWarning)


import warnings

warnings.simplefilter (action: ignore", SyntaxWarning)
warnings.simplefilter (action: "error", ImportWarning)

warnings.warn( message: "Warning, no code here", SyntaxWarning)
try:
    warnings.warn(message: "Warning, module not import", ImportWarning)
except:
    print("Warning processed")