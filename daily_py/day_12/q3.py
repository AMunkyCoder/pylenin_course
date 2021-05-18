# From a list containing ints, strings and floats, make three lists to store them separately. 

my_list = [1, "Pylenin", 5.6]

int_list = []
str_list = []
float_list = []

for i in my_list:
    if isinstance(i, int):
        int_list.append(i)
    elif isinstance(i, str):
        str_list.append(i)
    elif isinstance(i, float):
        float_list.append(i)
    else:
        print("Data type not supported for value: ", i)
print("int: {}; str: {}; float: {}".format(int_list, str_list, float_list))