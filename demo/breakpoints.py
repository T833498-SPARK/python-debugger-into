def is_prime(number: int) -> bool:
    numbers_to_check = [number for number in range(2, number)]
    for i in numbers_to_check:
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    my_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    for number in my_numbers:
        if is_prime(number):
            print(f"{number} is prime")
        else:
            print(f"{number} is not prime")
    