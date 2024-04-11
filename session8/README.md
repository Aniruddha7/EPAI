# Decorators 
A decorator is a python object that is used to modify functions or classes

In this assignment we will implement decorator to see how it changes the function and try to pass the given test cases

Instead of calling the outer function we use it to decorate the calling function

# Example function 

```python
def mul(a,b):
    return a*b
mul= logger(mul)
```

# We can also write it like this 
```python
@logger
def mul(a,b):
    return a*b
```

# odd it function:
odd_it function runs only during add seconds 

```python
def odd_it(fn):
    from functools import wraps
    from datetime import datetime
    from time import perf_counter

    """
    This function takes in other function and executes
    it during odd intervals/seconds
    """
    def inner(*args, **kwargs):
        if datetime.now().second %2 !=0:
            return fn(*args, **kwargs)
        else:
            print("We are Even")
    return inner
```
# logger 
logger funtion logs the details such as when was it called, funtion name, time taken to execute
```python
def logger(fn: "Function"):
    from functools import wraps
    from time import perf_counter
    from datetime import datetime, timezone

    '''
    This function takes in other function and logs the 
    details such as when was it called, funtion name, 
    time taken to execute
    '''

    @wraps(fn)
    def inner(*args, **kwargs):
        total_time=0
        run_time = datetime.now(timezone.utc)
        start=perf_counter()
        result = fn(*args, **kwargs)
        end=perf_counter()
        total_time+= (end-start)
        print(f'function_name {fn.__name__}: called at {run_time} with Execution time{total_time} ')
        print(f'Function description {fn.__doc__}' )
        print(f'Function annotation{fn.__annotations__}')
        return result
    return inner
```
### Decorator facroty is used for parameterized decorators

# authenticate 

The authenticate decorator factory takes in the password from user checks whether it matches with previously "set_password" and returns if its correct or no

```python
def authenticate(set_password):
    '''
    This is a decorator factory that takes in the password
    to pass and execute the function
    '''
    set_password= "secret"
    def dec(fn):
        from functools import wraps
        def inner(*args, **kwargs):
            if not args:
                raise TypeError
            elif args[0]==set_password:
                return "Amazing!"
            else:
                return "Wrong Password"
        return inner
    return dec
```
# timed 
The timed decorator factory takes in the function and calculates log of the function like total time taken to execute, function name average time and outputs the result

```python
def time_func(fn):
        from time import perf_counter
        from functools import wraps
        @wraps(fn)
        def inner(*args, **kwargs):
            total_time=0
            for i in range(reps):
                start= perf_counter()
                result= fn(*args, **kwargs)
                end= perf_counter()
                total_time+=(end-start)
            avgtime= total_time/reps
            print(f'function {fn.__name__} took total time {total_time} with average of {avgtime} and input parameter of {reps}')
            return result
        return inner
    return time_func
```
# privilege access

The privilege access decorator factory provides privilege access to 4,3,2 or 1 arguments to the function that has four free variables according to privilege levels high, medium, low or no set by factory call

```python
def decorator_factory(access:str):
    """
    This decorator factory provides privilege access to 4,3,2,1 arguments 
    to the function that has var1 va2 var3 var4 as free variables according to privilege level set by
    factory call
    """
    def param_func(fn):
        from functools import wraps
        var1= [1]
        var2= [2]
        var3= [3]
        var4= [4]
        @wraps(fn)
        def inner(*args, **kwargs):
            if access=="high":
                return var1, var2, var3, var4
            elif access=="mid":
                return var1, var2, var3
            elif access=="low":
                return var1, var2
            elif access=="no":
                return var1
            else:
                return "Improper access keyword set"
            return fn(*args, **kwargs)
        return inner
    return param_func
```