Session2- Object Mutability and Interning

# In this session, our goal is to get the object out of cyclic references and clear memory using Garbage collector and the code should #be optimized in such a way that it uses less Python memory and perform better. In the above test_session2.py file there are ten test #cases that check for test_clear_memory, code performance and readme file content.

1 Something:
#In this class, a constructor is created in a method and it is referencing to SomethingNew class. __repr_ function is called representation and is used to print the objects. 

2 SomethingNew:
#In this class, the integer is set to 0 it calls "Something class". Basically, it is writter to create cyclic references.This techniquw causes memory leaks which we need to fix later.

3 add_something:
#This functions takes collection and 'i' as input parameters. It assigns the something new object to the one in Something class and appends to the list created in add_something function

4 clear_memory:
#This function takes the list from something class and creates collection. clear memory function is called from Python memory manager to remove circular references

5 critical_function:
#In this function, a list obect is called and stored in colection variable. It adds contents in collections and i variables 131072 #times and then calls clear_memory function. It uses add memory and clear memory functions

6 compare_strings_old:
#This function compares the string a and b that are multiplied 200 times with initial string and time is calculated. == or comparison operator is slower than is operator hence we check with is operator in compare_strings_new

7 compare_strings_new:
#This function compares the string a and b that are multiplied 200 times with initial string and time is calculated and total time is dvided by compare_strings_old. Performance Error is raised if it is greater or equal to 10 secs

#Here, is operator is faster comapared to (==) or comparison operator since the comparison operator compares each strings whereas 'is' operator represents both objects pointing to same variable.

8 sleep:
#This function is called to introduce delay in programs. It can be given as 2, 3, 6, 10secs etc. It is a built in function in time module and can be used as time.sleep()

9 char_list:
#char_list variable is assigned with a list and it is iterable. In string comparison menthod, the loop is ended if "d" is iterated in #the string. It means string is ended. Char_list is list that contains characters

10 collection:
#collections in python are containers that are used to store collections of data like list, dict, set, tuple etc and these are all #built-in collections defined in python. Most commonly used collections are counter, defaultdict, OrderedDict, deque, Chainedmap and #namedtuple()

11 __init__:
#This menthod is the constructor in python which is used to construct objects. Constructors assign values or initialize the data #members of the class during object creation. Constructor also contains set of statements to be executed when object is created. As #soon as object is created, this method is run.