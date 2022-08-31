# Simpal Function program:

# function: 1st function define 2nd function call

# Convert the code in function
def simple_sum(num1, num2):
    # Need these 2 variable as argument so that apply condton out side function
    # num1 = 100
    # num2 = 300

    result = num1 + num2
    return result
    # multiply = result * 2
    # print('\nSum of num1 and num2: ', result)


num1 = 100
num2 = 300
# print(type(int(simple_sum(num1, num2))))
# exit()

# Condtionn to check is num1 is graeter then num2



if num1 > num2:
    multiply = 2 * simple_sum(num1, num2)
    print('\nMultiply: ', multiply)
    # print('\nSum of num1 and num2: ', sum_result)
elif num1 >= num2:
    simple_sum(num1, num2)
    # print('\nSum of num1 and num2: ', sum_result)
elif num1 < num2:
    multiply = 2 * simple_sum(num1, num2)
    print('\nMultiply: ', multiply)
    # print('\nSum of num1 and num2: ', sum_result)




# Home work

# what is local and global varibales and how to use them?