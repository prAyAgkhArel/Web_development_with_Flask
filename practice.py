#decorating the functions say_hello, say_goodbye and say_goodnight
# lets add delay of 3 secs to the functions using time.sleep()
import time

#firstly define the decorator
def delay_decorator(function):
    def wrapper_function():  # wraps the function with some additional functionality
        #do something before executing actual function
        time.sleep(1)
        #running actual function twice
        function()
        function()
        #do something after executing actual function
        time.sleep(1)
        print("Greeting is done.   -from decorator\n")
    return wrapper_function   #the function is returned after wrapping

@delay_decorator   #passes say_hello to delay_decorator() and executes the wrapper function
def say_hello():
    print("Hello")

#@ is called "syntactic sugar"
@delay_decorator   # should be written just above the function to be decorated
def say_goodbye():
    print("Goodbye")

def say_goodnight():
    print("Goodnight")

say_hello()   #not only prints hello but does everthing which is inside wrapper function
say_goodbye()

# lets run  decorated say_goodnight() in some other way
decorated_goodnight = delay_decorator(say_goodnight)
# creating a decorated_goodnight passing say_goodnight to the decorator
#calling the decorated_goodnight
decorated_goodnight()