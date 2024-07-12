from code_line_counter import CodeLineCounter

if __name__ == '__main__':
    code = "int a = 0;\n# this is a comment\n\nint b = 1;"
    counter = CodeLineCounter()
    count = counter.count(code)
    print(f"Number of lines of code: {count}")
