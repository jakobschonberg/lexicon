#A1
course_name = "python" #global variable

def fun():
    course_name = "AI" #local variable
    print(course_name) #local variable

fun()
print(course_name) #global variable

#A2
a = 0
def set_a():
    a = 1
set_a()
print(a) #a is still 0

#A3
a = 0
def increase(a):
    return a + 1
a = increase(a)
print(a)

#A4
a = 0
b = 0
def fun():
    a = 1
    def fun_inner():
        b = 2
        print("inner",a,b)
    fun_inner()
    print("fun",a,b)
fun()
print("global",a,b)

#A5
def max_value(*args): #if we had called our function max here instead of max_value it would have overwritten the built-in max()
    return max(args) #built-in max works here since we didn't overwrite it
print(max_value(1, 2, 3, 4, 3))