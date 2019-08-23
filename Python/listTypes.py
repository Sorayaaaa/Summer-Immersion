print("general list")
numbers = [1,2,3,4]
more=[numbers, 2,3]
print(more)
num=[1,"cat"]
print(num)

print("extended List")
exampleList = ["a","b","c"]
print (exampleList)
exampleList.extend(["cow","moo"])
print(exampleList)

print("sliced list")
exampleList = ["a","b","c","shark", 2, 5]
print(exampleList)
obj_slice= slice (1, 4, 1)
print(exampleList[obj_slice])

print("searching lists")
data = [['a','b'], ['a','c'],['b','d']]
search = 'c'
for sublist in data:
  if sublist[1] == search:
    print ("Found it!", sublist)
    break
vowels = ["a", "e", "i", "o", "u"]
index = vowels.index("e")
print("the index of e is ", index)

print("sorting list")
randoList = [5, 7, 7, 8, 9, 2, 3, 5]
randoStrList = ["cat" , "cow" , "poodle", "pig"]
randoList.sort(reverse = True)
randoStrList.sort()
print('sorted list (in descending):', randoList)
print("string sorted List", randoStrList)

print("tuple list")
tup = ("python" , "geeks")
print(tup)
tuple3 = ("python",)*3
print(tuple3)
