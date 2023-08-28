import interpret_options
import functions
import select_ssd
import variables
from knowledge_base import knowledge_base

functions.show_welcome_art()
functions.show_asterisk_divider()


# ----------------------------------------------------------------------------------------------------------------------

def select_rams():
    if build_status == "heavy":
        if multitask == 1 and budget_option == 2:  # ram yes and budget mid

            ram_1 = knowledge_base["heavy"]["mid"]["rams"]["ram_1"]
            ram_2 = knowledge_base["heavy"]["mid"]["rams"]["ram_2"]
            ram_3 = knowledge_base["heavy"]["mid"]["rams"]["ram_3"]

            variables.quotation_1.update({"Ram": ram_1})
            variables.quotation_2.update({"Ram": ram_2})
            variables.quotation_3.update({"Ram": ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

        elif multitask == 1 and budget_option == 1:  # ram yes and budget high                         #exotic

            ram_1 = knowledge_base["heavy"]["high"]["rams"]["ram_1"]
            ram_2 = knowledge_base["heavy"]["high"]["rams"]["ram_2"]
            ram_3 = knowledge_base["heavy"]["high"]["rams"]["ram_3"]
            ram_4 = knowledge_base["heavy"]["high"]["rams"]["ram_4"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3
            final_ram_4 = ram_4

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            variables.quotation_4.update({"Ram": final_ram_4})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3, variables.quotation_4

        elif multitask == 1 and budget_option == 3:  # ram yes and budget low

            ram_1 = knowledge_base["heavy"]["low"]["rams"]["ram_1"]
            ram_2 = knowledge_base["heavy"]["low"]["rams"]["ram_2"]
            ram_3 = knowledge_base["heavy"]["low"]["rams"]["ram_3"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

        elif multitask == 2 and budget_option == 1:  # ram no and budget high                         #exotic

            ram_1 = knowledge_base["heavy"]["high"]["rams"]["ram_1"]
            ram_2 = knowledge_base["heavy"]["high"]["rams"]["ram_2"]
            ram_3 = knowledge_base["heavy"]["high"]["rams"]["ram_3"]
            ram_4 = knowledge_base["heavy"]["high"]["rams"]["ram_4"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3
            final_ram_4 = ram_4

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            variables.quotation_4.update({"Ram": final_ram_4})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3, variables.quotation_4

        elif multitask == 2 and budget_option == 2:  # ram no and budget mid
            ram_1 = knowledge_base["heavy"]["mid"]["rams"]["ram_1"]
            ram_2 = knowledge_base["heavy"]["mid"]["rams"]["ram_2"]
            ram_3 = knowledge_base["heavy"]["mid"]["rams"]["ram_3"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

        elif multitask == 2 and budget_option == 3:  # ram no and budget low
            ram_1 = knowledge_base["heavy"]["low"]["rams"]["ram_1"]
            ram_2 = knowledge_base["heavy"]["low"]["rams"]["ram_2"]
            ram_3 = knowledge_base["heavy"]["low"]["rams"]["ram_3"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

    elif build_status == "moderate":
        if multitask == 1 and budget_option == 1:  # ram yes and budget high
            ram_1 = knowledge_base["moderate"]["high"]["rams"]["16GB"]["ram_1"]
            ram_2 = knowledge_base["moderate"]["high"]["rams"]["32GB"]["ram_1"]

            ram_3 = knowledge_base["moderate"]["high"]["rams"]["16GB"]["ram_2"]
            ram_4 = knowledge_base["moderate"]["high"]["rams"]["32GB"]["ram_2"]

            ram_5 = knowledge_base["moderate"]["high"]["rams"]["16GB"]["ram_3"]
            ram_6 = knowledge_base["moderate"]["high"]["rams"]["32GB"]["ram_3"]

            final_ram_1 = " ".join([ram_1, ram_2])
            final_ram_2 = " ".join([ram_3, ram_4])
            final_ram_3 = " ".join([ram_5, ram_6])

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

        elif multitask == 1 and budget_option == 2:  # ram yes and budget mid
            ram_1 = knowledge_base["moderate"]["mid"]["rams"]["16GB"]["ram_1"]
            ram_2 = knowledge_base["moderate"]["mid"]["rams"]["32GB"]["ram_1"]

            ram_3 = knowledge_base["moderate"]["mid"]["rams"]["16GB"]["ram_2"]
            ram_4 = knowledge_base["moderate"]["mid"]["rams"]["32GB"]["ram_2"]

            ram_5 = knowledge_base["moderate"]["mid"]["rams"]["16GB"]["ram_3"]
            ram_6 = knowledge_base["moderate"]["mid"]["rams"]["32GB"]["ram_3"]

            final_ram_1 = " ".join([ram_1, ram_2])
            final_ram_2 = " ".join([ram_3, ram_4])
            final_ram_3 = " ".join([ram_5, ram_6])

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

        elif multitask == 1 and budget_option == 3:  # ram yes and budget low
            ram_1 = knowledge_base["moderate"]["low"]["rams"]["16GB"]["ram_1"]
            ram_2 = knowledge_base["moderate"]["low"]["rams"]["16GB"]["ram_2"]
            ram_3 = knowledge_base["moderate"]["low"]["rams"]["16GB"]["ram_3"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

        elif multitask == 2 and budget_option == 1:  # ram no and budget high
            ram_1 = knowledge_base["moderate"]["high"]["rams"]["16GB"]["ram_1"]
            ram_2 = knowledge_base["moderate"]["high"]["rams"]["16GB"]["ram_2"]
            ram_3 = knowledge_base["moderate"]["high"]["rams"]["16GB"]["ram_3"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

        elif multitask == 2 and budget_option == 2:  # ram no and budget mid
            ram_1 = knowledge_base["moderate"]["mid"]["rams"]["8GB"]["ram_1"]
            ram_2 = knowledge_base["moderate"]["mid"]["rams"]["8GB"]["ram_2"]
            ram_3 = knowledge_base["moderate"]["mid"]["rams"]["8GB"]["ram_3"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

        elif multitask == 2 and budget_option == 3:  # ram no and budget low
            ram_1 = knowledge_base["moderate"]["low"]["rams"]["8GB"]["ram_1"]
            ram_2 = knowledge_base["moderate"]["low"]["rams"]["8GB"]["ram_2"]
            ram_3 = knowledge_base["moderate"]["low"]["rams"]["8GB"]["ram_3"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

    elif build_status == "light":
        if multitask == 1 and budget_option == 1:  # ram yes and budget high
            ram_1 = knowledge_base["light"]["high"]["rams"]["16GB"]["ram_1"]
            ram_2 = knowledge_base["light"]["high"]["rams"]["16GB"]["ram_2"]
            ram_3 = knowledge_base["light"]["high"]["rams"]["16GB"]["ram_3"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

        elif multitask == 1 and budget_option == 2:  # ram yes and budget mid
            ram_1 = knowledge_base["light"]["mid"]["rams"]["16GB"]["ram_1"]
            ram_2 = knowledge_base["light"]["mid"]["rams"]["16GB"]["ram_2"]
            ram_3 = knowledge_base["light"]["mid"]["rams"]["16GB"]["ram_3"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

        elif multitask == 1 and budget_option == 3:  # ram yes and budget low
            ram_1 = knowledge_base["light"]["low"]["rams"]["8GB"]["ram_1"]
            ram_2 = knowledge_base["light"]["low"]["rams"]["8GB"]["ram_2"]
            ram_3 = knowledge_base["light"]["low"]["rams"]["8GB"]["ram_3"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

        elif multitask == 2 and budget_option == 1:  # ram no and budget high
            ram_1 = knowledge_base["light"]["high"]["rams"]["8GB"]["ram_1"]
            ram_2 = knowledge_base["light"]["high"]["rams"]["8GB"]["ram_2"]
            ram_3 = knowledge_base["light"]["high"]["rams"]["8GB"]["ram_3"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

        elif multitask == 2 and budget_option == 2:  # ram no and budget mid
            ram_1 = knowledge_base["light"]["mid"]["rams"]["8GB"]["ram_1"]
            ram_2 = knowledge_base["light"]["mid"]["rams"]["8GB"]["ram_2"]
            ram_3 = knowledge_base["light"]["mid"]["rams"]["8GB"]["ram_3"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

        elif multitask == 2 and budget_option == 3:  # ram no and budget low
            ram_1 = knowledge_base["light"]["low"]["rams"]["4GB"]["ram_1"]
            ram_2 = knowledge_base["light"]["low"]["rams"]["4GB"]["ram_2"]
            ram_3 = knowledge_base["light"]["low"]["rams"]["4GB"]["ram_3"]

            final_ram_1 = ram_1
            final_ram_2 = ram_2
            final_ram_3 = ram_3

            variables.quotation_1.update({"Ram": final_ram_1})
            variables.quotation_2.update({"Ram": final_ram_2})
            variables.quotation_3.update({"Ram": final_ram_3})
            return variables.quotation_1, variables.quotation_2, variables.quotation_3

    return variables.quotation_1, variables.quotation_2, variables.quotation_3

# ----------------------------------------------------------------------------------------------------------------------

print("\nWhat are you going to use your pc for?")
functions.show_option_box()
user_input = input("Enter options that's most applicable to you, separated by commas: ")
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
        print(
            "Invalid input format or out-of-range values.\nPlease choose only from the given options, separated by commas.")
    elif str(e) == "DuplicateError":
        print("Duplicate numbers detected. Please enter each option only once.")
    else:
        print("An error occurred. Please enter valid input.")
    exit(1)

# -----------------------------------------------------------------------------------------------------------------------

interpret_options.interpret_option(numbers)
result_list, gpu_required, build_status = interpret_options.interpret_option(numbers)
functions.print_budget_box(variables.text)

# -----------------------------------------------------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------------------------------------------------

functions.show_divider()
interpret_options.interpret_budget(budget_option)
# quotation_1, quotation_2, quotation_3, quotation_4 = interpret_options.interpret_budget(budget_option)

# -----------------------------------------------------------------------------------------------------------------------

multitask = functions.ask_multitask()
functions.show_asterisk_divider(60)
select_rams()
select_ssd.select_ssds(build_status,budget_option)
functions.print_quotation_1()
functions.show_divider()
functions.print_quotation_2()
functions.show_divider()
functions.print_quotation_3()
functions.show_divider()
if len(variables.quotation_4) > 0:
    functions.print_quotation_4()

# ----------------------------------------------------------------------------------------------------------------------

