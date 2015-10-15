__author__ = 'jc260183'
# Learn your tables - a learning tool written in Python
# By CP1404


def display_menu():
    print("""1. option 1
2. option 2
3. option 3
4. exit program""")


def num_range():
    start = input("Please enter a number to start from:")
    end = input("Please enter a number to end at: ")



#def generate_addition_table():
#   for i in range(10):
#       for j in range(10):
#          print(i, "+", j, "=", i + j)

#def generate_multiplication_table():
#   for i in range(10):
#       for j in range(10):
#           print(i, "*", j, "=", i * j)

#def generate_subtraction_table():
#    for i in range(10):
#        for j in range(10):
#            print(i, "-", j, "=", i - j)


def generate_table(operator, num_range):
    for i in range(num_range):
        for j in range(num_range):
            result = "?"
            if operator == "+":
                result = i + j
            elif operator == "*":
                result = i * j
            elif operator == "-":
                result = i - j
            print(i, operator, j, "=", result)


# the main loop - keeps the program running
running = True
while running:
    display_menu()
    user_choice = input("Choice: ")
    if user_choice == "1":
        generate_table("+", 15)
    elif user_choice == "2":
        generate_table("*", 15)
    elif user_choice =="3":
        generate_table("-", 15)
    elif user_choice == "4":
        running = False