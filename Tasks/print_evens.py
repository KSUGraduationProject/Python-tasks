from Tasks.check_validaty import is_valid_data_type
def print_even_numbers(numbers):
    for number in numbers:
        if is_valid_data_type(number) and number % 2 == 0:
            print(number)
