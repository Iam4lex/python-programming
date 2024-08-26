# In python there are 2 types of variables

# 1. Local variables 
# These are variables that are created inside a function

def localVariable():

    myName = "Alex"

    print("MY name is ", myName)

localVariable() # call the function

# 2. Global variables
# These are variables that are created outside the function

myMessage = "Hello world"

def globalVariable(): # Define the function

    print("My message is ", myMessage)

globalVariable()

# 3. Using the global keyword
# The global keyword can be used to 

