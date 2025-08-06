attendance_week = [
    ["Alice", "Bob", "Charlie", "David"],
    ["Alice", "Charlie", "David"],
    ["Alice", "Bob", "David"],
    ["Alice", "David", "Eve"],
    ["Bob", "Charlie", "David"]
]
attendance_set = [set(day) for day in attendance_week]
print(attendance_set)

present_every_day = set.intersection(*attendance_set)
print("Students present every day:", present_every_day)
all_students = set.union(*attendance_set)
absent_at_least_one_day = all_students - present_every_day
print("Students absent at least one day:", absent_at_least_one_day)

first_day_present = attendance_set[0]
last_day_present = attendance_set[-1]
first_day_but_not_last = first_day_present - last_day_present
print("Students present on the first day but not on the last day:", first_day_but_not_last)

unique_studens_count = len(all_students)
print("Total unique students:", unique_studens_count)