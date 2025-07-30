#append
fruits = ["apple", "banana", "cherry"]
more_fruits = ["mango", "pineapple"]
for fruit in more_fruits:
    fruits.append(fruit)
print(fruits)

#insert
berries = ["strawberry", "blueberry"]
berries.insert(1, "raspberry")
berries.insert(2, "blackberry")
print(berries)

#remove
fruits_with_duplicate = ["apple", "banana", "apple", "cherry","apple","kiwi"]
while "apple" in fruits_with_duplicate:
    fruits_with_duplicate.remove("apple")
print(fruits_with_duplicate)

#pop
grade = [85,90,78,92,88]
third_grade = grade.pop(2)
grade.append(third_grade)
print(grade)

#index
animals = ["cat", "dog", "rabbit", "hamster","dog","parrot"]
first_dog_index = animals.index("dog")
print(first_dog_index)
second_dog_index = animals.index("dog", first_dog_index + 1)
print(second_dog_index)

#clear
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
for sublist in nested_list:
    sublist.clear()
print(nested_list)

#sort
numbers = [4,2,3,1,5]
numbers.sort()
print(numbers)

#reverse
numbers = [1,2,3,4,5]
numbers.reverse()
print(numbers)