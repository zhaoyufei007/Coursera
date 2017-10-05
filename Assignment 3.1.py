hrs = input("Enter Hours:")
h = float(hrs)
rts = input("Enter Rate:")
r = float(rts)
if h <=40:
    pay = h*r
else:
    pay = 40*r+(h-40)*1.5*r
print(pay)