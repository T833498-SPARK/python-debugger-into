def add_to_list(my_number: int, my_list: list = []) -> list:
    """Add a number to a list and return the list."""
    my_list.append(my_number)
    return my_list


if __name__ == "__main__":
    number_one = 1
    number_two = 2
    print(f"{number_one=}")
    print(f"{number_two=}")
    
    
    list_with_a = add_to_list(number_one)
    list_with_b = add_to_list(number_two)
    print(f"List with a: {list_with_a}")
    print(f"List with b: {list_with_b}")
    