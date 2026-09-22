#F1
total_seconds = int(input("Total seconds: "))
seconds = total_seconds % 60
total_minutes = total_seconds // 60
minutes = total_minutes % 60
hours = total_minutes // 60
print(f"Hours: {hours}\nMinutes: {minutes}\nSeconds: {seconds}")

#F2
a = 4711
print(f"{a//1000} {(a%1000)//100} {a%100//10} {a%10}")

#F3
def mask(s):
    if(len(s) <= 4):
        return s
    r = s[:2]
    for _ in range(2, len(s)-2):
        r = r + "*"
    r = r + s[-2:]
    return r

s = input("Input: ")
print ("Masked: " + str(mask(s)))

#F4
import math, numpy
a = math.pi
print(f"{a} {type(a)}")
e = numpy.exp(1) # e^1
print(f"{e} {type(e)}")
ipi = complex(0,math.pi)
print(f"{ipi} {type(ipi)}")
a = e**ipi
print(f"{numpy.around(a)} {type(a)}")
a = "01234"
b = a[-1:-1:-1]
print(b)
c = a[-1:1:-1]
print(c)