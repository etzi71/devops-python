## 1 basic function definition, empty function

# def hello_func(x):
#     return(x)

# print(hello_func(21))

## 2 function defenition
# def hello_func():
#     print('hello function!')
#
# hello_func()
# hello_func()
# hello_func()
# hello_func()
# hello_func()

## 3 return of function and method on return
# def hello_func():
#     return 'hello function!'
# print(hello_func())
# print(hello_func().upper())

## function arguments, to show : error when without argument, default value argument, couple arguments
# def hello_func(greeting):
#     return '{} function!'.format(greeting)
#
# print(hello_func())

#####
# DRY principle keep your code clean without repeats. Don't repeat yourself !
# Concentred on input and return value of functions
#####

# Function with args and kwargs
def student_info(*args, **kwargs):
<<<<<<< HEAD
    print(args[0])
    print(kwargs["name"])
# #
# student_info('Math', 'Art', name='Jhon', age=22)
# print ("---")
courses = ['Math', 'Art']
info = {'name':'Jhon', 'age':22}

# student_info(courses, info)
# print ("---")
=======
    print(args)
    print(kwargs)
#
student_info('Math', 'Art', name='Jhon', age=22)
print ("---")
courses = ['Math', 'Art']
info = {'name':'Jhon', 'age':22}

student_info(courses, info)
print ("---")
>>>>>>> 855897c18b858437f0f64ea37cd2c096b7b72544
student_info(*courses, **info)