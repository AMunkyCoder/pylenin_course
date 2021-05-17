# Sort the below tuple in increasing order of the length of each element.

my_tuple = ("Pylenin", "loves", "Python")

list_tuple = list(my_tuple)
list_tuple.sort(key=len)
print(tuple(list_tuple))