from Tasks.check_validaty import is_valid_data_type


def summation_of_array(numbers):
    sum = 0
    for number in numbers:
        if is_valid_data_type(number):
            sum += number
        else:
            return "error"
    return sum
