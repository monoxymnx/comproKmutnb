# def example_w_plus_mode():
#     with open("example.txt", "w+") as file:
#         file.write("Hello, World!\n")
#         file.write("This is a test file.\n")
#         file.seek(0)
#         content = file.read()
#         print(content)

# example_w_plus_mode()

def example_a_plus_mode():
    with open("example.txt", "a+") as file:
        file.seek(0)
        content = file.read()
        print(content)
        file.write("Appending a new line.\n")
        file.seek(0)
        updated_content = file.read()
        print(updated_content)
example_a_plus_mode()