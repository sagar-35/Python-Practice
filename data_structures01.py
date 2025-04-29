#data_structures 
#list 
fruits = ['apple', 'banana']
fruits.append("Orange")
print(fruits)

#numbers_list
numbers = [1,2,3,4,5,6,7]
numbers.append(60)
print(numbers)

#loop_list
for fruit in fruits:
    print(fruit)


for number in numbers:
    print(number)

# insert (index , value)
fruits = ["apple", "Orange"]
fruits.insert(0, "Mango")
print(fruits)


#remove(value)
fruits = ["apple", "Orange", "banana", "mango"]
fruits.remove("apple")
print(fruits)

#pop(index)
fruits = ["apple", "Orange", "banana", "mango"]
fruits.pop(1)
print(fruits)


#sort()(choto theke boro)
number = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,1,2,5,3,4]
number.sort()
print(number)

#reverse()(list ke ulto kore fela)
numbers = [20,15,13,12,11]
numbers.reverse()
print(numbers)


#set(only for unique values)
my_set = {"apple", "Orange", "banana", "mango","Orange", "Orange1"}
my_set.add("Orange")
print(my_set)

#remove
my_set.remove("Orange")
print(my_set)

#loop
for my_set1 in my_set:
    print(my_set1)

