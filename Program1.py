# Basic operation on list, tuple, set, dict 

print("Arithmetic Operation\n")

a = int(input("enter an integer :"))
b = int(input("enter an integer :"))

l1=[]
sum1 = a+b
print("Addition :",sum1)
l1.append(sum1)
sub = a-b
print("Substraction :",sub)
l1.append(sub)
mul = a*b
print("Multiplication :",mul)
l1.append(mul)
div = a/b
print("Division :",div)
l1.append(div)
mod = a+b
print("Modlus :",mod)
l1.append(mod)
print("Printing Arithmetic Operation List :",l1)

#Using List
l1.append(6)
print("After appending 6:", l1)
# Insert a number at index 2
l1.insert(2, 10)
print("After inserting 10 at index 2:", l1)

l2=[]
# Calculate the sum of list in other list
l2 = sum(l1)
print("Sum of list elements:", l2)

#Using Tuple
print("\nUsing Tuples:")
t1 = (1, 2, 3, 4, 5)
#sum of total ele
tuple_sum = sum(t1)
print("Sum of tuple elements:", tuple_sum)

#Using Sets
print("\nUsing Sets:")
s1 = {1, 2, 3, 4, 5}
s2 = {5, 6, 7, 8}
# Remove a number
s1.discard(3)
print("After removing 3:", s2)
union_set = s1.union(s2)
print("Union with another set:", union_set)

# Using Dictionaries
print("\nUsing Dictionaries:")
d1 = {'a': 1, 'b': 2, 'c': 3}
# Adding a new key-value pair
d1['d'] = 4
print("After adding key 'd':", d1)

print("\nSummary of Arithmetic Operations:")
print(f"List Sum: {l1}")
print(f"Tuple Sum: {tuple_sum}")
print(f"Set Sum: {s2}")
print(f"Dictionary Sum: {d1}")