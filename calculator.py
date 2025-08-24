"""
calculator.py
--------------
A simple command-line calculator project.

Features:
- Supports addition, subtraction, multiplication, and division.
- Accepts multiple numbers for a single operation.
- Rounds results to 2 decimal places.
- Handles invalid inputs and division by zero.
"""

def get_operation():
    """
    Ask the user to enter a valid operation.

    Returns:
        str: The operation ('add', 'subtract', 'multiply', or 'divide').
    """
    while True:
        operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
        if operation in ['add', 'subtract', 'multiply', 'divide']:
            return operation
        else:
            print("Invalid operation. Please enter one of: add, subtract, multiply, divide.")


def get_numbers():
    """
    Ask the user how many numbers they want to operate on.
    Ensures at least two numbers are required.

    Returns:
        int: The number of inputs for the operation.
    """
    while True:
        try:
            numbers = int(input("How many numbers do you want to operate on? "))
            if numbers >= 2:
                return numbers
            elif numbers < 2:
                print("You need at least two numbers to perform an operation.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_nums_list(numbers):
    """
    Collect a list of numbers from the user.

    Args:
        numbers (int): How many numbers to collect.

    Returns:
        list: List of floats entered by the user.
    """
    nums_lst = []
    for i in range(numbers):
        nums_lst.append(float(input(f"Enter number {i+1}: ")))
    return nums_lst


def perform_operation(operation, nums_lst):
    """
    Perform the selected mathematical operation on the list of numbers.

    Args:
        operation (str): The chosen operation ('add', 'subtract', 'multiply', 'divide').
        nums_lst (list): List of numbers on which operation will be performed.

    Returns:
        None
    """
    if operation == 'add':
        result = sum(nums_lst)
        result = round(result, 2)
        print(f"The result of addition is: {result}")

    elif operation == "subtract":
        result = nums_lst[0]
        for num in nums_lst[1:]:
            result -= num
        result = round(result, 2)
        print(f"The result of subtraction is: {result}")

    elif operation == "multiply":
        result = nums_lst[0]
        for num in nums_lst[1:]:
            result *= num
        result = round(result, 2)
        print(f"The result of multiplication is: {result}")

    elif operation == "divide":
        result = nums_lst[0]
        for num in nums_lst[1:]:
            if num == 0:
                print("Error: Division by zero is not allowed.")
                return None
            else:
                result /= num
        result = round(result, 2)
        print(f"The result of division is: {result}")


# Main Program Loop
if __name__ == "__main__":
    while True:
        operation = get_operation()
        numbers = get_numbers()
        nums_lst = get_nums_list(numbers)
        perform_operation(operation, nums_lst)

        allow = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if allow == "no":
            print("Exiting the calculator.")
            break
