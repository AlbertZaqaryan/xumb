# def test():
#     print(5)

# print(type(test()))
# -----------------------------------------
# def x():
#     return 5

# print(x() + 10)
# -----------------------------------------
# def myfunc(x):
#     return x ** 2

# number = int(input('Enter number: '))
# print(myfunc(number))
# -----------------------------------------
# import math

# print(math.sqrt(64))
# -----------------------------------------

# def armat(tiv):
#     return tiv ** 0.5

# print(armat(64))
# -----------------------------------------
# def func(a=5, b=6, c=10):
#     return a + b + c
# print(func(10, 7, 7))

# -----------------------------------------
# def func(a, b):
#     return a + b
# print(func(a=7, b=6))
# -----------------------------------------
# def func():
#     global x
#     x = 10
#     return x
# print(func())

# print(x)
# -----------------------------------------
# def func():
#     list_ = []
#     for i in range(5, 10):
#         list_.append(i)
#     return list_
# print(func())
# -----------------------------------------
# def func(*x):
#     return x
# print(func(4, 7, 8, 9, 5))
# -----------------------------------------
# def func(**kwargs):
#     return kwargs
# print(func(x=5, y=7, z=3))
# -----------------------------------------

# def fun1(num, tiv):
#     return num +tiv+ 25
# print(fun1(74,65))

# # fun1()
# def display_person(*args):
#     # for i in args:
#     #     print(i)
#     return args
# print(display_person("Emma", "25"))

# def display(**kwargs):
#     print(kwargs)

# #     for i in kwargs:
# #         print(i)

# display(emp="Kelly", salary=9000)


# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d

    # return inner_fun(a, b)
    # return a

# result = outer_fun(5, 10)
# print(result)


# def func(mylist):
#     if mylist == []:
#         return []
#     if type(mylist[0]) == int:
#         return [mylist[0]] + func(mylist[1:])
#     else:
#         return func(mylist[0]) + func(mylist[1:])

# mylist = [1, [2, 3, [4, 5, 6, [7, 8, [9, [10]]]]]]
# print(func(mylist))


def func(mylist):
    if mylist == []:
        return []
    return [mylist[0]] * mylist[1] + func(mylist[2:])
mylist = ['A', 12, 'B', 4, 'C', 3, 'A', 6, 'B', 2]
print(func(mylist))