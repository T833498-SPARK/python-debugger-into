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
    result = is_greater(a, b)
    print(f"{result=}")
    

