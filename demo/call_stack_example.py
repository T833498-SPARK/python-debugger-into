def do_something_complicated(my_string: str) -> list[int]:
    return nondescript_function_1(my_string)
    

def nondescript_function_1(my_string):
    my_list = nondescript_function_2(my_string)
    reversed_list = my_list[::-1]
    return reversed_list

def nondescript_function_2(my_string):
    return my_string.split()

if __name__ == "__main__":
    do_something_complicated("Hello-World!")
    
    
    
    

