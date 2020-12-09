from Tasks.check_validaty import is_valid_data_type


def sums_two_numbers(first_number, second_number):
    if is_valid_data_type(first_number) and is_valid_data_type(second_number):
        return first_number + second_number
    else:
        return "error"
