my_list = [42, 69, 322, 13, 0, 99, 5]
my_list_len = len(my_list)
index = 0
while index < my_list_len and my_list[index] >= 0:
    if my_list[index] > 0:
        print(my_list[index])
    index += 1

