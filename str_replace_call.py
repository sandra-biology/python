from myfunctions import str_replace

int_list = [2, 7, 8]
index = 0
print("int_list before:", int_list, "index =", index)

str_replace(int_list, index)
print("int_list after:", int_list)

float_list = [-0.5, 0.9, 3.14, 2.71828]

str_replace(float_list, index)
print("float_list after:", float_list)

