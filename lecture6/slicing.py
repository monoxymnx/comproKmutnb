data = list(range(100))
slice_data = data[10:51:5]
print(slice_data)

#negative slicing
numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[-5:-1])
print(numbers[::-1])

#string slicing
ss = "Sammy Shark!"
print(ss[4])
print(ss[6:11])
print(ss[:5])
print(ss[7:])
print(ss[-4:-1])
print(ss[6:11])
print(ss[6:11:1])
print(ss[0:12:2])
print(ss[0:12:4])
print(ss[::4])
print(ss[::-1])
print(ss[::-2])