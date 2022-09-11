# Scope: Local, Global

globalVaraibel = '\nGlobla variable\n'

# method to chekc local varaible scope
def localFunction():
    localVariable = '\nMain localFunction ka varaibale hun\n'
    # Define function inside function
    def innerLocalFunction():
        print(localVariable)
        # inside sub function
    # Inside main funciton
    innerLocalFunction()
    # print(localVariable)
    print(globalVaraibel)
# 

# localFunction()
# innerLocalFunction()
# print(localVariable)
hello = 'hi'

# Global keyword
def localToGloableVariable():
    global local, a, b, c
    local = '\nMain Local variable hun\n'
    a = 'new value'
    # a,b,c,d = 1,2,3,4

localToGloableVariable()
print(local, a)