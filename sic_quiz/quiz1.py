
def func(x):
    if x%2==0:
        return 1
    else: 
        return 2
result=func(func(3)+func(4))
print(result)                   #output: 2


list1=[1,2,3]
list2=list1.copy()
list2.append(4)
print(list1[1::1])              #output:[2,3]

lst=['a','b','c']
"".join(x for x in lst)       #""join.join(lst)
print(lst)                    # output: ['a', 'b', 'c']


def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function
closure=outer_function(5)
print(closure(3))             #output=8

#A closure happens when:
#You define a function inside another function.
#The inner function uses variables from the outer function.
#The outer function returns the inner function.
#The inner function remembers the values from the outer function, 
# even after the outer function finishes executing.


x=5
match x:
    case 0|1|2:
      print("low")
    case 3|4|5:
      print("medium")
    case _:
      print("high")           #output:medium


def mystery(a,b=[]):
    b.append(a)
    return b
print(mystery(1),end='')
print(mystery(2,[]),end='')
print(mystery(3),end='')         #output:[1][2][1,3]



def f(x):
   return x and f(x-1) or x
print(f(3))                       #output:1

x=2
match x:
    case 1|2:
      print("matched 1 or 2")
    case 3 if x>1:
      print("Matched 3 and x>1")
    case _:
      print("no match")           #matched 1 ot 2

for i in range(4):
    if i==2:
        break 
    else:
        print(i,end=',')
else:
    print("Done",end='@')          #output: 0,1,


try:
    x = 10 / 2
except ZeroDivisionError:
    print("Can't divide")
else:
    print("No errors occurred")  

#The else block runs only if the try block does NOT raise an exception.

#It is often used to keep the try block short —
#only code that might raise errors goes in try, and the safe code goes in else.


