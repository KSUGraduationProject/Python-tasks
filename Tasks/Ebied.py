"""
1. Write a function that sums two number.
2. Write a function that divides two numbers,
   but doesn't return a floating point value.
3. Write a function that sums a whole array of numbers.
4. Write a function that prints the even numbers from a given list.

---
Please note that:
1. Your functions should handle cases in which you don't
expect the same data type. In other words, 
your first function should fail if you tried to sum two strings.

2. Your test cases should cover every case you can think off.
"""


# 1. Write a function that sums two number.
def sum_two_nums(x, y):
    ans = float(x) + float(y)
    return ans


# 2. Write a function that divides two numbers,   but doesn't return a floating point value.
def divide_two_nums(x, y):
    ans = float(x) / float(y)
    return int(ans)


# 3. Write a function that sums a whole array of numbers.
def sum_arr(arr):
    ans = 0
    for x in arr:
        ans = ans + x
    return ans


# 4. Write a function that prints the even numbers from a given list.
def even_arr(arr):
    ans = []
    for x in arr:
        if x % 2 == 0: ans.append(x)
    return ans


num1 = float(input("Enter 1st number"))
num2 = float(input("Enter 2nd number"))
numbers = [1, 2, 3, 4]

print("sum of two numbers: ", sum_two_nums(num1, num2))
print("division of two numbers: ", divide_two_nums(num1, num2))
print("sum of all array: ", sum_arr(numbers))
print("even numbers in array: ", even_arr(numbers))
