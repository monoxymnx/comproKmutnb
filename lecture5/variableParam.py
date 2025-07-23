def displayInfo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
displayInfo(name="Elsa", age=30, city="Ubonratchathani")