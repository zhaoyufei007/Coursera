score = input("Enter Score: ")
try:
    sco = float(score)
except:
    sco = 2.0
if sco > 1:
    print("error!")
elif sco >= 0.9:
    print("A")
elif sco >= 0.8:
    print("B")
elif sco >= 0.7:
    print("C")
elif sco >= 0.6:
    print("D")
elif sco >= 0.0:
    print("F")
else:
    print("error!")
