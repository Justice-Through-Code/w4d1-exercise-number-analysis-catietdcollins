#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):
    #Followig the return statement use you will want to use the sum() function, with the range() function inside of the sum() parenthesis. In the range() parethesis you will put start, end and + 1(to be inclusive)
    return sum(range(start, end + 1))

# You will want to assign the function name(calculate_sum) to a variable so that you can print out the result. The calculate_sum() function should have 2 numbers in the argument(within the parenthesis)
get_sum = calculate_sum(0, 25)

# The final step will be printing your calculated sum,by means of the variable you made
print(get_sum)

"""
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """

    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.
#===============================================================================
def find_smallest_number(start, end):
    # Followig the return statement use the min() function with range inside the parenthesis. Inside the range parenthesis you will put start, end + 1(to make it inclusive)
    return min(range(start, end + 1))

# You will want to assign the function name(smallest_num) to a variable so that you can print out the result. The find_smallest_num() function should have 2 numbers in the argument(within the parenthesis)
smallest_number = find_smallest_number(0, 10)
print(smallest_number)

"""
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.

#===============================================================================
def find_largest_number(start, end):
        # Followig the return statement use the max() function with range inside the parenthesis. Inside the range parenthesis you will put start, end + 1(to make it inclusive)
    return max(range(start, end + 1))

# You will want to assign the function name(find_largest_number) to a variable so that you can print out the result. The find_largest_number() function should have 2 numbers in the argument(within the parenthesis)
largest_number = find_largest_number(0, 15)
print(largest_number)
"""
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.


def count_even_numbers(start, end):
    # Assign 0 to a variable, for the count of your function
    count_num = 0
    
    # Start a for loop to iterate through the numbers of the range. You'll put inside the range() parenthesis start, end + 1. To check if the nuber is odd you use the modulo operator(%) and see if it has a remainder of 2, by not equaling to 0.  If the number is odd, it will increment the number assigned to the variable made at the beginning (count_num). Return that variable.
    for i in range(start, end + 1):
        if i % 2 == 0:
            count_num += 1
    return count_num

# You will want to assign the function name(count_even_numbers) to a variable so that you can print out the result. The count_even_numbers() function should have 2 numbers in the argument(within the parenthesis)
even_numbers = count_even_numbers(0, 30)
print(even_numbers)
"""
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.

def count_odd_numbers(start, end):
    # Assign 0 to a variable
    count_odd = 0
    
    # Start a for loop to iterate through the numbers of the range. You'll put inside the range() parenthesis start, end + 1. To check if the nuber is odd you use the modulo operator(%) and see if it has a remainder of 2, by not equaling to 0.  If the number is odd, it will increment the number assigned to the variable made at the beginning (count_num). Return that variable.
    for i in range(start, end + 1):
        if i % 2 != 0:
            count_odd += 1
    return count_odd
    
# You will want to assign the function name(count_odd_numbers) to a variable so that you can print out the result. The count_odd_numbers() function should have 2 numbers in the argument(within the parenthesis)
odd_numbers = count_odd_numbers(0, 5)
print(odd_numbers)
"""
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.