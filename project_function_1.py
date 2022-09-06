# Step 3: Define Function 
def sum_function(num_1, num_2):
    output = int(num_1) + int(num_2)
    output_message = '''
#   ----------------------------------
#           Your Activity Result 
#   ----------------------------------
#   Your Input values: {} + {}
#   ----------------------------------
#   Output           = {} 
#   ----------------------------------
    '''.format(num_1, num_2, output)

    result = {
        'output': output,
        'output_message': output_message,
    }
    return result

# Step 4: Function for showin message again and again using this fuction call
def show_message_function():
    message = '''
    #     ------------------------------
    #     Welcome to Python Calculater
    #     ------------------------------
    #     Choose your option:
    #     1. Sum 
    #     2. Subtract 
    #     3. Multiplication
    #     4. Exit/Stop 
    #     -------------------------------
    '''
    print(message)
    user_input = input('\nEnter your choose: ')
    return user_input

# Step 5: Function to check user_input option and behalf of that call related function
def choose_options(user_input):
    if user_input == '1':
        num_1 = input('\nEnter first number: ')
        num_2 = input('\nEnter second number: ')    
        # Sum function ko call kiya aur ye return me dictionary value lekar aaya
        # Jisme se hame 2nd key output_message ko result me show karaya.
        result = sum_function(num_1, num_2)
        print(result['output_message'])
        choose_options(show_message_function())
    elif user_input == '2':
        print('\nSubtract')
        choose_options(show_message_function())
    elif user_input == '3':
        print('\Multi')
    elif user_input == '4':
        print('\nExit')
    else:
        print('\nWrong input')


# Step 1: Show Message
message = '''
#     ------------------------------
#     Welcome to Python Calculater
#     ------------------------------
#     Choose your option:
#     1. Sum 
#     2. Subtract 
#     3. Multiplication
#     4. Exit/Stop 
#     -------------------------------
'''
print(message)
user_input = input('\nEnter your choose: ')

# Step 2: Multipal condtion to handel user input and send user to specific function with user input condtion:
if user_input == '1':
    num_1 = input('\nEnter first number: ')
    num_2 = input('\nEnter second number: ')    
    # Sum function ko call kiya aur ye return me dictionary value lekar aaya
    # Jisme se hame 2nd key output_message ko result me show karaya.
    result = sum_function(num_1, num_2)
    print(result['output_message'])
    
    # Ye function se hum use ka input user_input var me recive kar rahe hain
    user_input = show_message_function()
    # Is function se hum user_input ko choose_opton funciton me pass kar rahe hai taki user activiy ke hisab se input de aur usko uska resutl mile.
    choose_options(user_input)
elif user_input == '2':
    print('\nSubtract')
    choose_options(show_message_function())
elif user_input == '3':
    print('\Multi')
elif user_input == '4':
    print('\nExit')
else:
    print('\nWrong input')

