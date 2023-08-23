import interpret_options
import functions
import variables

functions.show_option_box()

#----------------------------------------------------------------------------------------------------------------------

user_input = input("Enter option numbers separated by commas: ")
if not user_input:
    print("No input provided.")
    exit(1)

try:
    numbers = [int(num) for num in user_input.split(',')]
    # Check if all numbers are within the range of 0 to 16
    if not all(0 <= num <= 16 for num in numbers):
        raise ValueError("ValueError")
    # Check for duplicate numbers
    if len(numbers) != len(set(numbers)):
        raise ValueError("DuplicateError")
except ValueError as e:
    if str(e) == "ValueError":
        print("Invalid input format or out-of-range values.\nPlease choose only from the given options, separated by commas.")
    elif str(e) == "DuplicateError":
        print("Duplicate numbers detected. Please enter each option only once.")
    else:
        print("An error occurred. Please enter valid input.")
    exit(1)

#-----------------------------------------------------------------------------------------------------------------------

interpret_options.interpret_option(numbers)
result_list, gpu_required, build_status = interpret_options.interpret_option(numbers)
functions.print_budget_box(variables.text)

#-----------------------------------------------------------------------------------------------------------------------

while True:
    budget_option = input("Choose your budget option: ")

    if not budget_option:
        print("Error: Please enter a value.")
        continue

    if not budget_option.isdigit():
        print("Error: Invalid input format. Please enter a valid option.")
        continue

    budget_option = int(budget_option)

    if budget_option not in [1, 2, 3]:
        print("Error: Invalid budget option. Please choose 1 for 'high', 2 for 'mid', or 3 for 'low'.")
        continue

    break

#-----------------------------------------------------------------------------------------------------------------------

functions.show_divider()
interpret_options.interpret_budget(budget_option)
quotation_1, quotation_2 = interpret_options.interpret_budget(budget_option)
functions.print_quotation_1()
functions.show_divider()
functions.print_quotation_2()