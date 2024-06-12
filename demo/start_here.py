import time
from datetime import datetime

def get_current_time():
    return time.time()

def is_greater(a: int, b: int) -> bool:
    print("Checking to see if a is greater than b...")   
    result = a < b
    
    if result:
        print(f"{a} is greater than {b}")
        
    else:
        print(f"{a} is not greater than {b}")
        
    return result
    


if __name__ == "__main__":
    a = 3
    b = 4
    print(f"{a=}")
    print(f"{b=}")
    
    result = is_greater(a, b)
    
    current_timestamp = get_current_time()
    
    # Create basic data structure
    my_list = [1, 2, 3, 4, 5]
    my_dictionary = {"name": "Richard", "position": "MLE"}
    my_tuple = (1, 2)
    my_set = {1, 2, 5, 3}

    

