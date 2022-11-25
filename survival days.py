x=input("DD/MM/YYYY: ")
y=input("DD/MM/YYYY: ")
a=int(x[6:])
b=int(x[3:5])
c=int(x[:2])
d=int(y[6:])
e=int(y[3:5])
f=int(y[:2])
from datetime import date
d0 = date(a, b, c)
d1 = date(d, e, f)
delta = d1 - d0
print("The number of days the person survived in the world:")
print(delta.days)
