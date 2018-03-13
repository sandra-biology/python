def str_replace(int_list, index):
    if int_list[index] < 5:
        int_list[index] = "small"
    else:
        int_list[index] = "large"
    return int_list

int_list = [2, 7, 8]
index = 0
print("int_list before:", int_list, "index =", index)

str_replace(int_list, index)
print("int_list after:", int_list)