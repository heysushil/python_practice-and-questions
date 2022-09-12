# Using second Function project and convert it into class
import random


class NumberGame:

    def __init__(self):
        pass

    def play():
        # user input to get users lucky number
        user_chooice = int(input('\nEnter your lucky number between 1 to 10: '))
        # condtion to check is user number math with system number or not.
        # if mathc user wins if not user loss
        system_number = random.randrange(1, 10)
        # print('\nRand number: ',system_number)

        if user_chooice == system_number:
            result = """
            #     --------------------------------
            #         Choose your lucky number 
            #     --------------------------------
            #     Your number is {}
            #     My number is {}
            #     --------------------------------
            #           You Won the match!
            #     --------------------------------
            """.format(user_chooice, system_number)
            print(result)
            # call again show message to show the message and not exit the user forcfully.
            show_message()
        else:
            print('\nYou loose the game try again.')
            show_message()

    # 1. user ko option show karna hai:

    def show_message():
        message = """
        #     --------------------------------
        #             Let's Start Game
        #     --------------------------------
        #     1. Play
        #     2. Exit 
        #     --------------------------------
        """
        print(message)
        user_input = input('\nEnter your chooice: ')
        # print('\nYour luck lucy number is', user_input)

        # check user input condition and call related function
        if user_input == '1':
            NumberGame.play()
        elif user_input == '2':
            print('\nThanks for playing and you are successfully exit form game.\n')
        else:
            print('\nYou enter wrong entry try again with only numbers 1 or 2\n')
            # again call same function it self form inside same function.
            NumberGame.show_message()


# first of all we need to creat a object of NumberGame class then call related methods or properties
# gameOBJ = NumberGame
# gameOBJ.show_message()