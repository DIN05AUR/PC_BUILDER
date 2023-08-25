from variables import options
from art import tprint
import variables

def show_welcome_art():
    tprint("pc  builder")
    print("Welcome to pc build expert system!")

#---------------------------------------------------------------------------------------------------------------------------
def show_option_box():
    shadow_box = "┌" + "─" * 38 + "┐\n"

    for key, value in options.items():
        shadow_box += f"│ {key}: {value}" + " " * (36 - len(f'{key}: {value}')) + "│\n"

    shadow_box += "└" + "─" * 38 + "┘"
    print(shadow_box)

#---------------------------------------------------------------------------------------------------------------------------

def show_divider():
    divider = "-" * 40
    print(divider)

#--------------------------------------------------------------------------------------------------------------------------
def show_asterisk_divider(length=60):
  print("*" * length)

#----------------------------------------------------------------------------------------------------------------------------

def print_budget_box(text):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)

    print('╭' + '─' * (max_length + 2) + '╮')
    for line in lines:
        print('│ ' + line + ' ' * (max_length - len(line)) + ' │')
    print('╰' + '─' * (max_length + 2) + '╯')
text = "Please choose an option:\n1: High\n2: Mid\n3: Low"

#------------------------------------------------------------------------------------------------------------------------

def show_multitask_box(text1):
    lines = text1.split('\n')
    max_length = max(len(line) for line in lines)

    print('╭' + '─' * (max_length + 2) + '╮')
    for line in lines:
        print('│ ' + line + ' ' * (max_length - len(line)) + ' │')
    print('╰' + '─' * (max_length + 2) + '╯')

#------------------------------------------------------------------------------------------------------------------------

def ask_multitask():
  print("Is multitasking your style of doing things?")
  show_multitask_box(variables.text1)
  multitasking = input("Please choose an option: ")
  return multitasking

#---------------------------------------------------------------------------------------------------------------------------

def print_quotation_1():
    print("Here is your quotation 1: ")
    for key, value in variables.quotation_1.items():
        print(f"{key}: {value}")

#---------------------------------------------------------------------------------------------------------------------------

def print_quotation_2():
    print("Here is your quotation 2: ")
    for key, value in variables.quotation_2.items():
        print(f"{key}: {value}")

#------------------------------------------------------------------------------------------------------------------------

def print_quotation_2():
    print("Here is your quotation 2: ")
    for key, value in variables.quotation_2.items():
        print(f"{key}: {value}")