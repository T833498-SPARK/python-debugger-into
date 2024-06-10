def select_value(input_2):
    return input_2[0]

def reverse_and_select(input_1):
    reversed_list = input_1[::-1]
    c = select_value(reversed_list)
    return c

def repeat_list(my_list: list[int]):
    value = reverse_and_select(my_list)
    return my_list * value

if __name__ == "__main__":
    result = repeat_list([1, 2, 3, 4, 5])
    print(result)