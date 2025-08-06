std = {"name": "Alice", "age": 25, "grade": "A",}

std["age"] = 26
std["major"] = "Computer Science"
print(std)

del std["grade"]
print(std)

removed_major = std.pop("major")
print(removed_major)
print(std)