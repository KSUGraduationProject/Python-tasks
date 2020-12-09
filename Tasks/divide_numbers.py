from Tasks.check_validaty import is_valid_data_type

def divide_two_numbers(first_number, second_number):
    if is_valid_data_type(first_number) and is_valid_data_type(second_number):
        if second_number == 0:
            return "error"
        return int(first_number / second_number)
    else:
        return "error"
