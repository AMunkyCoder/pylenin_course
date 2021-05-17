# Convert the keys and values of the dictionary to tuple.

# my_dict = {"name" : "Pylenin",
#             "verb" : "loves",
#             "object": "Python"}

# Result ==> (("name", "Pylenin"), ("verb", "loves"), ("object", "Python"))

my_dict = {"name" : "Pylenin",
            "verb" : "loves",
            "object": "Python"}
my_tuple = []

for key, val in my_dict.items():
    my_tuple.append(tuple([key, val]))

print(tuple(my_tuple))