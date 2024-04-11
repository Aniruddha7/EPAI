def docstr_func():

    '''In this function,we are putting the docstring to send it to other one to check whether the characters are more than 50 or not '''
    #
    return docstr_func.__doc__

def docstr_check(fn):

    '''This function takes the docstr_func() function and checks if the docstring length is more than 50 and it passes if its more'''
    length=50
    def inner():
        #print(fn.__doc__)
        if len(fn.__doc__)>=length:
            return True
        else:
            print("check string length")
    return inner


def next_fibonacci():

    """
    This function gives the next Fibonacci number
    """
    a = 0
    b = 1
    def fibonacci_calculate():
        
        """
        This function takes the input a,b and calculates the next fibonacci number
        """
        nonlocal a, b
        fibonacci = a + b
        a = b
        b = fibonacci
        return fibonacci
    return fibonacci_calculate


def add(x, y):
	'''
	returns addition of 2 input numbers
	'''
	return x + y


def mul(x, y):
	'''
	returns multiplication of 2 input numbers
	'''
	return x * y


def sub(x, y):
	'''
	returns subtraction of 2 input numbers
	'''
	return x - y


def div(x, y):

	'''
	returns division of 2 input numbers
	'''
	if bool(y):
		return x / y

counter_dict ={}

def counter(fn):
    '''
    This closure tracks how many times a function was called and updates the gloval dictionary variable counter_dict{} every time
        
    Functionality : This function defines global dictionary (counter) and a free variable (cnt). Defines another function which
                    increments the free variable whenever the function fn is called and stores in counter.
	'''
    count = 0
	
    def count_inc(*args, **kwargs):
        ''' This function increments the free variable count and updates the global dictionary.'''
        nonlocal count
        global counter_dict
        count += 1
        counter_dict[fn.__name__] = count
        return fn(*args, **kwargs)
    return count_inc

def modified_counter(fn, user_dict):
    '''
    This closure takes in specific dictionary to update counts
    Input= function fn and dictionary user_dict
    Output= inner function
    '''
    def counter_inc(*args, **kwargs):
        '''Updates the input dictionary with the count for the specific function fn.'''
        user_dict[fn.__name__] += 1
        return fn(*args, **kwargs)
    return counter_inc