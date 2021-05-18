# Write a Python program to convert the input_list to output_list.
# 
# input_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 
# output_lst = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

input_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

output_lst = list(zip(*input_lst))

print(output_lst)