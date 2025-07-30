def format_strings(*args):
    if len(args) == 1 and " " in args[0]:
        return "-".join(args[0].split()).upper()
    return "".join(args).replace(" ", "").upper()

if __name__ == '__main__':
    result = format_strings("Hello", "world", "this", "is", "a", "test")
    print(result)

    result = format_strings("Python", "is", "fun")
    print(result)

    result = format_strings("Hello world")
    print(result)
