# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
# The first line of code has been defined as below.

def hello_name(user_name):
    print(user_name)

hello_name("hello_USERNAME!")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    """Print odd numbers 1-100, return nothing."""
    odd_numbers = list(range(1,101,2))
    print(odd_numbers)

first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of code has been defined as below.

def max_num_in_list(a_list):
    """Write a Python function, max_num_in_list to return the max number of a given list."""
    values = [5, 10, 15, 20, 25]
    print(max(values))

max_num_in_list(a_list='values')    


# Question 4
# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

a_year = 2000

if(is_leap_year):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. The return type should be boolean Type.

def is_consecutive(a_list):
    """Check to see if all numbers in a list are consecutive numbers."""
    list = [23, 20, 21, 22, 24]
    sorted_list = sorted(list)
    range_list = a_list(range(min(list), max(list) + 1))
    if sorted_list == range_list:
        print("a_list has consecutive numbers.")
    else:
        print("a_list has no consecutive numbers.")

is_consecutive(a_list=list)