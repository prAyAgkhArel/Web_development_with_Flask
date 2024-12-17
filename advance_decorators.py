#if decorator function needs argument passed to a function then??

def logging_decorator(function):
    def wrapper(*args):        #use *args and *kwargs to take arguments passed
        print(f"You called {function.__name__}{args}")
        result = function(*args)
        print(f"It returned: {result}")
        return result

    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)