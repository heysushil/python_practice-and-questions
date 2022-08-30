# Function bana hai.
    # function me 3 condtion honga hai
        # 1. volum up par 1+ hoga 
        # 2. volum down par -1 hoga
        # 3. power button par mobile on or off



def mobile_basic_function(user_action):
    if user_action == 1:
        # pass # volum up
        print('\n Volum up 5: ', 5 + user_action)
    elif user_action == 2:
        # pass # volum down
        print('\nVolum down 2: ', 2 - user_action)
    elif user_action == 3:
        print('\nMobile power on or off': bool(0))
    else:
        # pass # poser on off
        print('\nYou are entered wrong inuput try again with right on.')

print('''
----------------------
    Mobile actions
----------------------
1. Volum up
2. Volum down
3. Mobile Power On or Off
''')

user_input = int(input('\nEnter your mobile input: '))

# function call
mobile_basic_function(user_input)


# Example of logic bulding

# Chot lagi to kya karegne
#     rona hai 
#     4 ungli 

#     aumbulance
#     bleading stop karne ke koise 
#     padosi bula sakt home
#     dost ko bula sakte
#     ghar walo ko bula sakte ho 
#     nagdeek me clinei hai waha gaye 
#     najeek me hospital hhoga sakta hai 
#     medical ho waha ja sakte ho 



# Programs:

# 1: function bana hai 4 number user input le kar uska sum, subtract aur mutliplication karna hai, sabhi result seperate line me input number ke sath me result show karna hai.
    # Exam: User input 4 * 5 * 6 * 8 = result
    # 4 number user se jo input lena hai wo list me store karke aage pass karna hai.

    # list = [2,3,4,5] = list[0] * list[1]

# 2: function bana hai number odd/even check karn ke liye. user input se check kanr hai.

# 3 function bana hai ki user input de single numebr aur uska table print karna hai.

