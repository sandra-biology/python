def str_replace(int_list, index):
	"""The parameters are well defined variables!
	"""
    if int_list[index] < 5:
        int_list[index] = "small"
    else:
        int_list[index] = "large"
    return int_list
